from collections import deque
import random_proc_gen

def round_robin(processes, quantum):
	"""
	Round Robin Scheduling Algorithm
	:param processes: List of tuples (pid, arrival_time, burst_time)
	:param quantum: Time quantum for scheduling
	"""
	queue = deque(sorted(processes, key=lambda x: x[1])) # Sort by arrival time
	time = 0
	wait_times = {}
	turnaround_times = {}
	remaining_burst = {pid: burst for pid, _, burst in processes}
	while queue:
		pid, arrival, _ = queue.popleft()
		if time < arrival:
			time = arrival # Move time forward if CPU is idle
		execute_time = min(remaining_burst[pid], quantum)
		remaining_burst[pid] -= execute_time
		time += execute_time
		if remaining_burst[pid] == 0:
			wait_times[pid] = time - arrival - remaining_burst[pid] # Total wait time
			turnaround_times[pid] = time - arrival # Total turnaround time
			print(f"Process {pid}: Waiting Time = {wait_times[pid]}, Turnaround Time = {turnaround_times[pid]}")
		else:
			queue.append((pid, arrival, remaining_burst[pid])) # Re-add if burst remains
	avg_wait = sum(wait_times.values())/len(wait_times)
	avg_turnaround = sum(turnaround_times.values()) / len(turnaround_times)
	print(f"Average Waiting Time: {avg_wait:.2f}")
	print(f"Average Turnaround Time: {avg_turnaround:.2f}")

# Example Usage
proc = random_proc_gen.random_proc()
flag = True
quant = 2
while flag:
    try:
        quant = int(input("Enter quantum n: "))
        flag = False
    except ValueError:
        print("Must enter integer")
round_robin(proc, quantum=quant)
