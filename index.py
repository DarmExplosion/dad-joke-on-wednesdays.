from time import sleep
import requests
import json
from datetime import datetime
import calendar
from datetime import date

url = "WEBHOOK URL" 

data = {
    "content" : "Sup",
    "username" : "Dad Joke Delivery!"
}

newhead = {
    "Accept" : "application/json"
}

while True:
    d = date.today()
    print('Date is:', d)
    z = calendar.day_name[d.weekday()]
    print('Weekday name is:', z)

    if z == "Friday":
        sleepytimer = 60
        print(datetime.now().weekday())
        x = requests.get("https://icanhazdadjoke.com/", headers = newhead)
        print(x.content)
        y = json.loads(x.content)
        print(y["joke"])
        data = {
            "content" : y["joke"],
            "username" : "Dad Joke Delivery!"
        }
        result = requests.post(url, json = data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))
    else:
        sleepytimer = 3600
    sleep(sleepytimer)
    
