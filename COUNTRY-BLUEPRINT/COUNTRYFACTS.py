from countryinfo import CountryInfo
import csv
def country ():
    print("_"*100)
    print("COUNTRY INFO WINDOW")
    print("_"*100)
    while True:
        A=input("Enter the country to get info= ")
        country=CountryInfo(A)
        print("___________________________________________")
        print("Details of the country :", A)
        print("___________________________________________")
        print("Continent=", country.region())
        print("Subregion=", country.subregion())
        print("Longitude and latitude=", country.latlng())
        print("Capital =", country.capital())
        print("Currencies=", country.currencies())
        print("Area=", country.area())
        print("Population=", country.population())
        print("Timezone=", country.timezones())
        print("International Calling code=", country.calling_codes())
        print("Native name=", country.native_name())
        print("Others names= ", country.alt_spellings())
        print("Language= ", country.languages())
        print("Residents=", country.demonym())
        print("Top level domain=", country.tld())
        print("Provinces=")
        A=country.provinces()
        for i in A:
            print ( "\t\t", i)
        print()
        print("More info got to=", country.wiki())
        ch1=input("wish to continue(Y/N)=")
        if ch1 in "Nn":
            Menu()

def countryandcapitals():
    print("_" * 100)
    print("COUNTRY AND CAPITAL")
    print("_" * 100)
    L=[]
    F1=open("COUNTRIESANDCAPITAL.csv", 'r', newline="")
    csvobj=csv.reader(F1)
    print("SNO","\t","COUNTRIES","\t", "CAPITAL")
    for i in csvobj:
        L.append(i)
    A=len(L)
    print("SNO","|","Name", "|\t\t\t", "Capital")
    for i in range(0, A):
        print(i,"|", L[i][0],"|", L[i][1])
    print("press enter to proceed to the Menu")


def countrycamp():
    print("_" * 100)
    print("COUNTRY COMPARE WINDOW")
    print("_" * 100)
    while True:
        A = input("Enter the 1st country= ")
        B=input("Enter the 2nd country=")
        country = CountryInfo(A)
        A1=country.region()
        A2= country.subregion()
        A3=country.capital()
        A4=country.currencies()
        A5=country.area()
        A6= country.population()
        A7=country.timezones()
        A8=country.calling_codes()
        A9=country.native_name()
        A10=country.alt_spellings()
        A11=country.demonym()
        A12=country.languages()
        A13=country.wiki()
        A14=country.latlng()
        A15=country.tld()
        country = CountryInfo(B)
        B1 = country.region()
        B2 = country.subregion()
        B3 = country.capital()
        B4 = country.currencies()
        B5 = country.area()
        B6 = country.population()
        B7 = country.timezones()
        B8 = country.calling_codes()
        B9 = country.native_name()
        B10 = country.alt_spellings()
        B11 = country.demonym()
        B12 = country.languages()
        B13=country.wiki()
        B14=country.latlng()
        B15=country.tld()
        print('_'*100)
        print("COUNTRIES=\t",A, '\t||\t', B)
        print("CONTINENT=\t",A1,'\t||\t', B1)
        print("SUBREGION=\t",A2, '\t||\t', B2)
        print("CAPITAL=\t",A3, '\t||\t', B3)
        print("CURRENCY=\t",A4,'\t||\t', B4)
        print("AREA=\t",A5,'\t||\t', B5)
        print("POPULATION=\t",A6,'\t||\t', B6)
        print("LONGITUDE AND LATITUDE=\t", A14,"\t||\t","\t", B14)
        print("TIME ZONE=\t",A7,'\t||\t', B7)
        print()
        print("INTERNATIONAL TELEPHONE CODE=\t",A8,'\t||\t', B8)
        print("NATIVE NAME=\t",A9,'\t||\t', B9)
        print("OTHER NAMS=\t",A10,'\t||\t', B10)
        print()
        print("RESIDENTS=\t",A11,'\t||\t', B11)
        print("LANGUAGES=\t", A12,"\t||\t", B12)
        print("TOP LEVEL DOMAIN=", A15, "\t||\t", B15)
        print("MORE INFO=\t", A13, "\t||\t", B13)
        ch1 = input("wish to continue(Y/N)=")
        if ch1 in "Nn":
            Menu()
def Menu():
    while True:
        print("\t\t\tMenu")
        print("press 1 for country info")
        print("press 2 for comparison between two countrries")
        print("press 3 for countries and capitals")
        print("press 4 to exit")
        ch=int(input("Enter the choice= "))
        if ch==1:
            country()
        elif ch==2:
            countrycamp()
        elif ch==3:
            countryandcapitals()
        elif ch==4:
            break
        else:
            print("Invalid choice")

Menu()


