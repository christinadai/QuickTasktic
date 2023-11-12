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



import http.client

conn = http.client.HTTPSConnection("maps.googleapis.com")
payload = ''
headers = {}

conn.request("GET", "/maps/api/place/nearbysearch/json?keyword=grocery&location=37.349200%252C-121.938562&radius=1500&fields=formatted_address,name,geometry&key=AIzaSyBlP3GItzc6nLlcHHQPMldzK3Jjsg-Gjdo", payload, headers)
res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))