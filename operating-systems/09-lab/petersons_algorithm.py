import threading
import time


flag = [False, False]
turn = 0
count = 0

def process(id):
    other = 1 - id
    for _ in range(100):
        flag[id] = True
        global turn
        turn = other
        while flag[other] and turn == other:
            pass
        print(f'Process {id} is entering critical section')
#        time.sleep(0.5)
        global count
        count += 1
        flag[id] = False
        print(f'Process {id} has left critical section')

#t2 = threading.Thread(target=process, args=(1,))
threads = [threading.Thread(target=process, args=(i,)) for i in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(count)

# Task 5
'''
Thread 1 is leaving critical section
Thread 1 is waiting to enter critical section
Thread 1 has entered critical section
Thread 1 is leaving critical section
Final counter value: 200
python mutex_demo.py  0.01s user 0.01s system 106% cpu 0.015 total


Process 1 is entering critical section
Process 1 has left critical section
200
python petersons_algorithm.py  1.38s user 0.01s system 99% cpu 1.388 total

==========================
I ran both scripts without arbitrary time delays.

Comparison between two algorithms shows that using mutex is significanlty faster.
While peterson's algorithms just utilizes software to solve the entering
critical section issue, using mutex seems like an only reasonable way to manage
it if we care about performance.
'''
