import requests
response=requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1")
data=response.json()
for i in data:
    print(i["name"])
