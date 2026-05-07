import threading
import time
import random

mutex = threading.Lock()

# Shared resource
counter = 0
shared_list = []

def critical_section_with_mutex(thread_id):
    global counter
    for _ in range(100):
        #time.sleep(random.uniform(0.1, 0.5))
        print(f"Thread {thread_id} is waiting to enter critical section")
        mutex.acquire()
        try:
            print(f"Thread {thread_id} has entered critical section")
            shared_list.append(thread_id)
            counter += 1
            #time.sleep(random.uniform(0.1, 0.3))
            print(f"Thread {thread_id} is leaving critical section")
        finally:
            mutex.release()

threads = [threading.Thread(target=critical_section_with_mutex, args=(i,)) for i in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Final counter value: {counter}")

# Task 1
'''
❯ python mutex_demo.py
Thread 1 is waiting to enter critical section
Thread 1 has entered critical section
Thread 2 is waiting to enter critical section
Thread 0 is waiting to enter critical section
Thread 1 is leaving critical section
Thread 2 has entered critical section
Thread 2 is leaving critical section
Thread 0 has entered critical section
Thread 0 is leaving critical section

In the demonstration above, it can be observed that only one thread can be
inside of the critical section. Once the thread enters the critical section
other threads have to wait for the thread in the critical section to
finish, and only then they can go into the section. 
'''

# Task 2
'''
❯ python mutex_demo.py
Thread 2 is waiting to enter critical section
Thread 2 has entered critical section
Thread 4 is waiting to enter critical section
Thread 3 is waiting to enter critical section
Thread 2 is leaving critical section
Thread 4 has entered critical section
Thread 1 is waiting to enter critical section
Thread 0 is waiting to enter critical section
Thread 4 is leaving critical section
Thread 3 has entered critical section
Thread 2 is waiting to enter critical section
Thread 3 is leaving critical section
Thread 1 has entered critical section
Thread 4 is waiting to enter critical section
Thread 1 is leaving critical section
Thread 0 has entered critical section
Thread 3 is waiting to enter critical section
Thread 0 is leaving critical section
Thread 2 has entered critical section
Thread 1 is waiting to enter critical section
Thread 2 is leaving critical section

In this version, the number of threads intiated was increased from 3
to 5 and it is easy to see that nothing has changed: threads initated
have to wait for the one in the critical section to leave.
'''
