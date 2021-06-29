import os
import requests
from bs4 import BeautifulSoup

# os.system("clear")
url = "https://www.iban.com/currency-codes"
CountryList = []
CountryDict = {}

try:
    Result = requests.get(url)
    Country_Soup = BeautifulSoup(Result.text, "html.parser")
    Country_Infos = Country_Soup.find_all("tbody")
    for Country_tbody in Country_Infos:
        for Country_tr in Country_tbody.find_all("tr"):
            for idx, Country_td in enumerate(Country_tr.find_all("td")):
                #print(idx, Country_td)
                if(idx == 0):
                    Country = Country_td.string.capitalize()
                elif(idx == 1):
                    Currency = Country_td.string
                elif(idx == 2):
                    Code = Country_td.string
                elif(idx == 3):
                    Number = Country_td.string
            CountryList.append(
                {'Country': Country, 'Currency': Currency, 'Code': Code, 'Number': Number})
    print("Hello! Please Choose select a country by number:")
    for idx, CountryInfo in enumerate(CountryList):
        print("# "+str(idx)+" "+CountryInfo['Country'])
    while True:
        try:
            UserInput = (int(input("#: ")))

            if(UserInput < len(CountryList)):
                print("You chose "+CountryList[UserInput]['Country'])
                print("The currency code is "+CountryList[UserInput]['Code'])
                break
            else:
                print("Choose a number from the list")

        except:
            print("That wasn't a number")
            UserInput = 30000


except:
    print("URL Connect Fail OR scraping Fail")
