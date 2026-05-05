import requests
corrcounter=0
ccount=0
def play():
    response = requests.get("https://strangerthingsquotes.shadowdev.xyz/api/quotes")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    numplay=0
    for i in range(len(data)):
        answer=data[i]["author"]
        print(data[i]["quote"])
        ask=input("Who said this quote?")
        if ask==data[i]["author"]:
            ccount+=1
            corrcounter+=1
            print("You got it correct!")
            print(f"You have gotten {corrcounter} correct in a row!")
            print(f"You have gotten {ccount}/{gg} correct!")
            print(numplay)
        else:
            corrcounter=0
            print(numplay)
            print(f"You got it wrong, the correct answer was {answer}")
            print(f"You have gotten {ccount}/{gg} questions correct!")
gg=int(input("How many times would you like to play?"))
for i in range(gg):
    play()