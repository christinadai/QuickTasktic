import requests
import json
import xml.etree.ElementTree as ET

def get_uas():

    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=exhblj9x47&hashToken=ZXhoYmxqOXg0N3xwdjBNa3NEdkg1NmxOSXl6Z3dVd2QzWXlEelpheE5wOTZIMlYwS2dY"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return (response.json()["result"]["token"])

def find_route(lat_1, long_1, lat_2, long_2):
    auth = get_uas()

    url = f"https://api.iq.inrix.com/findRoute?wp_1={lat_1}%2C{long_1}&wp_2={lat_2}%2C{long_2}&format=json"

    payload = {}
    headers = {
      'Authorization': f'Bearer {auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return (response.json()["routes"]["id"])


def route_travel_times(count, time_interval, lat_1, long_1, lat_2, long_2):
    auth = get_uas()
    route_id = find_route(lat_1, long_1, lat_2, long_2)

    url = f"https://api.iq.inrix.com/routeTravelTimes?routeId={route_id}&travelTimeCount={count}&travelTimeInterval={time_interval}"

    payload = {}
    headers = {
    'Authorization': f'Bearer {auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # Parse the XML response
    root = ET.fromstring(response)
    #Access the specific elements that we need
    
    
    return 
    

    #return response.json()



route_travel_times(15, 45, 37.352100, -121.936780, 37.356930, -121.936630)
