def fcfs(processes):
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    
    print("Process ID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    
    for process in processes:
        if process['arrival_time'] > completion_time:
            completion_time = process['arrival_time']
        completion_time += process['burst_time']
        process['completion_time'] = completion_time
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        process['waiting_time'] = process['turnaround_time'] - process['burst_time']
        total_turnaround_time += process['turnaround_time']
        total_waiting_time += process['waiting_time']
        
        print(f"{process['id']}\t\t{process['arrival_time']}\t\t{process['burst_time']}\t\t{process['completion_time']}\t\t{process['turnaround_time']}\t\t{process['waiting_time']}")
    
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_waiting_time = total_waiting_time / len(processes)
    
    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")

# Take input for number of processes
num_processes = int(input("Enter the number of processes: "))

# Initialize an empty list to store processes
processes = []

# Take input for each process
for i in range(num_processes):
    process_id = i + 1
    arrival_time = int(input(f"Enter arrival time for process {process_id}: "))
    burst_time = int(input(f"Enter burst time for process {process_id}: "))
    processes.append({'id': process_id, 'arrival_time': arrival_time, 'burst_time': burst_time})

# Call the fcfs function with the processes
fcfs(processes)
