import random_proc_gen

# implementation from https://www.geeksforgeeks.org/dsa/shortest-remaining-time-first-preemptive-sjf-scheduling-algorithm/
class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def srtf(processes):
    current_time, completed = 0, 0
    while completed < len(processes):
        idx = -1
        for i, p in enumerate(processes):
            if p.arrival_time <= current_time and p.remaining_time > 0 and (idx == -1 or p.remaining_time < processes[idx].remaining_time):
                idx = i
        if idx != -1:
            processes[idx].remaining_time -= 1
            current_time += 1
            if processes[idx].remaining_time == 0:
                processes[idx].completion_time = current_time
                processes[idx].turnaround_time = current_time - processes[idx].arrival_time
                processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
                completed += 1
        else:
            current_time += 1

def print_results(processes):
    total_wt, total_tat = 0, 0
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
        print(f"Process{p.id}: Waiting time = {p.waiting_time} Completion time = {p.completion_time} Turnaround time: {p.turnaround_time}")
    print(f"Average Waiting Time: {(total_wt / len(processes)):.2f}")
    print(f"Average Turnaround Time: {(total_tat / len(processes)):.2f}")

procs = random_proc_gen.random_proc()
processes = [Process(proc[0], proc[1], proc[2]) for proc in procs]
srtf(processes)
print_results(processes)
