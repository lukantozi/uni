import random


# FIFO Algorithm
def fifo(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                memory.pop(0)
            memory.append(page)

    return page_faults


# LRU Algorithm
def lru(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                memory.pop(0)
            memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)

    return page_faults


# RAND Algorithm
def rand_algo(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                # Evict a random page
                evict_index = random.randint(0, capacity - 1)
                memory[evict_index] = page
            else:
                memory.append(page)

    return page_faults


# opt algorithm
def opt(pages, capacity):
    memory = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) < capacity:
                # need to know the future
                memory.append(page)
            else:
                future_uses = {}
                for p in memory:
                    try:
                        future_uses[p] = pages[i + 1:].index(p)
                    except ValueError:
                        future_uses[p] = float('inf')

                evict = max(future_uses, key=lambda p: future_uses[p])
                memory[memory.index(evict)] = page

    return page_faults


# clock algorithm
def clock(pages, capacity):
    memory = [None] * capacity
    bits = [0] * capacity
    hand = 0
    page_faults = 0

    for page in pages:
        if page in memory:
            # marking it as recently used
            bits[memory.index(page)] = 1
            continue

        # sweeping
        page_faults += 1
        flag = True
        while flag:
            if bits[hand] == 0:
                # eviction
                memory[hand] = page
                bits[hand] = 1
                # advance
                hand = (hand + 1) % capacity
                flag = False
            else:
                # second chance
                bits[hand] = 0
                hand = (hand + 1) % capacity

    return page_faults


def lru_with_tracking(pages, capacity):
    frames = []
    page_faults = 0

    for i, page in enumerate(pages):
        fault = False
        if page not in frames:
            fault = True
            page_faults += 1
            if len(frames) == capacity:
                frames.pop(0)
            frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)

        state = str(frames)
        flag = "FAULT" if fault else "hit"
        print(f"{i+1:<5} {page:<5} {state:<20} {flag}")

    print(f"\nTotal LRU page faults: {page_faults}")
    return page_faults


# Random page reference string (same seed for reproducibility)
random.seed(42)
pages = [random.randint(1, 10) for _ in range(20)]
#locality_pages = [random.randint(1, 4) for _ in range(20)]
locality_pages = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
# Working set fits in frames: LRU and Clock should outperform FIFO
workload_pages = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 4, 5, 1, 2, 3, 1, 2, 3, 4, 1]
capacity = 3


data = [pages, locality_pages, workload_pages]

task = 1
for d in data:
    # Display the results
    print(f"Task {task}")
    print(f"Page reference string: {d}")
    print(f"FIFO page faults: {fifo(d, capacity)}")
    print(f"LRU page faults: {lru(d, capacity)}")
    print(f"RAND page faults: {rand_algo(d, capacity)}")
    print(f"OPT page faults: {opt(d, capacity)}")
    print(f"Clock page faults: {clock(d, capacity)}\n")
    task += 1


print("Task 4: LRU frame size sweep")
print(f"Page reference string: {workload_pages}")
print(f"{'Frames':<10} {'Page Faults'}")
print("-" * 22)
for capacity in range(2, 6):
    faults = lru(workload_pages, capacity)
    print(f"{capacity:<10} {faults}")


print("\nTask 5: LRU step-by-step state")
print(f"Page reference string: {pages}")
print(f"Frames: {capacity}\n")
print(f"{'Step':<5} {'Page':<5} {'Frames':<20} {'Fault?'}")
print("-" * 40)

lru_with_tracking(pages, capacity)


#===================================================================== 
# Task 1
#===================================================================== 

# RESULTS (capacity=3):
#
# Random string [1-4 range]:
#   FIFO=8, LRU=9, RAND=8
#   LRU performs WORSE than FIFO here. Small page pool + random order means
#   LRU's recency heuristic misfires, evicting pages that return quickly.
#
# Hand-crafted locality string [1,2,3,1,2,3,...,4]:
#   FIFO=14, LRU=14, RAND=8
#   Working set size (4 pages) exceeds capacity (3 memory) by exactly 1.
#   FIFO and LRU both thrash predictably. RAND avoids the pattern by chance.
#   Demonstrates that deterministic algorithms can be gamed by adversarial strings.
#
# Conclusion: LRU is not universally better. Its advantage appears on workloads
# with genuine temporal locality, not on adversarial or tight-working-set patterns.


#===================================================================== 
# Task 2
#===================================================================== 

# RESULTS (seed=42, capacity=3):
#
# Random string: FIFO=15, LRU=15, RAND=15, OPT=11
#   No temporal locality. All three algorithms perform equally poorly.
#   OPT still reduces faults significantly via future knowledge alone.
#
# Locality string: FIFO=14, LRU=14, RAND=8, OPT=7
#   Working set (4 pages) exceeds frame count (3) by 1, causing thrashing.
#   FIFO and LRU get trapped in a deterministic eviction loop.
#   RAND avoids the pattern by chance, approaching OPT.
#   OPT achieves near-minimum by always evicting page 4 (least future use).
#
# Conclusion: LRU's advantage only emerges with genuine temporal locality
# and a working set that fits within available memory.


#===================================================================== 
# Task 3
#===================================================================== 

# Workload string (hot set {1,2,3} fits in 3 frames, cold spikes {4,5}):
# FIFO=10, LRU=9, RAND=9, Clock=10, OPT=7
#
# LRU outperforms FIFO: recency tracking correctly keeps the hot set loaded
# and evicts cold pages (4, 5) when they spike in.
# FIFO evicts the oldest page regardless, sometimes kicking out a hot page.
# Clock ties with FIFO on this short string, needs more cold spikes to
# accumulate enough bit sweeps to differentiate from FIFO.
# OPT achieves minimum faults with perfect future knowledge.
#
# Conclusion: LRU's advantage is visible when a stable working set exists
# and frame count matches the hot set size exactly.


#===================================================================== 
# Task 4
#===================================================================== 
#
# RESULTS:
# Frames=2 -> 20 faults  (hot set size 3 doesn't fit; constant thrashing)
# Frames=3 -> 9 faults   (hot set fits exactly; dramatic improvement)
# Frames=4 -> 8 faults   (one extra slot absorbs a cold spike)
# Frames=5 -> 5 faults   (only compulsory faults remain; first-time loads)
#
# The 2->3 jump is the most significant: once frames match the working set
# size, faults drop sharply. This demonstrates why knowing your workload's
# working set size matters for memory allocation decisions.
# LRU satisfies the stack property, faults never increase with more frames.


#===================================================================== 
# Task 5
#===================================================================== 
# Step  Page  Frames               Fault?
# ----------------------------------------
# 1     2     [2]                  FAULT
# 2     1     [2, 1]               FAULT
# 3     5     [2, 1, 5]            FAULT
# 4     4     [2, 1, 5, 4]         FAULT
# 5     4     [2, 1, 5, 4]         hit
# 6     3     [2, 1, 5, 4, 3]      FAULT
# 7     2     [1, 5, 4, 3, 2]      hit
# 8     9     [5, 4, 3, 2, 9]      FAULT
# 9     2     [5, 4, 3, 9, 2]      hit
# 10    10    [4, 3, 9, 2, 10]     FAULT
# 11    7     [3, 9, 2, 10, 7]     FAULT
# 12    1     [9, 2, 10, 7, 1]     FAULT
# 13    1     [9, 2, 10, 7, 1]     hit
# 14    2     [9, 10, 7, 1, 2]     hit
# 15    4     [10, 7, 1, 2, 4]     FAULT
# 16    4     [10, 7, 1, 2, 4]     hit
# 17    9     [7, 1, 2, 4, 9]      FAULT
# 18    10    [1, 2, 4, 9, 10]     FAULT
# 19    1     [2, 4, 9, 10, 1]     hit
# 20    9     [2, 4, 10, 1, 9]     hit
# 
# Total LRU page faults: 12
