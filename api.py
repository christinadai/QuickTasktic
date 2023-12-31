

import requests
import json
import xml.etree.ElementTree as ET
import xmltodict
#from googleMaps import get_coordinates # Google maps API

# AUTHENTICATION
def get_uas():
  url = "https://api.iq.inrix.com/auth/v1/appToken?appId=exhblj9x47&hashToken=ZXhoYmxqOXg0N3xwdjBNa3NEdkg1NmxOSXl6Z3dVd2QzWXlEelpheE5wOTZIMlYwS2dY"
  payload = {}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)

  return (response.json()["result"]["token"])

# INRIX API 1 : gets route ID for route_travel_times
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


# INRIX API 2: Gives fastest travel time given two locations (lat, long) format
def route_travel_times(lat_1, long_1, lat_2, long_2, count = 3, time_interval = 45):
  auth = get_uas()

  route_id = find_route(lat_1, long_1, lat_2, long_2)
  #print(route_id)

  url = f"https://api.iq.inrix.com/routeTravelTimes?routeId={route_id}&travelTimeCount={count}&travelTimeInterval={time_interval}"

  payload = {}
  headers = {
  'Authorization': f'Bearer {auth}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  #Convert XML/Text file (response) to JSON/dictionary (json_data)

  xml_dict = xmltodict.parse(response.text)
  #print(xml_dict)

  # Use get to get info
  travel_time = xml_dict.get('Inrix', {}).get("Trip", {}).get("Route", {}).get("TravelTimes", {}).get("TravelTime", [{}])[0].get("@travelTimeMinutes")

  return travel_time

# print(route_travel_times(37.770581, -122.44255, 37.765297, -122.442527))
#print(route_travel_times(37.349, -121.939, 37.765297, -122.442527))

# INRIX API 3: gives probability of getting lot parking as a percent within a 150 meter radius 
def lot_parking(lat, long):
  auth = get_uas()
  url = f"https://api.iq.inrix.com/lots/v3?point={lat}%7C{long}&radius=150"

  payload = {}
  headers = {
  'Authorization': f'Bearer {auth}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  #print("this is from the parking thing")
  #print(response.text)
  #return(response.text)
  return response.json()
  


# INRIX API 4: gives probability of getting street parking as a percent within 0.5 mile radius 
def street_parking(lat, long, rad = 1000):
  auth = get_uas()

  url = f"https://api.iq.inrix.com/blocks/v3?point={lat}%7C{long}&radius=1000"
  #print(url)

  payload = {}
  headers = {
  'Authorization': f'Bearer {auth}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  probability = response.json()["result"][0]["probability"]
  if (probability == None):
    probability = 10
  #print(probability)
  return (probability)

# print(street_parking(37.770581, -122.44255))

# print(route_travel_times(37.770581, -122.44255, 37.765297, -122.442527))


"""
#testing:
#street_parking(37.74304518280319, 122.42438793182373, 50)

#find_route(37.770581, -122.442550, 37.765297, -122.442527)
#print(get_uas())
"""






'''
import requests
import json
import xml.etree.ElementTree as ET
import xmltodict
from googleMaps import get_coordinates # Google maps API

# AUTHENTICATION
def get_uas():

    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=exhblj9x47&hashToken=ZXhoYmxqOXg0N3xwdjBNa3NEdkg1NmxOSXl6Z3dVd2QzWXlEelpheE5wOTZIMlYwS2dY"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return (response.json()["result"]["token"])

# INRIX API 1 : gets route ID for route_travel_times
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


# INRIX API 2: Gives fastest travel time given two locations (lat, long) format
def route_travel_times(lat_1, long_1, lat_2, long_2, count = 3, time_interval = 45):
    auth = get_uas()
    
    route_id = find_route(lat_1, long_1, lat_2, long_2)

    url = f"https://api.iq.inrix.com/routeTravelTimes?routeId={route_id}&travelTimeCount={count}&travelTimeInterval={time_interval}"

    payload = {}
    headers = {
    'Authorization': f'Bearer {auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    #Convert XML/Text file (response) to JSON/dictionary (json_data)

    xml_dict = xmltodict.parse(response.text)
    #print(xml_dict)
    
    # Use get to get info
    travel_time = xml_dict.get('Inrix', {}).get("Trip", {}).get("Route", {}).get("TravelTimes", {}).get("TravelTime", [{}])[0].get("@travelTimeMinutes")

    return travel_time

# INRIX API 3: gives probability of getting lot parking as a percent within a 150 meter radius 
def lot_parking(lat, long):
    auth = get_uas()
    url = "https://api.iq.inrix.com/lots/v3?point={lat}%7C{long}&radius=150"

    payload = {}
    headers = {
      'Authorization': f'Bearer {auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return response.json()


# INRIX API 4: gives probability of getting street parking as a percent within 0.5 mile radius 
def street_parking(lat, long, rad = 800):
    auth = get_uas()

    url = f"https://api.iq.inrix.com/blocks/v3?point={lat}%7C{long}&radius=200"

    payload = {}
    headers = {
      'Authorization': f'Bearer {auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    probability = response.json["result"]["probability"]
    print(probability)
    #return (response.json())

print(route_travel_times(37.770582, -122.44255, 37.765600, -122.442527))

"""
#testing:
#street_parking(37.74304518280319, 122.42438793182373, 50)
#route_travel_times(15, 45, 37.770581, -122.442550, 37.765297, -122.442527, "2023-12-12T01:23:00Z")
#find_route(37.770581, -122.442550, 37.765297, -122.442527)
#print(get_uas())
"""
'''