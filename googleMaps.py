import requests

def get_coordinates():
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=grocery&location=37.349200%2C-121.938562&radius=1500&fields=formatted_address,name,geometry&key=AIzaSyBlP3GItzc6nLlcHHQPMldzK3Jjsg-Gjdo"

    payload = {}
    headers = {
    'key': '&key=AIzaSyBlP3GItzc6nLlcHHQPMldzK3Jjsg-Gjdo',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6ImV4aGJsajl4NDciLCJ0b2tlbiI6eyJpdiI6IjE5MDUwNWJlZDI4OWViMjlkYmUxZWE3ZjIwM2QyMDYyIiwiY29udGVudCI6ImU0NTA2NTUzY2JiNzZhZDA1YTUwYzlkYWQ5YTZmZWI3ZmU5MzI2ZjRmMDQ0Yjk3MzQ4ZDkyZDA3YWRkOTA1YmJhZmZiNDg0YjZiZWFiNjdiOGRmYTlkOTRjMDJjZTJiMTY2OGM0MDU2OWI5NGFjNzEwZDkwZGE3N2VlNzVkMGE0MDg1YTgwZDc2NWFhMzE2ZjVmOTEyN2UwMzRkZGNiMjc2ZjMzOTkxZTk5MGVhNTcwY2FlYjZjMzFiYjVjZjZhMWYwMTUxMTI0YzI2Zjc0YWFmYzM5N2ZiZDRlNjJlZjRhM2M3YzY1ZWYxOTM5MzM0ZGQxMzFhYWQ4ZmM4NzJiODY1ZThmYTgyMzhmMGZlZTk0N2QwNTIzMTE5NzZmYmM2NTBkOTAwNWMyMzE1YWZhMzdmNDNjNjljYjVhYWJjYjIyMDVmYjEwNjJhMDQ4MjY4MGY5ODljMDhkMDhkYjQxMjc5Njg0MWMzODFmZTBkMzM4NWIwOTQyYmY5NmUwNzBkNWMxOGVhZmU5NWE0ZTU0MGY5NGQzMzM3ODA1NTdjMTQ0ZDljYTNiZTUzNTUzNDViODEyNDVkMGZlMmU1YzFmMTliMzI2NTE4NzM4OTIzYzUxZDA1MjE4NzhiNGQzNjRjMmU5ZWI0MWQ1NjYwMjdjN2U3YTNiZjU1MmQ5YzExNzA3ODZjNDM5ZmE1N2JmM2M2YmZmMmM3ODM1OTZjY2JjY2JiMzgzZjI1MWE2ZmZkMWExNzY0ZDY0MjdmMWMwM2MzZTdkOTI3NjRlNGFlNjdhNmRkNTk2ODE4Y2I4OTE3OGZiZmViY2ZkZDcxNTcwMWQwMmQ0NzIyMjllOGEzNDQ2MTY4YTYyNGM0NmE4ODU4ODRiYjU1MDZkIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiIxOTA1MDViZWQyODllYjI5ZGJlMWVhN2YyMDNkMjA2MiIsImNvbnRlbnQiOiJkMzUzN2U0MWQ4YzU1YjhlNTM3ZWI0ZTRlODg2ZTZkNWZjYmY1ZmUxOGI2NmJmNzE0YWM5MTA3NmEyYzczYmNlYTg4ZTQzMDAwM2RhYmU0MWI3ZTNiNmFhIn0sImp0aSI6ImY0ZjViYjYyLTA1ZjItNDkxNy05NmM3LTA2NGYxN2M1MWIxMSIsImlhdCI6MTY5OTc0MTU5MiwiZXhwIjoxNjk5NzQ1MTkyfQ.1ALoiCw6LqBkaS9AaP_5RvIxHy7DL55S5ct-sS7Ms6Q'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    first_location = response.json()["results"][0]["geometry"]["location"]
    lat = first_location["lat"]
    long = first_location["lng"]
    return(lat, long)

    #print(f"{lat}, {long}")

    #print(get_coordinates())








#old code
#import http.client
#from backend import Task
'''
x = "shoestore"
y = 37.349200
z = -121.938562
radius = 150

conn = http.client.HTTPSConnection("maps.googleapis.com")
payload = ''
headers = {}
conn.request("GET", "/maps/api/place/nearbysearch/json?keyword=shoestore&location=37.349200%252C-121.938562&radius=2000&fields=formatted_address,name,geometry&key=AIzaSyBlP3GItzc6nLlcHHQPMldzK3Jjsg-Gjdo", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
'''
"""
import http.client
import certifi
conn = http.client.HTTPSConnection("maps.googleapis.com")
payload = ''
headers = {}
conn.request("GET", "/maps/api/place/nearbysearch/json?keyword=grocery&location=37.349200%252C-121.938562&radius=1500&fields=formatted_address,name,geometry&key=AIzaSyBlP3GItzc6nLlcHHQPMldzK3Jjsg-Gjdo", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
"""