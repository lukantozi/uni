import heapq
import random_proc_gen

def sjf(processes):
	processes.sort(key=lambda x: x[2]) # Sort by burst time
	current_time, total_wait, total_turnaround = 0, 0, 0
	for pid, arrival, burst in processes:
		if current_time < arrival:
			current_time = arrival
		wait_time = current_time - arrival
		total_wait += wait_time
		total_turnaround += wait_time + burst
		current_time += burst
		print(f"Process {pid}: Waiting Time = {wait_time}, Turnaaround Time = {wait_time + burst}")
	avg_wait=total_wait/len(processes)
	avg_turnaround=total_turnaround/len(processes)
	print(f"Average Waiting Time: {avg_wait:.2f}")
	print(f"Average Turnaround Time: {avg_turnaround:.2f}")
# Example usage
proc = random_proc_gen.random_proc()
sjf(proc)
