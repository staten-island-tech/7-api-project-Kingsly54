import requests

def km():
    response = requests.get("https://strangerthingsquotes.shadowdev.xyz/api/quotes")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    corrcounter=0
    for i in range(len(data)):
        answer=data[i]["author"]
        print(data[i]["quote"])
        ask=input("Who said this quote?")
        if ask==data[i]["author"]:
            corrcounter+=1  
            print("You got it correct!")
            print(f"You have gotten {corrcounter} correct in a row!")
        else:
            corrcounter=0
            print(f"You got it wrong, the correct answer was {answer}")
km()