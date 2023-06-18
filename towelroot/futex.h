#include <stdint.h>

struct list_head
{
    struct list_head *next;
    struct list_head *prev;
};

struct plist_node
{
    int prio;
    struct list_head prio_list;
    struct list_head node_list;
};

struct rt_mutex_waiter
{
    struct plist_node list_entry;
    struct plist_node pi_list_entry;
    struct task_struct *task;
    struct rt_mutex *lock;
};

// taken from arch/arm
struct thread_info {
    unsigned long flags; /* low level flags */
    int preempt_count; /* 0 => preemptable, <0 => bug */
    unsigned long addr_limit;
    struct task_struct *task; /* main task structure */
};

// a bit of cheating...
typedef unsigned int kuid_t;
typedef unsigned int kgid_t;
typedef unsigned int atomic_t;

struct cred {
    atomic_t usage;
    kuid_t uid; /* real UID of the task */
    kgid_t gid; /* real GID of the task */
    kuid_t suid; /* saved UID of the task */
    kgid_t sgid; /* saved GID of the task */
    kuid_t euid; /* effective UID of the task */
    kgid_t egid; /* effective GID of the task */
    kuid_t fsuid; /* UID for VFS ops */
    kgid_t fsgid; /* GID for VFS ops */
};

int futex(int *uaddr, int futex_op, int val, uint32_t val2, int *uaddr2, int val3);
int futex_wait(int *uaddr, int val);
int futex_lock_pi(int *uaddr);
int futex_unlock_pi(int *uaddr);
int futex_wait_requeue_pi(int *src, int *dst, int expected_val);
int futex_cmp_requeue_pi(int *src, int *dst, int max_requeued_waiters, int expected_val);
