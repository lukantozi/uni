import threading
import time
import random

semaphore = threading.Semaphore(3)
shared_list = []
counter = 0

def critical_section_with_semaphore(thread_id):
    global counter
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Thread {thread_id} is waiting for semaphore")
        semaphore.acquire()
        try:
            print(f"Thread {thread_id} has entered critical section")
            shared_list.append(thread_id)
            counter += 1
            time.sleep(random.uniform(0.1, 0.3))
            print(f"Thread {thread_id} is leaving critical section")
        finally:
            semaphore.release()

threads = [threading.Thread(target=critical_section_with_semaphore, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Final counter value: {counter}")

# Task 1
'''
❯ python semaphore_demo.py
Thread 1 is waiting for semaphore
Thread 1 has entered critical section
Thread 0 is waiting for semaphore
Thread 2 is waiting for semaphore
Thread 1 is leaving critical section
Thread 0 has entered critical section
Thread 0 is leaving critical section
Thread 2 has entered critical section
Thread 2 is leaving critical section
Thread 1 is waiting for semaphore
Thread 1 has entered critical section

In the demonstration above, it can be observed that only one thread can be
inside of the critical section. Once the thread enters the critical section
other threads have to wait for the thread in the critical section to
finish, and only then they can go into the section. The results are same,
because initiating semaphores with 1 (binary), is causing it to act like mutex.
'''

# Task 2
'''
Below script was run after making the modifications:
    semaphore = threading.Semaphore(3)
    for i in range(5)]

❯ python semaphore_demo.py
Thread 0 is waiting for semaphore
Thread 0 has entered critical section
Thread 4 is waiting for semaphore
Thread 4 has entered critical section
Thread 3 is waiting for semaphore
Thread 3 has entered critical section
Thread 4 is leaving critical section
Thread 0 is leaving critical section
Thread 2 is waiting for semaphore
Thread 2 has entered critical section
Thread 1 is waiting for semaphore
Thread 1 has entered critical section
Thread 3 is leaving critical section
Thread 2 is leaving critical section
Thread 1 is leaving critical section
Thread 4 is waiting for semaphore
Thread 4 has entered critical section

It can be observed that 3 threads can be present in the section
simultaneously when we intiate 5 threads in total.
'''
