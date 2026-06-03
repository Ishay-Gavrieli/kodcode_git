import requests

base_url = "http://localhost:8000"

responsed = requests.get(f"{base_url}/shapes")
print(responsed.status_code)
print(responsed.json())


responsed = requests.post(f"{base_url}/shapes")
print(responsed.status_code)
print(responsed.json())


responsed = requests.get(f"{base_url}/shapes/total-area")
print(responsed.status_code)
print(responsed.json())


responsed = requests.get(f"{base_url}/shapes/count")
print(responsed.status_code)
print(responsed.json())


responsed = requests.get(f"{base_url}/shapes/type/{type}")
print(responsed.status_code)
print(responsed.json())


responsed = requests.get(f"{base_url}/shapes/{id}")
print(responsed.status_code)
print(responsed.json())

responsed = requests.put(f"{base_url}/shapes/{id}")
print(responsed.status_code)
print(responsed.json())

responsed = requests.delete(f"{base_url}/shapes/{id}")
print(responsed.status_code)
print(responsed.json())