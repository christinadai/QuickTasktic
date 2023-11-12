# FUNCTIONS
#time conversion
def timetodec(timestr):
  
    a = timestr.split(":")
    hours, min = a[0],a[1]
    dectime = int(hours) + int(min)/60.0
    return dectime
		
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
departure_time_string = '12:10'

departure_time = timetodec(departure_time_string) 
curr_time = departure_time 
curr_coordinate_x = 0.0 
curr_coordinate_y = 0.0 
starting_coordinate_x = 37.3491386955373 
starting_coordinate_y = -121.9367374882497 
num_of_time_sen_event = 0

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

def create_task_dict(task_name, time_sensitive, time_sensitivity, given_location, current_location, parking_availability, total_parking_score):
    task_dict = {
        'task_name': task_name,
        'time_sensitive': time_sensitive,
        'time_sensitivity': time_sensitivity if time_sensitive else None,
        'given_location': given_location,
        'current_location': current_location,
        'parking_availability': parking_availability,
        'total_parking_score': total_parking_score
    }
    return task_dict

# Example usage:
task_name = "Complete Project"
time_sensitive = True
time_sensitivity = 3  # Assuming time sensitivity is an integer
given_location = "Office"
current_location = {'x': 10, 'y': 20}
parking_availability = "High"
total_parking_score = 9.5 


task_info = create_task_dict(task_name, time_sensitive, time_sensitivity, given_location, current_location, parking_availability, total_parking_score)

# Print the created dictionary
print(task_info)
    def __init__(self, task_name, time_sensitive=False, ts_time_string='100:00', specific_location=False, specific_coordX=0.0, specific_coordY=0.0):
        self.task_name = task_name
        self.time_sensitive = time_sensitive
        self.ts_time_string = ts_time_string
        self.specific_location = specific_location
        self.specific_coordX = specific_coordX
        self.specific_coordY = specific_coordY

ts_time = "10:02"
ts_time = timetodec(ts_time)

