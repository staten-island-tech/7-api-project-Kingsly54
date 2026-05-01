import requests

def km():
    response = requests.get("https://strangerthingsquotes.shadowdev.xyz/api/quotes")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    for i in len(data):
        print(data[i]["quote"])
km()