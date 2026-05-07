import threading
import time
import random

mutex = threading.Lock()
mutex_1 = threading.Lock()
# Shared resource
counter = 0
shared_list = []

def critical_section_with_mutex_a(thread_id):
    global counter
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Thread {thread_id} is waiting to enter critical section")
        mutex.acquire()
        time.sleep(0.5)
        mutex_1.acquire()
        try:
            print(f"Thread {thread_id} has entered critical section")
            shared_list.append(thread_id)
            counter += 1
            time.sleep(random.uniform(0.1, 0.3))
            print(f"Thread {thread_id} is leaving critical section")
        finally:
            mutex_1.release()
            mutex.release()

def critical_section_with_mutex_b(thread_id):
    global counter
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Thread {thread_id} is waiting to enter critical section")
        mutex_1.acquire()
        time.sleep(0.5)
        mutex.acquire()
        try:
            print(f"Thread {thread_id} has entered critical section")
            shared_list.append(thread_id)
            counter += 1
            time.sleep(random.uniform(0.1, 0.3))
            print(f"Thread {thread_id} is leaving critical section")
        finally:
            mutex.release()
            mutex_1.release()

thread_a = threading.Thread(target=critical_section_with_mutex_a, args=("A",))
thread_b = threading.Thread(target=critical_section_with_mutex_b, args=("B",))

thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()
print(f"Final counter value: {counter}")

# Task 4
'''
To simulate this task, I decided to start two threads, each of them enetering
two critical states, locking two mutexes in alternate order. This is causing
thread execution to hang, since thread a locks first mutex, and before it tries
to lock the second mutex, thread b is locking it. At the same time, thread b
also wants to lock second mutex, but thread a is keeping it locked. Two make sure
that both threads would lock their initial mutexes successfully, i had to manually
delay inbetween lock, so that the simulation of infinite hang would be possible.

❯ python mutex_deadlock.py
Thread A is waiting to enter critical section
Thread B is waiting to enter critical section

'''
