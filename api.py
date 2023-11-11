import requests

url = "https://api.iq.inrix.com/auth/v1/appToken?appId=exhblj9x47&hashToken=ZXhoYmxqOXg0N3xwdjBNa3NEdkg1NmxOSXl6Z3dVd2QzWXlEelpheE5wOTZIMlYwS2dY"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
