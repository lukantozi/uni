import threading
import time
import random

NUM_PHILOSOPHERS = 10
STARVATION_THRESHOLD = 3.0

wait_start = [None] * NUM_PHILOSOPHERS

forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

def philosopher(id):
    while True:
        print(f"Philosopher {id} is thinking")
        time.sleep(random.uniform(0.1, 0.5))

        wait_start[id] = time.time()
        print(f"Philosopher {id} is hungry")

        # To avoid deadlock, pick lower-numbered fork first
        first = id
        second = (id + 1) % NUM_PHILOSOPHERS

        if id == NUM_PHILOSOPHERS - 1:
            first, second = second, first

        while True:
            wait_time = time.time() - wait_start[id]
            others_starving = any(
                wait_start[j] is not None
                and (time.time() - wait_start[j] > wait_time + STARVATION_THRESHOLD)
                for j in range(NUM_PHILOSOPHERS) if j != id
            )
            if not others_starving:
                break
            time.sleep(0.5)

        forks[first].acquire()
        forks[second].acquire()

        print(f"Philosopher {id} is eating")
        time.sleep(random.uniform(0.1, 0.3))

        forks[second].release()
        forks[first].release()
        time.sleep(random.uniform(0.5, 2))

        print(f"Philosopher {id} has finished eating")

threads = [threading.Thread(target=philosopher, args=(i,)) for i in
range(NUM_PHILOSOPHERS)]

for t in threads:
    t.start()

# Task 1
"""
In this task I ran the script above and observed that the
philosophers pick up forks in order and can eat indefinitely.


❯ python dining_philosophers_fork_ordering.py
Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking
Philosopher 1 is eating
Philosopher 4 is eating
Philosopher 4 has finished eating
Philosopher 4 is thinking
Philosopher 1 has finished eating
Philosopher 1 is thinking
Philosopher 2 is eating
Philosopher 0 is eating
Philosopher 2 has finished eating
Philosopher 2 is thinking
Philosopher 3 is eating
Philosopher 0 has finished eating
Philosopher 0 is thinking
Philosopher 3 has finished eating
"""

# Task 2
"""
In neither instances of number of philosophers 6, 7, and 10
has the deadlock occured.

❯ python dining_philosophers_fork_ordering.py
Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking
Philosopher 5 is thinking
Philosopher 6 is thinking
Philosopher 7 is thinking
Philosopher 8 is thinking
Philosopher 9 is thinking
Philosopher 2 is eating
Philosopher 6 is eating
Philosopher 0 is eating
Philosopher 2 has finished eating
"""

# Task 3
"""
Adding random delays (0.5, 2) showed that the in the initial
run of all of the philosophers were thinking and then once some of the 
philosophers started eating. There were no starvations observed, unlike
arbiter method.

❯ python dining_philosophers_fork_ordering.py
Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking
Philosopher 5 is thinking
Philosopher 6 is thinking
Philosopher 7 is thinking
Philosopher 8 is thinking
Philosopher 9 is thinking
Philosopher 2 is eating
Philosopher 4 is eating
Philosopher 6 is eating
Philosopher 0 is eating
Philosopher 8 is eating
Philosopher 2 has finished eating
Philosopher 2 is thinking
Philosopher 5 is eating
Philosopher 6 has finished eating
Philosopher 6 is thinking
Philosopher 3 is eating
Philosopher 0 has finished eating
"""

# Task 4
"""
For this task I've introduced logic where if the
philosopher is waiting for a long time, it gets accessed
to the fork, which is shown in the output. Philosopher
6 got hungry and ate right after that.

❯ python dining_philosophers_fork_ordering.py
Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking
Philosopher 5 is thinking
Philosopher 6 is thinking
Philosopher 7 is thinking
Philosopher 8 is thinking
Philosopher 9 is thinking
Philosopher 6 is hungry
Philosopher 6 is eating
Philosopher 9 is hungry
Philosopher 9 is eating
Philosopher 7 is hungry
Philosopher 7 is eating
Philosopher 5 is hungry
Philosopher 5 is eating
Philosopher 0 is hungry
Philosopher 0 is eating
Philosopher 2 is hungry
Philosopher 2 is eating
"""
