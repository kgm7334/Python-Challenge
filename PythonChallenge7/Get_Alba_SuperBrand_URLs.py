import requests
from bs4 import BeautifulSoup


def GetSuperBrand(AlbaURL):
    print("startGetSuperBrand")
    SuperBrand_URLs = []

    Result = requests.get(AlbaURL)

    Alba_Soup = BeautifulSoup(Result.text, "html.parser")
    MainSuperBrand_div = Alba_Soup.find("div", {"id": "MainSuperBrand"})
    # soup.find_all(attrs={'class':'card-title'})
    li_impact = MainSuperBrand_div.find_all(attrs={'class': 'impact'})

    for a in li_impact:
        url = a.find("a")["href"]+"job/brand/?page=1&pagesize=50000"
        SuperBrand_URLs.append(
            {'URL': url, 'FileName': a.find("strong").text})

    # for str in SuperBrand_URLs:
        # print(str['FileName']+str['URL']+"\n")

    #strr = len(SuperBrand_URLs)
    # print(strr)
    return SuperBrand_URLs
