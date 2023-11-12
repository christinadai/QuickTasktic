
import operator
from collections import deque
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/process', methods=['POST'])
@cross_origin()
def process():
    #print("hello") # ignore, test print
    data1 = request.get_data()  # data is byte encoded
    #print(data)
    data_str1 = data1.decode('utf-8')  #decode byte data into string
    #print(data_str)
    data_dict1 = json.loads(data_str1) # change string into a dictionary
    print(data_dict1[0])
    #print("hello")
    print(data_dict1[1])
    print(data_dict1[2])
    print(data_dict1[3])
    print(data_dict1[4])
    return(data_dict1)
    


def task_dict(task_name, time_spent, time_sensitive, time_sensitivity, given_location, current_location, parking_availability, travel_time):
    task_dict = {
        'task_name': task_name,
        'time_spent': time_spent,
        'time_sensitive': time_sensitive,
        'time_sensitivity': time_sensitivity if time_sensitive else None,
        'given_location': given_location,
        'current_location': current_location,
        'parking_availability': parking_availability,
        'travel_time': travel_time,
        'total_parking_score': parking_score(parking_availability, travel_time)
    }
    return task_dict

#print(process)

    
def parking_score(parking_percent, travel_time_mins):
    return (0.3 * parking_percent) +( 0.7 * travel_time_mins)

# algorithm that gives the order of tasks based on availability
# parameters: array of tasks (dictionaries)
def sort_tasks(arr):
    # assumed start time is 12:00 am
    current_time = 00.00

    # create (1) reg_task- array of non-priority tasks (2) priority_queue- array of priority tasks (sorted by time)
    non_pri = deque()
    pri = deque()
    for i in arr:
        if(i["time_sensitive"]):
            pri.append(i)
        else:
            non_pri.append(i)
            

    # sort pri by timing, this will never change
    pri = deque(sorted(pri, key = operator.itemgetter('time_sensitivity')))
    

    # create output order of tasks, checking priority queue every time a new task from the 
    ordered_tasks = []
    for i in range(len(non_pri)+len(pri)):
        #sort the non_pri array by total_parking score (relative to the previous location, parking score will change)
        non_pri = deque(sorted(non_pri, key= operator.itemgetter('total_parking_score')))

        # compare first value of non_pri to priv
        if(len(non_pri) == 0):
            popped_val = pri.pop()
            #print(popped_val)
            ordered_tasks.append(popped_val)
            current_time = current_time + popped_val["time_spent"]
            #print(current_time)
        elif(len(pri) == 0):
            popped_val = non_pri.pop()
            #print(popped_val)
            ordered_tasks.append(popped_val)
            current_time = current_time + popped_val["time_spent"]
            #print(current_time)
        elif(non_pri[0]["time_spent"] + current_time > pri[0]["time_sensitivity"]):
            popped_val = pri.pop()
            #print(popped_val)
            ordered_tasks.append(popped_val)
            current_time = current_time + popped_val["time_spent"]
            #print(current_time)
        else:
            popped_val = non_pri.pop()
            #print(popped_val)
            ordered_tasks.append(popped_val)
            current_time = current_time + popped_val["time_spent"]
            #print(current_time)
        

    return ordered_tasks

# test code for the function:
    
task1 = task_dict("Task1", 3.5, False, 0, "N/A", "N/A", 0.8, 4)
task2 = task_dict("Task2", 6.5, False, 0, "N/A", "N/A", 1.0, 1)
task3 = task_dict("Task3", 7.0, False, 0, "N/A", "N/A", 0.08, 3)
task4 = task_dict("Task4", 0.25, True, 17.00, "N/A", "N/A", 0.05, 23)
task5 = task_dict("Task5", 0.05, False, 0, "N/A", "N/A", 0.9, 4)
task6 = task_dict("Task6", 1.00, True, 15.00, "N/A", "N/A", 0.2, 1)
task7 = task_dict("Task7", 0.02, False, 0, "N/A", "N/A", 0.4, 1)
    
array = [task1, task2, task3, task4, task5, task6, task7]

array = sort_tasks(array)

    # Process the data or perform any backend tasks
    # ...

    # Return a response back to the frontend
    # response = {
    #     "status": "success",
    #     "message": "Data received successfully!"
    # }
    # print(response.message)

    # response.headers.add('Access-Control-Allow-Origin', '*')

    # return jsonify(response)

if __name__ == '__main__':
    app.run()