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

#variables
num_of_tasks = 0 
tasks = []       # An empty list to store task objects
curr_time = 0.0  
departure_time = 0.0  
curr_coordinate_x = 0.0  
curr_coordinate_y = 0.0  
starting_coordinate_x = 37.3491386955373  
starting_coordinate_y = -121.9367374882497  
num_of_time_sen_event = 0

#time conversion 
Def timetodec(timestr):
	Try:
		hrs, min = map( int, timestr.split(‘:’)
		Dectime =(hrs+min)/60.0
		Return dectime
	Except value error:
		print(“Invalid time!”)

#rank 
Int park_rank=Call Park INRIX API;
	Int travel_time=Call Travel INRIX API;
	Int rank=(0.3*park_rank)+(0.7*travel_time);
	for(i=0; i< count; i++){
		if(rank[i] < rank[i+1])