import requests

response = requests.get('https://api.nasa.gov/planetary/apod?api_key=dcxaWY8eIEjJtdOV2k8ukcUc6w4htdXUOb9alBCI')
if response.status_code == 200:
    data = response.json()
    print(data)
    print(data.get("url"))
