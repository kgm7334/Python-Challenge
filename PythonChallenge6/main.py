from CountryParser import CountryParse
from UserInputControl import UserSelectCountry
from ConvertParser import ConvertParse

CountryList = CountryParse()
UserSelectResultDic = UserSelectCountry(CountryList)
ConvertParse(UserSelectResultDic)
