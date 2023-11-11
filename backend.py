# FUNCTIONS
#time conversion
def timetodec(timestr):
	try:
		hrs, min = map(int, timestr.split(':'))
		dectime =(hrs+min)/60.0
		return dectime
	except ValueError:
		print('Invalid time!')
		
# return most time-sensitive task
def find_min_ts_task(task_array):
    time_sensitive_tasks = [task for task in task_array if task.time_sensitive]

    if time_sensitive_tasks:
        min_ts_task = min(time_sensitive_tasks, key=lambda task: task.ts_time)
        return min_ts_task
    else:
        return None
    
#sortandrank
def calculate_rank(park_rank, travel_time):
    count = len(park_rank)
    rank = [0]*count
    for i in range(count):
        rank[i] = (0.3 * park_rank[i]) + (0.7 * travel_time[i])
    return rank

def sort_rank(rank):
    count = len(rank)
    for i in range(count):
        for j in range(0, count - i - 1):
            if rank[j] < rank[j + 1]:
                temp = rank[j]
                rank[j] = rank[j + 1]
                rank[j + 1] = temp

    return rank	

#variables
num_of_tasks = 0 
tasks = []       # An empty list to store task objects
departure_time_string = ''
departure_time = timetodec(departure_time_string) 
curr_time = departure_time 
curr_coordinate_x = 0.0 
curr_coordinate_y = 0.0 
starting_coordinate_x = 37.3491386955373 
starting_coordinate_y = -121.9367374882497 
num_of_time_sen_event = 0

class Task:
    def __init__(task_name, time_sensitive=False, ts_time_string='100:00', specific_location=False, specific_coordX = 0.0, specific_coordY = 0.0):
        task_name.time_sensitive = time_sensitive
        task_name.ts_time_string = ts_time_string
        task_name.ts_time = ts_time
        task_name.specific_location = specific_location
        task_name.specific_coordX = specific_coordX
        task_name.specific_coordY = specific_coordY

ts_time = 0.0
ts_time = timetodec(ts_time)

