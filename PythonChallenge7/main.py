import os
import csv
import requests
from bs4 import BeautifulSoup
from Get_Alba_SuperBrand_URLs import GetSuperBrand
from Get_Detail_SuperBrand_Info import GetDetailInfo


alba_url = "http://www.alba.co.kr"


SuperBrand_URLs = GetSuperBrand(alba_url)
GetDetailInfo(SuperBrand_URLs)
