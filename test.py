import requests
url = "https://cors-proxy-inky.vercel.app/hackhour.hackclub.com/api/history/U079HV9PTC7"
headers = {
    "Origin": "your-origin.com",  # Replace with your actual origin
    "X-Requested-With": "XMLHttpRequest",
    "Authorization": "Bearer 5ee2ee3e-b72f-41e2-a038-0c06ffec0cf2"  # Replace with your actual authorization token
}
response = requests.get(url, headers=headers)
print(response.text)