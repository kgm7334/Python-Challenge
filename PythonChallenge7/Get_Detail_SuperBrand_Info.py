import requests
from bs4 import BeautifulSoup
import csv
import re


def SaveCSV(SuperBrandDetailInfo, FileName):
    FileName = re.sub('[\/:*?"<>|]', '', FileName)
    #FileName = ''.join(char for char in FileName if char.isalnum())
    file = open(f"{FileName}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in SuperBrandDetailInfo:
        try:
            writer.writerow(list(job.values()))
        except:
            continue
    return


def GetDetailInfo(SuperBrand_URLs):
    print("startGetDetailInfo")
    SuperBrandDetailInfo = []

    for url in SuperBrand_URLs:
        Result = requests.get(url['URL'])
        DetailInfo_Soup = BeautifulSoup(Result.text, "html.parser")
        tbody = DetailInfo_Soup.find("tbody")
        if(tbody == None):
            continue
        tr = tbody.find_all('tr', {'class': ""})
        if(tr == None):
            continue

        for info in tr:
            try:
                place = info.find("td", {"class": "local"}).text
                place = place.replace('\xa0', ' ')
            except:
                place = "ExceptPlace"
            try:
                title = info.find("span", {"class": "title"}).text
            except:
                title = "ExceptTitle"
            try:
                time = info.find("span", {"class": "time"}).text
            except:
                time = "ExceptTime"
            try:
                pay = info.find("span", {"class": "payIcon"}).text + \
                    info.find("span", {"class": "number"}).text
            except:
                pay = "ExceptPay"
            try:
                date = info.find("strong").text
            except:
                date = "ExceptDate"
            SuperBrandDetailInfo.append(
                {'Place': place, 'Title': title, 'Time': time, 'Pay': pay, 'Date': date})

        SaveCSV(SuperBrandDetailInfo, url['FileName'])
