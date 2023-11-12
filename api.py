import requests
import json
import xml.etree.ElementTree as ET
import xmltodict

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

    id = response.json().get('result', {}).get('trip', {}).get('routes', [{}])[0].get('id')
    
    return (id)


#Defauly departure time given in case not provided by user
def route_travel_times(count, time_interval, lat_1, long_1, lat_2, long_2, dep_time = "2023-11-12T01:23:00Z"):
    auth = get_uas()
    route_id = find_route(lat_1, long_1, lat_2, long_2)

    url = f"https://api.iq.inrix.com/routeTravelTimes?routeId={route_id}&departureTime={dep_time}&travelTimeCount={count}&travelTimeInterval={time_interval}"

    payload = {}
    headers = {
    'Authorization': f'Bearer {auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    #Convert XML/Text file (response) to JSON (json_data)

    xml_dict = xmltodict.parse(response.text)

    # Convert the Python dictionary to string
    str_data = json.dumps(xml_dict, indent=2)  # indent for pretty printing

    #Convert data from string to json
    parsed_json = json.loads(str_data)

    # Use get to get info
    travel_time = parsed_json.get('Inrix', {}).get("Trip", {}).get("Route", {}).get("TravelTimes", {}).get("TravelTime", [{}])[0].get("@travelTimeMinutes")
    
    return travel_time

#Half a mile radius, maximum 10 minute walk
def street_parking(lat, long, rad = 800):
    auth = get_uas()

    url = f"https://api.iq.inrix.com/blocks/v3?point={lat}%7C-{long}&radius={rad}"

    payload = {}
    headers = {
      'Authorization': f'Bearer {auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return (response.json())




"""
#testing:
#street_parking(37.74304518280319, 122.42438793182373, 50)
#route_travel_times(15, 45, 37.770581, -122.442550, 37.765297, -122.442527, "2023-11-12T01:23:00Z")
#find_route(37.770581, -122.442550, 37.765297, -122.442527)
#print(get_uas())
"""