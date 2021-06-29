import os
import requests
from bs4 import BeautifulSoup


def CountryParse():
    url = "https://www.iban.com/currency-codes"
    CountryList = []

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
        print("Welcome to CurrencyConvert PRO 2000")
        for idx, CountryInfo in enumerate(CountryList):
            print("# "+str(idx)+" "+CountryInfo['Country'])

    except:
        print("URL Connect Fail OR scraping Fail")
    return CountryList
