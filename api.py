import requests
import json

url = "https://api.iq.inrix.com/auth/v1/appToken?appId=exhblj9x47&hashToken=ZXhoYmxqOXg0N3xwdjBNa3NEdkg1NmxOSXl6Z3dVd2QzWXlEelpheE5wOTZIMlYwS2dY"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()["result"]["token"])


"""

def get_uas_token(api_url, app_id, app_key, hash_token):
    

    headers = {
        'User-Agent': user_agent,  # Replace with your User-Agent string
        'Authorization': f'App {app_id}:{app_key}',
        'Hash-Token': hash_token,
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        response_json = response.json()

        # Assuming the API returns the User-Agent token in the response
        uas_token = response_json.get('result', {}).get('token')  # Adjusted this based on the actual response structure

        return uas_token
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
# Example usage:
api_url = 'https://api.iq.inrix.com/auth/v1/appToken?appId=exhblj9x47&hashToken=ZXhoYmxqOXg0N3xwdjBNa3NEdkg1NmxOSXl6Z3dVd2QzWXlEelpheE5wOTZIMlYwS2dY/routeTravelTimes'
app_id = 'exhblj9x47'
app_key = 'pv0MksDvH56lNIyzgwUwd3YyDzZaxNp96H2V0KgX'
hash_token = 'ZXhoYmxqOXg0N3xwdjBNa3NEdkg1NmxOSXl6Z3dVd2QzWXlEelpheE5wOTZIMlYwS2dY'

token = get_uas_token(api_url, app_id, app_key, hash_token)

if token:
    print(f"User-Agent Token: {token}")
else:
    print("Failed to get User-Agent Token.")
"""
