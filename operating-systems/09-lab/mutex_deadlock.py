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
        time.sleep(0.1)
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
