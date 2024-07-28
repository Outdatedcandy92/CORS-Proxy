import requests

url = "https://cors-proxy-gray.vercel.app/jsonplaceholder.typicode.com/todos/1"
headers = {
    "Origin": "your-origin.com",  # Replace with your actual origin
    "X-Requested-With": "XMLHttpRequest"
}
response = requests.get(url, headers=headers)
print(response.text)