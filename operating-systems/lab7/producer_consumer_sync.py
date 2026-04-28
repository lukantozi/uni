import threading
import time
import random
from queue import Queue
from threading import Semaphore

# Buffer size
BUFFER_SIZE = 5

# Shared buffer
buffer = Queue(BUFFER_SIZE)

# Semaphores
empty = Semaphore(BUFFER_SIZE)
full = Semaphore(0)
mutex = Semaphore(1)

# Producer function
def producer(pid):
    while True:
        item = random.randint(1, 100)
        time.sleep(random.uniform(0.5, 2)) # Simulate production time

        empty.acquire() # Wait for empty slot
        mutex.acquire() # Enter critical section
        buffer.put(item)
        print(f"Producer {pid} produced {item} | Buffer size: {buffer.qsize()}")
        mutex.release() # Exit critical section
        full.release() # Signal that item is available

# Consumer function
def consumer(cid):
    while True:
        full.acquire() # Wait for available item
        mutex.acquire() # Enter critical section
        item = buffer.get()
        print(f"Consumer {cid} consumed {item} | Buffer size: {buffer.qsize()}")
        mutex.release() # Exit critical section
        empty.release() # Signal that space is available
        time.sleep(random.uniform(0.5, 2)) # Simulate consumption time

# Start threads
producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

for t in producers + consumers:
    t.daemon = True
    t.start()

# Run simulation for 10 seconds
time.sleep(10)
print("Simulation complete.")
