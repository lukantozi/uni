import random

def random_proc():
    random.seed(5)
    process_list = [(1, 0, 5), (2, 1, 3), (3, 2, 8)]
    for i in range (4, 22):
        wait_time = random.randint(0, 10)
        burst_time = random.randint(1, 20)
        process_list.append((i, wait_time, burst_time))
    return process_list

if __name__ == "__main__":
    print(random_proc())
