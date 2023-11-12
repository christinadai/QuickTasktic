
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
    #timeDepart = 11
    curLoc = [37.76441, -122.438156]
    #destination = [37.76441, 122.438156]

    name1 = data_dict1[0]["errand1"]
    qq = data_dict1[0]["tsTime1"]
    if qq.find(":") != -1:
        timesen1 = timetodec(qq)
    else:
        timesen1 = qq
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
    if xx.find(":") != -1:
        timesen2 = timetodec(xx)
    else:
        timesen2 = xx
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

    name3 = data_dict1[2]["errand3"]
    oo = data_dict1[2]["tsTime3"]
    if oo.find(":") != -1:
        timesen3 = timetodec(oo)
    else:
        timesen3 = oo
    specLoc3 = data_dict1[2]["specLoc3"]
    #print (name2)
    cords3 = get_coordinates(name3, curLoc[0], curLoc[1])
    timespent3 = processAI(name3)
    cordsx3 = float(cords3[0])
    cordsy3 = float(cords3[1])
    #print (cordsx2)
    #print (cordsy2)

    travel_time3 = route_travel_times(curLoc[0], curLoc[1], cordsx3, cordsy3)
    parking_availability3 = street_parking(cordsx3, cordsy3, 1000)
    #if (travel_time2 == None):
    #    travel_time2 = 1

    dict3 = {
        'task_name': name3,
        'time_spent': timespent3,
        'time_sensitivity': timesen3,
        #'time_sensitivity': time_sensitivity if timesen2 else None,
        'given_location': specLoc3,
        #'current_location': current_location,
        'parking_availability': parking_availability3,
        'travel_time': travel_time3,
        'total_parking_score': parking_score(parking_availability3, travel_time3)
    }

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


    travel_time4 = route_travel_times(curLoc[0], curLoc[1], cordsx4, cordsy4)
    parking_availability4 = street_parking(cordsx4, cordsy4, 1000)
    #if (travel_time2 == None):
    #    travel_time2 = 1

    dict4 = {
        'task_name': name4,
        'time_spent': timespent4,
        'time_sensitivity': timesen4,
        #'time_sensitivity': time_sensitivity if timesen2 else None,
        'given_location': specLoc4,
        #'current_location': current_location,
        'parking_availability': parking_availability4,
        'travel_time': travel_time4,
        'total_parking_score': parking_score(parking_availability4, travel_time4)
    }

    #print(dict1)
    #print(dict2)
    #print(dict3)
    #print(dict4)

    bigArray = [dict1, dict2, dict3, dict4]
    sortBigArray = sort_tasks(bigArray)

    print_tasks(sortBigArray)

    return(sortBigArray)
    
    
def parking_score(parking_percent, travel_time_mins):
    if ( travel_time_mins == None):
        travel_time_mins ==1
    return (0.3 * parking_percent) +( 0.7 * int(travel_time_mins))

def print_tasks(array):
    print("Hi! Thank you for choosing QuickTaskTic! Here is your schedule for the day: ")
    for i in array:
        print(f"{i['task_name']} will take you {i['travel_time']} minutes to drive there and {i['time_spent']} minutes to complete, you will be done at .")

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
    ordered_tasks[i]
    return ordered_tasks

if __name__ == '__main__':
    app.run()
