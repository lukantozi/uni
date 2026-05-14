import threading
import time
import random

# Number of philosophers
NUM_PHILOSOPHERS = 10

# Create forks (as locks)
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

# Arbiter (Waiter)
arbiter = threading.Semaphore(NUM_PHILOSOPHERS - 1)

def philosopher(id):
    while True:
        print(f"Philosopher {id} is thinking")
        time.sleep(random.uniform(0.1, 0.5))
        
        print(f"Philosopher {id} is hungry")
        arbiter.acquire()
        time.sleep(random.uniform(0.5, 2))

        # Pick up forks
        left = forks[id]
        right = forks[(id + 1) % NUM_PHILOSOPHERS]

        with left:
            with right:
                print(f"Philosopher {id} is eating")
                time.sleep(random.uniform(0.1, 0.3))

        print(f"Philosopher {id} has finished eating")
        arbiter.release()
        time.sleep(random.uniform(0.5, 2))

# Create threads
threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]

for t in threads:
    t.start()

# Threads will run indefinitely; manually terminate the program to stop

# Task 1
"""
In this example I ran the script above and observed that the
forks are picked up without philosophers starving indefinitely.

❯ python dining_philosophers_arbiter.py
Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking
Philosopher 2 is hungry
Philosopher 2 is eating
Philosopher 4 is hungry
Philosopher 4 is eating
Philosopher 1 is hungry
Philosopher 3 is hungry
Philosopher 2 has finished eating
Philosopher 2 is thinking
Philosopher 1 is eating
Philosopher 0 is hungry
Philosopher 4 has finished eating
"""

# Task 2
"""
In neither instances of number of philosophers 6, 7, and 10
has the deadlock occured.

❯ python dining_philosophers_arbiter.py
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
Philosopher 0 is hungry
Philosopher 0 is eating
Philosopher 4 is hungry
Philosopher 4 is eating
Philosopher 2 is hungry
Philosopher 2 is eating
Philosopher 9 is hungry
Philosopher 3 is hungry
Philosopher 0 has finished eating
Philosopher 0 is thinking
Philosopher 9 is eating
"""

# Task 3
"""
Adding random delays (0.5, 2) showed that the in the initial
run philosophers started thinking and then most of
them got hungry, untill one of the first philosophers who
started to feel hungry used forks and after that all
philosophers started to use forks alternatively.

❯ python dining_philosophers_arbiter.py
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
Philosopher 8 is hungry
Philosopher 0 is hungry
Philosopher 9 is hungry
Philosopher 2 is hungry
Philosopher 7 is hungry
Philosopher 5 is hungry
Philosopher 6 is hungry
Philosopher 3 is hungry
Philosopher 4 is hungry
Philosopher 0 is eating
Philosopher 7 is eating
Philosopher 0 has finished eating
Philosopher 1 is hungry
Philosopher 9 is eating
Philosopher 7 has finished eating
Philosopher 6 is eating
Philosopher 6 has finished eating
"""
