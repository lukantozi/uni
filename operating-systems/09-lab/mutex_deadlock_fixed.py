import threading
import time
import random

mutex = threading.Lock()
mutex_1 = threading.Lock()
# Shared resource
counter = 0
shared_list = []

def critical_section_with_mutex(thread_id):
    global counter
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Thread {thread_id} is waiting to enter critical section")
        mutex.acquire()
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

threads = [threading.Thread(target=critical_section_with_mutex, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter value: {counter}")
#print(shared_list)

# Task 4

'''
In this version of mutex, I demonstrate a fixed version using the original
script, where each thread enters two critical sections, but nothing hangs
because every thread will enter sections in the same exact order, eliminating
anything going wrong.


❯ python mutex_deadlock_fixed.py
Thread 1 is waiting to enter critical section
Thread 1 has entered critical section
Thread 0 is waiting to enter critical section
...
...
...
Thread 2 has entered critical section
Thread 2 is leaving critical section
Thread 4 has entered critical section
Thread 4 is leaving critical section
Final counter value: 25

'''
