
def UserSelectCountry(CountryList):

    FromCountryCode = FromInputNumber(CountryList)
    print("\n")
    ToCountryCode = ToInputNumber(CountryList)
    print("\n")
    Amount = InputAmount(FromCountryCode, ToCountryCode)

    ResultList = {'From': FromCountryCode,
                  'To': ToCountryCode, 'Amount': Amount}
    return ResultList


def FromInputNumber(CountryList):
    print("Where are you from choose a country by number \n")
    while True:
        try:
            Input = (int(input("#: ")))

            if(Input < len(CountryList)):
                print(CountryList[Input]['Country'])
                break
            else:
                print("Choose a number from the list")

        except:
            print("That wasn't a number")
            Input = 30000
    return CountryList[Input]['Code']


def ToInputNumber(CountryList):
    print("Now choose another country.\n")
    while True:
        try:
            Input = (int(input("#: ")))

            if(Input < len(CountryList)):
                print(CountryList[Input]['Country'])
                break
            else:
                print("Choose a number from the list")

        except:
            print("That wasn't a number")
            Input = 30000
    return CountryList[Input]['Code']


def InputAmount(FromCountryCode, ToCountryCode):
    print(
        f"How many {FromCountryCode} do you want to convert to {ToCountryCode}? .\n")
    while True:
        try:
            Input = (int(input("#: ")))
            break
        except:
            print("That wasn't a number")
    return Input
