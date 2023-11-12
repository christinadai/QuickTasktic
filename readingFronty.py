
import operator
from collections import deque
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
from openai_tester import processAI
from googleMaps import get_coordinates
from api import route_travel_times
from api import street_parking

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



#time conversion
def timetodec(timestr):
    a = timestr.split(":")
    hours, min = a[0],a[1]
    dectime = int(hours) + int(min)/60.0
    return dectime

@app.route('/process', methods=['POST'])
@cross_origin()
def process():
    #print("hello") # ignore, test print
    data1 = request.get_data()  # data is byte encoded
    #print(data)
    data_str1 = data1.decode('utf-8')  #decode byte data into string
    #print(data_str)
    data_dict1 = json.loads(data_str1) #change string into a dictionary
    #print(data_dict1[0])
    #print(data_dict1[1])
    #print(data_dict1[2])
    #print(data_dict1[3])
    #print(data_dict1[4])

    

    #print(data_dict1[0]["errand1"])

    timeDepart = 11
    curLoc = [37.76441, -122.438156]
    #destination = [37.76441, 122.438156]

    name1 = data_dict1[0]["errand1"]
    qq = data_dict1[0]["tsTime1"]
    timesen1 = timetodec(qq)
    specLoc1 = data_dict1[0]["specLoc1"]
    #print (name1)
    #print(get_coordinates(y))
    #print(name1)
    #print(curLoc[0])
    #print(curLoc[1])
    cords1 = get_coordinates(name1, curLoc[0], curLoc[1])
    cordsx1 = float(cords1[0])
    cordsy1 = float(cords1[1])
    #print(cords1[0])
    #print(cords1[1])
    timespent1 = processAI(name1)
    travel_time1 = route_travel_times(curLoc[0], curLoc[1], cordsx1, cordsy1)
    #print(travel_time1)
    parking_availability1 = street_parking(cordsx1, cordsy1, 1000)  #time_sent2 

    dict1 = {
        'task_name': name1,
        'time_spent': timespent1,
        'time_sensitivity': timesen1,
        'given_location': specLoc1,
        #'current_location': current_location,
        'parking_availability': parking_availability1,
        'travel_time': travel_time1,
        'total_parking_score': parking_score(parking_availability1, travel_time1)
    }



    name2 = data_dict1[1]["errand2"]
    xx = data_dict1[1]["tsTime2"]
    timesen2 = timetodec(xx)
    specLoc2 = data_dict1[1]["specLoc2"]
    #print (name2)
    cords2 = get_coordinates(name2, curLoc[0], curLoc[1])
    timespent2 = processAI(name2)
    cordsx2 = float(cords2[0])
    cordsy2 = float(cords2[1])
    #print (cordsx2)
    #print (cordsy2)

    travel_time2 = route_travel_times(curLoc[0], curLoc[1], cordsx2, cordsy2)
    parking_availability2 = street_parking(cordsx2, cordsy2, 1000)
    #if (travel_time2 == None):
    #    travel_time2 = 1

    dict2 = {
        'task_name': name2,
        'time_spent': timespent2,
        'time_sensitivity': timesen2,
        #'time_sensitivity': time_sensitivity if timesen2 else None,
        'given_location': specLoc2,
        #'current_location': current_location,
        'parking_availability': parking_availability2,
        'travel_time': travel_time2,
        'total_parking_score': parking_score(parking_availability2, travel_time2)
    }

    print(dict1)
    print(dict2)

    '''
    name3 = data_dict1[2]["errand3"]
    print (name3)
    #print(get_coordinates(y))
    cords3 = get_coordinates(name3)
    print(cords3[0])
    print(cords3[1])
    processAI(name3)
    '''


    #print(lot_parking(cordx, cords[1]))
    
    #route_travel_times(cordx, cords[1], 37.349200, -121.938562)

    





    name4 = data_dict1[3]["errand4"]
    rr = data_dict1[3]["tsTime4"]
    if rr.find(":") != -1:
        timesen4 = timetodec(rr)
    else:
        timesen4 = rr
    specLoc4 = data_dict1[3]["specLoc4"]
    #print (name2)
    cords4 = get_coordinates(name4, curLoc[0], curLoc[1])
    timespent4 = processAI(name4)
    cordsx4 = float(cords4[0])
    cordsy4 = float(cords4[1])


    #print(data_dict1[3]["errand4"])


    #x = str(data_dict1[4]["errand5"])
    #print(processAI(x))

    #for i in range(5):
     #   first_value = list(data_dict1[1]())[0]
      #  print(first_value)
    bigArray = [dict1, dict2]

    sortBigArray = sort_tasks(bigArray)



    return(sortBigArray)
    
    

'''
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
'''

#print(process)

    
def parking_score(parking_percent, travel_time_mins):
    return (0.3 * parking_percent) +( 0.7 * int(travel_time_mins))

def print_tasks(array):
    print("Hi! Thank you for choosing QuickTaskTic! Here is your schedule for the day: ")
    total_time = 0
    for i in array:
        print(f"{i['task_name']} will take you {i['travel_time']} minutes to drive there and {i['time_spent']} minutes to complete.")
        total_time = total_time + i['task_name'] + i['time_spent']

    total_hours = total_time / 60
    total_minutes = total_time % 60

    print(f"It will take you {total_hours} hours and {total_minutes} minutes to complete all of your tasks! Thank you for choosing QuickTaskTic!")

# algorithm that gives the order of tasks based on availability
# parameters: array of tasks (dictionaries)
def sort_tasks(arr):
    # assumed start time is 12:00 am
    current_time = 00.00

    # create (1) reg_task- array of non-priority tasks (2) priority_queue- array of priority tasks (sorted by time)
    non_pri = deque()
    pri = deque()
    for i in arr:
        if(i["time_sensitivity"]):
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
            current_time = current_time + float(popped_val["time_spent"])
            #print(current_time)
        elif(len(pri) == 0):
            popped_val = non_pri.pop()
            #print(popped_val)
            ordered_tasks.append(popped_val)
            current_time = current_time + float(popped_val["time_spent"])
            #print(current_time)
        elif(float(non_pri[0]["time_spent"]) + current_time > pri[0]["time_sensitivity"]):
            popped_val = pri.pop()
            #print(popped_val)
            ordered_tasks.append(popped_val)
            current_time = current_time + float(popped_val["time_spent"])
            #print(current_time)
        else:
            popped_val = non_pri.pop()
            #print(popped_val)
            ordered_tasks.append(popped_val)
            current_time = current_time + float(popped_val["time_spent"])
            #print(current_time)
        

    return ordered_tasks

# test code for the function:
    
#task1 = task_dict("Task1", 3.5, False, 0, "N/A", "N/A", 0.8, 4)
#task2 = task_dict("Task2", 6.5, False, 0, "N/A", "N/A", 1.0, 1)
#task3 = task_dict("Task3", 7.0, False, 0, "N/A", "N/A", 0.08, 3)
#task4 = task_dict("Task4", 0.25, True, 17.00, "N/A", "N/A", 0.05, 23)
#task5 = task_dict("Task5", 0.05, False, 0, "N/A", "N/A", 0.9, 4)
#task6 = task_dict("Task6", 1.00, True, 15.00, "N/A", "N/A", 0.2, 1)
#task7 = task_dict("Task7", 0.02, False, 0, "N/A", "N/A", 0.4, 1)
    
#array = [task1, task2, task3, task4, task5, task6, task7]



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
