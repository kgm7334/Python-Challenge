import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


def ConvertParse(UserSelectResultDic):
    url = f"https://wise.com/gb/currency-converter/{UserSelectResultDic['From']}-to-{UserSelectResultDic['To']}-rate?amount={UserSelectResultDic['Amount']}"

    try:
        Result = requests.get(url)
        Convert_Soup = BeautifulSoup(Result.text, "html.parser")
        Convert_Infos = Convert_Soup.find(
            "span", {"class": "text-success"}).text

        print(format_currency(float(UserSelectResultDic['Amount']), UserSelectResultDic['From'], locale="ko_KR")
              + " is " + format_currency((float(Convert_Infos)*float(UserSelectResultDic['Amount'])), UserSelectResultDic['To'], locale="ko_KR"))
    except:
        print("URL Connect Fail OR scraping Fail OR Not Exist CurrencyCode")
