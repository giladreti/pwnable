#define _GNU_SOURCE
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/syscall.h>

#define FUTEX_WAIT 0
#define FUTEX_LOCK_PI 6
#define FUTEX_UNLOCK_PI 7
#define FUTEX_WAIT_REQUEUE_PI 11
#define FUTEX_CMP_REQUEUE_PI 12

int futex(int *uaddr, int futex_op, int val, uint32_t val2, int *uaddr2, int val3)
{
    return syscall(SYS_futex, uaddr, futex_op, val, val2, uaddr2, val3);
}

int futex_wait(int *uaddr, int val)
{
    return futex(uaddr, FUTEX_WAIT, val, 0, NULL, 0);
}

int futex_lock_pi(int *uaddr)
{
    return futex(uaddr, FUTEX_LOCK_PI, 0, 0, NULL, 0);
}

int futex_unlock_pi(int *uaddr)
{
    return futex(uaddr, FUTEX_UNLOCK_PI, 0, 0, NULL, 0);
}

int futex_wait_requeue_pi(int *src, int *dst, int expected_val)
{
    return futex(src, FUTEX_WAIT_REQUEUE_PI, expected_val, 0, dst, 0);
}

int futex_cmp_requeue_pi(int *src, int *dst, int max_requeued_waiters, int expected_val)
{
    return futex(src, FUTEX_CMP_REQUEUE_PI, 1, max_requeued_waiters, dst, expected_val);
}