import threading
import time
import random

NUM_PHILOSOPHERS = 10
MAX_CYCLES = 10

forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

think_times = [[] for _ in range(NUM_PHILOSOPHERS)]
eat_times   = [[] for _ in range(NUM_PHILOSOPHERS)]

def philosopher(id):
    cycle = 0
    while cycle < MAX_CYCLES:
        t0 = time.time()
        print(f"Philosopher {id} is thinking")
        time.sleep(random.uniform(0.1, 0.5))
        think_times[id].append(time.time() - t0)

        print(f"Philosopher {id} is hungry")

        first = id
        second = (id + 1) % NUM_PHILOSOPHERS
        if id == NUM_PHILOSOPHERS - 1:
            first, second = second, first

        forks[first].acquire()
        forks[second].acquire()

        t0 = time.time()
        print(f"Philosopher {id} is eating")
        time.sleep(random.uniform(0.1, 0.3))
        eat_times[id].append(time.time() - t0)

        forks[second].release()
        forks[first].release()

        print(f"Philosopher {id} has finished eating")
        time.sleep(random.uniform(0.5, 2))
        cycle += 1

    avg_think = sum(think_times[id]) / len(think_times[id])
    avg_eat   = sum(eat_times[id])   / len(eat_times[id])
    print(f"[STATS] Philosopher {id} | avg think: {avg_think:.3f}s | avg eat: {avg_eat:.3f}s")

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]
for t in threads:
    t.start()

# Task 5
"""
After running maximum of 10 cycles for each philosopher, the output
belo was yielded.
Overall, both approaches prevent deadlock, but the fork-ordering method
showed better observed fairness and throughput in my experiments, while
the arbiter method adds a global limiter that can reduce concurrency
and still allows theoretical starvation.

[STATS] Philosopher 4 | avg think: 0.336s | avg eat: 0.198s
[STATS] Philosopher 8 | avg think: 0.215s | avg eat: 0.204s
[STATS] Philosopher 5 | avg think: 0.298s | avg eat: 0.198s
[STATS] Philosopher 2 | avg think: 0.255s | avg eat: 0.230s
[STATS] Philosopher 9 | avg think: 0.300s | avg eat: 0.227s
[STATS] Philosopher 7 | avg think: 0.323s | avg eat: 0.191s
[STATS] Philosopher 1 | avg think: 0.281s | avg eat: 0.185s
[STATS] Philosopher 0 | avg think: 0.299s | avg eat: 0.213s
[STATS] Philosopher 3 | avg think: 0.354s | avg eat: 0.183s
[STATS] Philosopher 6 | avg think: 0.308s | avg eat: 0.218s
"""

# Task
"""
Task 6 comparison:
The arbiter solution prevents deadlock by allowing at most N-1 philosophers
to compete for forks at the same time. This makes the solution simple and safe,
but it introduces a global bottleneck because a philosopher must first obtain
permission from the semaphore before attempting to pick up forks.

The fork-ordering solution prevents deadlock by enforcing a fixed resource
acquisition order. In this approach, non-adjacent philosophers can eat in
parallel without waiting for a central arbiter, so throughput is typically higher.

In terms of fairness, both approaches avoided deadlock in my experiments, but
fork-ordering showed more balanced behavior in the observed runs. The arbiter
approach can still lead to longer waiting for some philosophers, while the
fork-ordering approach distributed access more evenly in practice.
"""
