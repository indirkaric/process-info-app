from concurrent.futures import process
import psutil

def get_list_of_process_sorted_by_memory_usage():
    processes = []
    
    for process in psutil.process_iter():
       try:
        
           process_info = process.as_dict(attrs = ['pid', 'name', 'username', 'cpu_percent'])
           process_info['virtual-memory-space'] = process.memory_info().vms / (1024 * 1024)
           
           processes.append(process_info);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    
    processes = sorted(processes, key = lambda procObj: procObj['virtual-memory-space'], reverse = True)
    return processes

def print_processes():
    processes = get_list_of_process_sorted_by_memory_usage()
    
    for process in processes:
        print(process)

    print("*" *130)

    print("Top 5 processes with with high virtual memory space\n")
    for process in processes[:5] :
        print(process)

print_processes()

   



