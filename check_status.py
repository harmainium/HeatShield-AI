import requests

api_key = input("Paste your FortyGuard API key: ")

activity_id = "b007004c-28bf-4b97-8d7a-744b06ab58b4"

url = f"https://api.fortyguard.com/v1/status/{activity_id}"

headers = {
    "api-key": api_key
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)