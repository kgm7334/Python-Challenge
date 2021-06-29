import os
import requests

while True:
    print("Welcome to  IsitDown.py")
    print("Please Write URL Or URLs You Want To Check. (Seperated comma)")

    User_Input_URL = input("").replace(" ", "").lower()
    if(User_Input_URL == ""):
        continue
    else:
        if((".com" in User_Input_URL) and ("," in User_Input_URL)):
            URLs = User_Input_URL.split(",")
            for URL in URLs:
                if(".com" in URL):
                    if("http" in URL):
                        try:
                            r = requests.get(URL)
                            if(r.status_code == requests.codes.ok):
                                print(URL+" is up!")
                            if(r.status_code == 404):
                                print(URL+" is down!")
                        except:
                            print(URL+" is down!")
                            continue
                    else:
                        try:
                            r = requests.get("http://"+URL)
                            if(r.status_code == requests.codes.ok):
                                print("http://"+URL+" is up!")
                            if(r.status_code == 404):
                                print("http://"+URL+" is down!")
                        except:
                            print("http://"+URL+" is down!")
                            continue

            while True:
                Excute = input(
                    "Do You Want to start over? y/n: ").strip().lower()
                if(Excute == "y" or Excute == "n"):
                    break
                else:
                    print("Thats Not avalid answer")
                    continue
        else:
            print(User_Input_URL+" is not a valid URL")
            while True:
                Excute = input(
                    "Do You Want to start over? y/n: ").strip().lower()
                if(Excute == "y" or Excute == "n"):
                    break
                else:
                    print("Thats Not avalid answer")
                    continue

        if(Excute == "n"):
            break
