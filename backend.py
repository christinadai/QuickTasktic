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

class Task:
    def __init__(task_name, time_sensitive=False, ts_time=-1.0, specific_location=False):
        task_name.time_sensitive = time_sensitive
        task_name.ts_time = ts_time
        task_name.specific_location = specific_location

#time conversion 
Def timetodec(timestr):
	try:
		hrs, min = map( int, timestr.split(‘:’)
		Dectime =(hrs+min)/60.0
		Return dectime
	except value error:
		print(“Invalid time!”)

#rank 

def sort_rank(rank):
    count = len(rank)
    for i in range(count):
        for j in range(0, count - i - 1):
            if rank[j] < rank[j + 1]:
                temp = rank[j]
                rank[j] = rank[j + 1]
                rank[j + 1] = temp

    return rank
