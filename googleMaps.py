from backend import Task

import http.client

conn = http.client.HTTPSConnection("maps.googleapis.com")
payload = ''
headers = {}
#
conn.request("GET", "/maps/api/place/nearbysearch/json?keyword="  "&location=37.349200%252C-121.938562&radius=200&fields=formatted_address,name,geometry&key=AIzaSyBlP3GItzc6nLlcHHQPMldzK3Jjsg-Gjdo%20", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))