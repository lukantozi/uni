import threading
import time
import random
from queue import Queue
from threading import Semaphore
from datetime import datetime

# Buffer size
BUFFER_SIZE = 10

# Shared buffer
buffer = Queue(BUFFER_SIZE)

# Semaphores
empty = Semaphore(BUFFER_SIZE)
full = Semaphore(0)
mutex = Semaphore(1)

start_stamp = datetime.now().timestamp()

produced = 0
consumed = 0

# Producer function
def producer(pid):
    while True:
        item = random.randint(1, 100)
        time.sleep(random.uniform(0.05, 0.2)) # Simulate production time

        empty.acquire() # Wait for empty slot
        mutex.acquire() # Enter critical section
        buffer.put(item)
        prod_stamp = round(datetime.now().timestamp() - start_stamp, 2)
        print(f"Producer {pid} produced {item} | Buffer size: {buffer.qsize()} | Time: {prod_stamp}")
        global produced
        produced += 1
        with open("log.txt", "a") as l:
            l.write(f"Producer {pid} produced {item} | Buffer size: {buffer.qsize()} | Time: {prod_stamp}\n")
        mutex.release() # Exit critical section
        full.release() # Signal that item is available

# Consumer function
def consumer(cid):
    while True:
        full.acquire() # Wait for available item
        mutex.acquire() # Enter critical section
        item = buffer.get()
        cons_stamp = round(datetime.now().timestamp() - start_stamp, 2)
        print(f"Consumer {cid} consumed {item} | Buffer size: {buffer.qsize()} | Time: {cons_stamp}")
        global consumed
        consumed += 1
        with open("log.txt", "a") as l:
            l.write(f"Consumer {cid} consumed {item} | Buffer size: {buffer.qsize()} | Time: {cons_stamp}\n")
        mutex.release() # Exit critical section
        empty.release() # Signal that space is available
        time.sleep(random.uniform(2, 4)) # Simulate consumption time

# Start threads
producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(1)]

for t in producers + consumers:
    t.daemon = True
    t.start()

# Run simulation for 10 seconds
time.sleep(20)
print("Simulation complete.")
print(f"Produced: {produced}\nConsumed: {consumed}")

# Task 1
# Changing buffer size from 5 to 10 showed no significant changes when it comes to blocking producers.
# Reason to that is timing of producers/consumers; buffer limit was never hit since producers were not
# significantly faster than consumers

# Task 2
# When doubling the amount of producers, having buffer of size 10, the producers where blocked
# few times and the system was waiting for consumers to wake up so that they could produce items, and 
# producers could put more items in the buffer.

# Task 3
# As the script runs longer, producers have to wait until they can produce more, causing latency
# which is visible here: 
# Producer 1 produced 38 | Buffer size: 10 | Time: 17.15
# Consumer 0 consumed 50 | Buffer size: 9 | Time: 18.82
# Producer 0 produced 77 | Buffer size: 10 | Time: 18.82
# Consumer 1 consumed 92 | Buffer size: 9 | Time: 19.12
# Producer 3 produced 78 | Buffer size: 10 | Time: 19.12
# Simulation complete.

# Task 4
# Having two fast producers (0.05, 0.2), and one slow consumer (2, 4), buffer filled very quick,
# and producers had to wait until consumers would take the items from the buffer relatively slow.
# ❯ python producer_consumer_sync.py
# Producer 0 produced 25 | Buffer size: 1 | Time: 0.11
# Consumer 0 consumed 25 | Buffer size: 0 | Time: 0.11
# Producer 1 produced 49 | Buffer size: 1 | Time: 0.19
# Producer 0 produced 37 | Buffer size: 2 | Time: 0.25
# Producer 1 produced 67 | Buffer size: 3 | Time: 0.31
# Producer 0 produced 91 | Buffer size: 4 | Time: 0.43
# Producer 1 produced 15 | Buffer size: 5 | Time: 0.45
# Producer 0 produced 54 | Buffer size: 6 | Time: 0.57
# Producer 1 produced 85 | Buffer size: 7 | Time: 0.59
# Producer 1 produced 54 | Buffer size: 8 | Time: 0.66
# Producer 0 produced 100 | Buffer size: 9 | Time: 0.71
# Producer 1 produced 69 | Buffer size: 10 | Time: 0.72
# Consumer 0 consumed 49 | Buffer size: 9 | Time: 2.29
# Producer 1 produced 99 | Buffer size: 10 | Time: 2.29
# Consumer 0 consumed 37 | Buffer size: 9 | Time: 5.37
# Producer 0 produced 88 | Buffer size: 10 | Time: 5.37
# Consumer 0 consumed 67 | Buffer size: 9 | Time: 8.24
# Producer 1 produced 58 | Buffer size: 10 | Time: 8.24
# Consumer 0 consumed 91 | Buffer size: 9 | Time: 11.53
# Producer 0 produced 2 | Buffer size: 10 | Time: 11.53
# Consumer 0 consumed 15 | Buffer size: 9 | Time: 13.78
# Producer 1 produced 100 | Buffer size: 10 | Time: 13.78
# Consumer 0 consumed 54 | Buffer size: 9 | Time: 16.81
# Producer 0 produced 51 | Buffer size: 10 | Time: 16.81
# Simulation complete.

# Task 5
# Consumer 0 consumed 3 | Buffer size: 9 | Time: 2.9
# Producer 0 produced 91 | Buffer size: 10 | Time: 2.9
# Consumer 0 consumed 77 | Buffer size: 9 | Time: 5.22
# Producer 1 produced 89 | Buffer size: 10 | Time: 5.22
# Consumer 0 consumed 82 | Buffer size: 9 | Time: 8.68
# Producer 0 produced 22 | Buffer size: 10 | Time: 8.68
# Consumer 0 consumed 16 | Buffer size: 9 | Time: 12.35
# Producer 1 produced 14 | Buffer size: 10 | Time: 12.35
# Consumer 0 consumed 81 | Buffer size: 9 | Time: 14.83
# Producer 0 produced 19 | Buffer size: 10 | Time: 14.83
# Consumer 0 consumed 25 | Buffer size: 9 | Time: 18.42
# Producer 1 produced 80 | Buffer size: 10 | Time: 18.42
# Simulation complete.
# Produced: 17
# Consumed: 7
