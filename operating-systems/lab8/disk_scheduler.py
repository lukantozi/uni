# SSTF Implementation
def sstf(requests, head):
    sequence = []
    total_seek = 0
    requests = requests.copy()
    while requests:
        distances = [abs(r - head) for r in requests]
        idx = distances.index(min(distances))
        total_seek += abs(requests[idx] - head)
        head = requests.pop(idx)
        sequence.append(head)
    return sequence, total_seek

# Example usage:
reqs = [98, 183, 37, 122, 14, 124, 65, 67]
order, seek_time = sstf(reqs, 100)
print("SSTF order:", order)
print("Total seek time:", seek_time, end="\n\n")
reqs1 = sorted(reqs, reverse=True)
order1, seek_time1 = sstf(reqs1, 100)
print(f"reverse sorted requests input -> {reqs1}")
print("SSTF order:", order1)
print("Total seek time:", seek_time1, end="\n\n")

# Task 1 comment:
# order of the requests have no effect on seek time and in sstf algorithm, since it is
# designed to pick the nearest one each time  from the pool

# SCAN Implementation
def scan(requests, head, direction='up', disk_size=100):
    sequence = []
    total_seek = 0
    requests = sorted(requests)
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    if direction == 'up':
        for r in right:
            sequence.append(r)
            total_seek += abs(head - r)
            head = r
        if left:
            total_seek += abs(head - disk_size + 1)
            head = disk_size - 1
            for r in reversed(left):
                sequence.append(r)
                total_seek += abs(head - r)
                head = r
    else:
        for r in reversed(left):
            sequence.append(r)
            total_seek += abs(head - r)
            head = r
        if right:
            total_seek += abs(head - 0)
            head = 0
            for r in right:
                sequence.append(r)
                total_seek += abs(head - r)
                head = r

    return sequence, total_seek

# Example:
order, seek_time = scan(reqs, 100, 'up')
print("SCAN order:", order)
print("Total seek time:", seek_time, end="\n\n")

# LOOK implementation
def look(requests, head, direction='up'):
    sequence = []
    total_seek = 0
    requests = sorted(requests)
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    if direction == 'up':
        for r in right:
            sequence.append(r)
            total_seek += abs(head - r)
            head = r
        if left:
            for r in reversed(left):
                sequence.append(r)
                total_seek += abs(head - r)
                head = r
    else:
        for r in reversed(left):
            sequence.append(r)
            total_seek += abs(head - r)
            head = r
        if right:
            for r in right:
                sequence.append(r)
                total_seek += abs(head - r)
                head = r

    return sequence, total_seek

# Example:
order, seek_time = look(reqs, 100)
print("LOOK order:", order)
print("Total seek time:", seek_time, end="\n\n")

# Task 2: a)
# LOOK algorithm is way faster than SCAN algorithm, since it does not waste time to go to
# extremes of the disk and only goes up and down to the requests located at the end of each
# direction, cutting the time to scan all the disk.


# C-SCAN Implementation
def c_scan(requests, head, disk_size=100):
    sequence = []
    total_seek = 0
    requests = sorted(requests)
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    for r in right:
        sequence.append(r)
        total_seek += abs(head - r)
        head = r

    if left:
        total_seek += abs(head - (disk_size - 1)) + (disk_size - 1)
        head = 0
        for r in left:
            sequence.append(r)
            total_seek += abs(head - r)
            head = r

    return sequence, total_seek

# Example:
order, seek_time = c_scan(reqs, 100)
print("C-SCAN order:", order)
print("Total seek time:", seek_time, end="\n\n")


# C-LOOK implementation
def c_look(requests, head):
    sequence = []
    total_seek = 0
    requests = sorted(requests)
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    for r in right:
        sequence.append(r)
        total_seek += abs(head - r)
        head = r

    if left:
        for r in left:
            sequence.append(r)
            total_seek += abs(head - r)
            head = r

    return sequence, total_seek

# Example:
order, seek_time = c_look(reqs, 100)
print("C-LOOK order:", order)
print("Total seek time:", seek_time, end="\n\n")

# Task 2: b)
# C-LOOK implementation cuts time compared to C-SCAN, as it does not go to the extremes of the disk
# when returning to the left side, it lands on the leftmost request, cutting overall seek time.

# Task 3:
# Choosing the starting head 150 (compared to initial 53), C-SCAN and SCAN algorithms showed
# not significant changes, while SSTF algorithms seek time increased significantly, and 
# LOOK algorithm showed the best improvement (299 -> 202).

# Choosing the starting head at position 0 gives exact same seek time among all algorithms:
# SSTF order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 183
# 
# reverse sorted requests input -> [183, 124, 122, 98, 67, 65, 37, 14]
# SSTF order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 183
# 
# SCAN order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 183
# 
# LOOK order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 183
# 
# C-SCAN order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 183
# 
# C-LOOK order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 183
#
# Choosing starting head position at 199, circular algorithms show the worst outcome,
# while rest of the algorithms show similar result as when the head starts at 0.

# SSTF order: [183, 124, 122, 98, 67, 65, 37, 14]
# Total seek time: 185
# 
# reverse sorted requests input -> [183, 124, 122, 98, 67, 65, 37, 14]
# SSTF order: [183, 124, 122, 98, 67, 65, 37, 14]
# Total seek time: 185
# 
# SCAN order: [183, 124, 122, 98, 67, 65, 37, 14]
# Total seek time: 185
# 
# LOOK order: [183, 124, 122, 98, 67, 65, 37, 14]
# Total seek time: 185
# 
# C-SCAN order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 382
# 
# C-LOOK order: [14, 37, 65, 67, 98, 122, 124, 183]
# Total seek time: 354

# Having the head in the ~middle at 100 position, 
