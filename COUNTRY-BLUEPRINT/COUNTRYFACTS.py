from countryinfo import CountryInfo
import csv


def country():
    print("_" * 100)
    print("COUNTRY INFO WINDOW")
    print("_" * 100)
    while True:
        A = input("Enter the country to get info= ")
        country = CountryInfo(A)
        print("___________________________________________")
        print(f"Details of the country : {A}")
        print("___________________________________________")
        print(f"Continent= {country.region()}")
        print(f"Subregion= {country.subregion()}")
        print(f"Longitude and latitude= {country.latlng()}")
        print(f"Capital= {country.capital()}")
        print(f"Currencies= {country.currencies()}")
        print(f"Area= {country.area()}")
        print(f"Population= {country.population()}")
        print(f"Timezone= {country.timezones()}")
        print(f"International Calling code= {country.calling_codes()}")
        print(f"Native name= {country.native_name()}")
        print(f"Others names= {country.alt_spellings()}")
        print(f"Language= {country.languages()}")
        print(f"Residents= {country.demonym()}")
        print(f"Top level domain= {country.tld()}")
        print("Provinces=")
        provinces = country.provinces()
        for i in provinces:
            print(f"\t\t{i}")
        print()
        print(f"More info go to= {country.wiki()}")
        ch1 = input("Wish to continue (Y/N)= ")
        if ch1.lower() == "n":
            break


def countryandcapitals():
    print("_" * 100)
    print("COUNTRY AND CAPITAL")
    print("_" * 100)
    with open("COUNTRIESANDCAPITAL.csv", 'r', newline="") as F1:
        csvobj = csv.reader(F1)
        L = list(csvobj)
    print("SNO", "\t", "COUNTRIES", "\t", "CAPITAL")
    for i, item in enumerate(L):
        print(i, "\t", item[0], "\t", item[1])
    input("Press enter to proceed to the Menu")


def countrycamp():
    print("_" * 100)
    print("COUNTRY COMPARE WINDOW")
    print("_" * 100)
    while True:
        A = input("Enter the 1st country= ")
        B = input("Enter the 2nd country= ")

        country1 = CountryInfo(A)
        A1, A2, A3 = country1.region(), country1.subregion(), country1.capital()
        A4, A5, A6 = country1.currencies(), country1.area(), country1.population()
        A7, A8, A9 = country1.timezones(), country1.calling_codes(), country1.native_name()
        A10, A11, A12 = country1.alt_spellings(), country1.demonym(), country1.languages()
        A13, A14, A15 = country1.wiki(), country1.latlng(), country1.tld()

        country2 = CountryInfo(B)
        B1, B2, B3 = country2.region(), country2.subregion(), country2.capital()
        B4, B5, B6 = country2.currencies(), country2.area(), country2.population()
        B7, B8, B9 = country2.timezones(), country2.calling_codes(), country2.native_name()
        B10, B11, B12 = country2.alt_spellings(), country2.demonym(), country2.languages()
        B13, B14, B15 = country2.wiki(), country2.latlng(), country2.tld()

        print('_' * 100)
        print(f"COUNTRIES= {A} \t||\t {B}")
        print(f"CONTINENT= {A1} \t||\t {B1}")
        print(f"SUBREGION= {A2} \t||\t {B2}")
        print(f"CAPITAL= {A3} \t||\t {B3}")
        print(f"CURRENCY= {A4} \t||\t {B4}")
        print(f"AREA= {A5} \t||\t {B5}")
        print(f"POPULATION= {A6} \t||\t {B6}")
        print(f"LONGITUDE AND LATITUDE= {A14} \t||\t {B14}")
        print(f"TIME ZONE= {A7} \t||\t {B7}")
        print()
        print(f"INTERNATIONAL TELEPHONE CODE= {A8} \t||\t {B8}")
        print(f"NATIVE NAME= {A9} \t||\t {B9}")
        print(f"OTHER NAMES= {A10} \t||\t {B10}")
        print()
        print(f"RESIDENTS= {A11} \t||\t {B11}")
        print(f"LANGUAGES= {A12} \t||\t {B12}")
        print(f"TOP LEVEL DOMAIN= {A15} \t||\t {B15}")
        print(f"MORE INFO= {A13} \t||\t {B13}")

        ch1 = input("Wish to continue (Y/N)= ")
        if ch1.lower() == "n":
            break


def Menu():
    while True:
        print("\t\t\tMenu")
        print("Press 1 for country info")
        print("Press 2 for comparison between two countries")
        print("Press 3 for countries and capitals")
        print("Press 4 to exit")
        ch = int(input("Enter the choice= "))
        if ch == 1:
            country()
        elif ch == 2:
            countrycamp()
        elif ch == 3:
            countryandcapitals()
        elif ch == 4:
            break
        else:
            print("Invalid choice")


Menu()
