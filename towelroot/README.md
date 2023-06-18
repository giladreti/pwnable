# setup
kernel symbols were obtained by running https://github.com/marin-m/vmlinux-to-elf on the given zImage. a simple fix must be made in order to correctly determine base address - `first_symbol_virtual_address` should not include symbols of address 0, as they do not point to part of the kernel image.

# vuln
there are many resources online. if i understand correctly, the key point is that the developer of the futex api did not intend that a pi -> pi requeue should be possible.

we can see that the waiter (`futex_wait_requeue_pi`) expects to be woken up in 1 of 2 ways:
1. `futex_cmp_requeue_pi` was able to acquire the lock and woke us up (in this case we are not in the waiter lists as we never waited for the lock so no cleanups are needed)
2. we couldn't acquire the lock and started waiting on it. then we were woken up in some other way and we need to clean up
now since the waiter cleans up after itself and does not expect any other wake up, if we enter the first case while waiting we will not get cleaned up. for this to happen we must requeue and wait (in order to create a waiter) and then somehow still be woken up by a requeue, which can be only be done by requeing to another pi lock and succeeding. this can be done by force releasing the futex and requeing onto itself which explains the rest of the vuln triggering. the self requeue is possible (and in fact the only possibility) since `requeue_pi_key` is not cleared when we requeue and wait for the second futex, so that any requeue of the waiter to the second futex is possible (as only `requeue_pi_key` is compared)
another problem occurs if the uafed waiter is the only waiter - in this case `lookup_pi_state` will create a new `pi_state` for us on which will get freed when the function returns (as we will be the only referents). since it contains the internal `pi_mutex` (which contains our `wait_list` linked list with the uafed waiter reference). thus, we need to create another reference to the state, so we attempt to lock it before. in fact, the `lookup_pi_state` fails as the futex is now locked on our waiter and thus the pid comparison to the first waiter (our additional one) fails, and we requeue no waiters.

so to summarize, those are the steps and why they are needed:
1. lock pi futex (so that the next step will create a waiter)
2. requeue (wait then cmp) non pi onto pi and create a waiter since pi is locked (so that we have something to uaf)
3. lock pi futex again (to create a new waiter - this will prevent the `pi_state` from freeing in the last step)
4. force release pi in usermode (so that next requeue will acquire the lock and wake the waiter itself)
5. requeue pi onto itself (this wakes the waiter which will think it succeeded in the first requeue and thus has not created any waiter state) (we can requeue to itself and only to itself as explained above)

this explains why this is not a bug in a non_pi -> pi requeue as in this case the waiter assumptions are correct and we indeed wake up by one those 2 ways and also why bug cannot be triggered by waking the pi futex (instead of releasing in usermode and requeuing to itself to wakeup) since `wake_futex_pi` will not reset `q.rt_waiter` and we will enter the second case in `futex_wait_requeue_pi` which will `rt_mutex_finish_proxy_lock` which cleans the lists up via `remove_waiter` (presumably)

# exploit
the exploit is pretty simple, we get a uafed stack waiter, overwrite it with our data so that it points to a next waiter in usermode, then inserting new waiters before the usermode waiter writes the new waiter's address to `fake_waiter.prev->next` so we can write a pointer to an absolute address. we use this to first write it to usermode and thus leak a kernel stack address, then use this stack address to overwrite the thread's `addr_limit` and obtain kernel RW.