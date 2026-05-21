import random

# Memory block representation
class MemoryBlock:
    def __init__(self, start, size):
        self.start = start
        self.size = size

    def __repr__(self):
        return f"Block(start={self.start}, size={self.size})"

# Allocation Algorithms
class MemoryAllocator:
    def __init__(self, size):
        self.memory = [MemoryBlock(0, size)] # initially one big free block

    def allocate(self, request_size, strategy='first_fit'):
        index = self._find_index(request_size, strategy)
        if index is None:
            raise MemoryError(f"Request size of {request_size} could not be allocated (out of memory)")

        block = self.memory.pop(index)
        allocated = MemoryBlock(block.start, request_size)
        remaining_size = block.size - request_size

        if remaining_size > 0:
            remaining = MemoryBlock(block.start + request_size, remaining_size)
            self.memory.insert(index, remaining)

        return allocated

    def deallocate(self, block):
        self.memory.append(block)
        self.memory.sort(key=lambda b: b.start)

        merged = []
        for b in self.memory:
            if not merged:
                merged.append(b)
            else:
                last = merged[-1]
                # If current block starts exactly where last one ends, merge
                if last.start + last.size == b.start:
                    last.size += b.size
                else:
                    merged.append(b)
        self.memory = merged


    def fragmentation_stats(self):
        if not self.memory:
            return {
                "free_blocks": 0,
                "total_free": 0,
                "largest_free_block": 0,
                "external_fragmentation": 0,
            }

        free_blocks = len(self.memory)
        sizes = [b.size for b in self.memory]
        total_free = sum(sizes)
        largest_free_block = max(sizes)
        external_fragmentation = total_free - largest_free_block

        return {
            "free_blocks": free_blocks,
            "total_free": total_free,
            "largest_free_block": largest_free_block,
            "external_fragmentation": external_fragmentation,
        }

    def _find_index(self, size, strategy):
        candidates = [(i, b.size) for i, b in enumerate(self.memory) if b.size >= size]

        if not candidates:
            return None

        if strategy == 'first_fit':
            return candidates[0][0]
        elif strategy == 'best_fit':
            return min(candidates, key=lambda x: x[1])[0]
        elif strategy == 'worst_fit':
            return max(candidates, key=lambda x: x[1])[0]

    def show_memory(self):
        print("Free memory blocks:", self.memory)


    def visualize(self, total_size, resolution=1):
        # everything filled with "#"
        cells = ['#'] * (total_size // resolution)

        # free regions as '.'
        for b in self.memory:
            start = b.start // resolution
            end = (b.start + b.size) // resolution
            for i in range(start, end):
                if 0 <= i < len(cells):
                    cells[i] = '.'

        print("Memory map:")
        print("".join(cells))

# Example usage
if __name__ == "__main__":
    strategies = ['first_fit', 'best_fit', 'worst_fit']
    #requests = [20, 15, 10, 30, 25]
    #requests = [10, 10, 10, 10, 50, 5]
    #requests = [33, 33, 20]
    requests = [12, 7, 25, 3, 18, 10]

    for strategy in strategies:
        print(f"\nStrategy: {strategy}")
        allocator = MemoryAllocator(60) # modifications
        allocations = []
        for r in requests:
            try:
                block = allocator.allocate(r, strategy)
                allocations.append(block)
                print(f"Allocated: {block}")
            except MemoryError as e:
                print("MemoryError: ", e)
                allocations.append(None)

        print("Deallocating some blocks to create fragmentation...")
        allocator.deallocate(allocations[1])
        allocator.deallocate(allocations[2])

        allocator.show_memory()
        stats = allocator.fragmentation_stats()
        print("Fragmentation stats: ", stats)
        allocator.visualize(60)

# Task 1
"""
A)
Original output of the task. All strategies behave same.

❯ python memory_allocation.py

Strategy: first_fit
Allocated: Block(start=0, size=20)
Allocated: Block(start=20, size=15)
Allocated: Block(start=35, size=10)
Allocated: Block(start=45, size=30)
Allocated: Block(start=75, size=25)
Free memory blocks: []

Strategy: best_fit
Free memory blocks: []

Strategy: worst_fit
Allocated: Block(start=0, size=20)
Allocated: Block(start=20, size=15)
Allocated: Block(start=35, size=10)
Allocated: Block(start=45, size=30)
Allocated: Block(start=75, size=25)
Free memory blocks: []

===================================
B)
Modified total memory size changed from 100 to 60.

As shown below, request of size 30 adn 25 couldn't be allocated
due to not enough initial memory.

❯ python memory_allocation.py

Strategy: first_fit
...
Request of size 30 could not be allocated.
Allocated: None
Request of size 25 could not be allocated.
Allocated: None
Free memory blocks: [Block(start=45, size=15)]

Strategy: best_fit
...
Request of size 30 could not be allocated.
Allocated: None
Request of size 25 could not be allocated.
Allocated: None
Free memory blocks: [Block(start=45, size=15)]

Strategy: worst_fit
...
Request of size 30 could not be allocated.
Allocated: None
Request of size 25 could not be allocated.
Allocated: None
Free memory blocks: [Block(start=45, size=15)]

===============================
C)
Script was run with initial memory of 100, with requests:
requests = [10, 10, 10, 10, 50, 5].

All strategies still behave the same, but it's much more clear
how the size shifts the initial address of the next request.

Strategy: first_fit
Allocated: Block(start=0, size=10)
Allocated: Block(start=10, size=10)
Allocated: Block(start=20, size=10)
Allocated: Block(start=30, size=10)
Allocated: Block(start=40, size=50)
Allocated: Block(start=90, size=5)
Free memory blocks: [Block(start=95, size=5)]

Strategy: best_fit
Allocated: Block(start=0, size=10)
Allocated: Block(start=10, size=10)
Allocated: Block(start=20, size=10)
Allocated: Block(start=30, size=10)
Allocated: Block(start=40, size=50)
Allocated: Block(start=90, size=5)
Free memory blocks: [Block(start=95, size=5)]

Strategy: worst_fit
Allocated: Block(start=0, size=10)
Allocated: Block(start=10, size=10)
Allocated: Block(start=20, size=10)
Allocated: Block(start=30, size=10)
Allocated: Block(start=40, size=50)
Allocated: Block(start=90, size=5)
Free memory blocks: [Block(start=95, size=5)]

"""

# Task 2
"""
For this task I added a simple deallocator that returns freed blocks to the free list.
This creates multiple separate free regions (holes), which illustrates external fragmentation.

Strategy: first_fit
Allocated: Block(start=0, size=20)
Allocated: Block(start=20, size=15)
Allocated: Block(start=35, size=10)
Allocated: Block(start=45, size=30)
Allocated: Block(start=75, size=25)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=20, size=15), Block(start=45, size=30)]

Strategy: best_fit
Allocated: Block(start=0, size=20)
Allocated: Block(start=20, size=15)
Allocated: Block(start=35, size=10)
Allocated: Block(start=45, size=30)
Allocated: Block(start=75, size=25)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=20, size=15), Block(start=45, size=30)]

Strategy: worst_fit
Allocated: Block(start=0, size=20)
Allocated: Block(start=20, size=15)
Allocated: Block(start=35, size=10)
Allocated: Block(start=45, size=30)
Allocated: Block(start=75, size=25)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=20, size=15), Block(start=45, size=30)]
"""

# Task 3
"""
I changed the requests to [12, 7, 25, 3, 18, 10] to better reflect variable process sizes
For this sequence and total memory 60, all three strategies still produce the
same allocations, because at each step there is only one free block large enough,
so the choice of strategy does not matter.

❯ python memory_allocation.py

Strategy: first_fit
Allocated: Block(start=0, size=12)
Allocated: Block(start=12, size=7)
Allocated: Block(start=19, size=25)
Allocated: Block(start=44, size=3)
Request of size 18 could not be allocated.
Allocated: None
Allocated: Block(start=47, size=10)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=57, size=3)]

Strategy: best_fit
Allocated: Block(start=0, size=12)
Allocated: Block(start=12, size=7)
Allocated: Block(start=19, size=25)
Allocated: Block(start=44, size=3)
Request of size 18 could not be allocated.
Allocated: None
Allocated: Block(start=47, size=10)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=57, size=3)]

Strategy: worst_fit
Allocated: Block(start=0, size=12)
Allocated: Block(start=12, size=7)
Allocated: Block(start=19, size=25)
Allocated: Block(start=44, size=3)
Request of size 18 could not be allocated.
Allocated: None
Allocated: Block(start=47, size=10)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=57, size=3)]
"""

# Task 4

"""
Using requests = [12, 7, 25, 3, 18, 10] and total memory 60.

We have 35 bytes of free memory, but the largest contiguous free block is only 25 bytes.
The remaining 10 bytes are split across two smaller holes, so they contribute to external fragmentation.

Strategy: best_fit
Allocated: Block(start=0, size=12)
Allocated: Block(start=12, size=7)
Allocated: Block(start=19, size=25)
Allocated: Block(start=44, size=3)
Request of size 18 could not be allocated.
Allocated: None
Allocated: Block(start=47, size=10)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=12, size=7), Block(start=19, size=25), Block(start=57, size=3)]
Fragmentation stats:  {'free_blocks': 3, 'total_free': 35, 'largest_free_block': 25, 'external_fragmentation': 10}
"""

# Task 5-6
"""
❯ python memory_allocation.py

Strategy: first_fit
Allocated: Block(start=0, size=12)
Allocated: Block(start=12, size=7)
Allocated: Block(start=19, size=25)
Allocated: Block(start=44, size=3)
MemoryError:  Request size of 18 could not be allocated (out of memory)
Allocated: Block(start=47, size=10)
Deallocating some block to create fragmentation...
Free memory blocks: [Block(start=12, size=32), Block(start=57, size=3)]
Fragmentation stats:  {'free_blocks': 2, 'total_free': 35, 'largest_free_block': 32, 'external_fragmentation': 3}
"""

# Task 7
"""
❯ python memory_allocation.py

Strategy: first_fit
Allocated: Block(start=0, size=12)
Allocated: Block(start=12, size=7)
Allocated: Block(start=19, size=25)
Allocated: Block(start=44, size=3)
MemoryError:  Request size of 18 could not be allocated (out of memory)
Allocated: Block(start=47, size=10)
Deallocating some blocks to create fragmentation...
Free memory blocks: [Block(start=12, size=32), Block(start=57, size=3)]
Fragmentation stats:  {'free_blocks': 2, 'total_free': 35, 'largest_free_block': 32, 'external_fragmentation': 3}
Memory map:
############................................#############...
"""
