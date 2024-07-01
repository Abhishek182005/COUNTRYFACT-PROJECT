from django.shortcuts import render, redirect
from countryinfo import CountryInfo
import csv
from django.http import HttpResponse

def menu(request):
    return render(request, 'Countryinfo_app/menu.html')

def country_info(request):
    if request.method == 'POST':
        country_name = request.POST.get('country')
        try:
            country = CountryInfo(country_name)
            context = {
                'name': country_name,
                'region': country.region(),
                'subregion': country.subregion(),
                'latlng': country.latlng(),
                'capital': country.capital(),
                'currencies': country.currencies(),
                'area': country.area(),
                'population': country.population(),
                'timezones': country.timezones(),
                'calling_codes': country.calling_codes(),
                'native_name': country.native_name(),
                'alt_spellings': country.alt_spellings(),
                'languages': country.languages(),
                'demonym': country.demonym(),
                'tld': country.tld(),
                'provinces': country.provinces(),
                'wiki': country.wiki()
            }
            return render(request, 'Countryinfo_app/country_info.html', context)
        except KeyError:
            return render(request, 'Countryinfo_app/error.html', {'error_message': 'Country not found or data unavailable.', 'retry_url': 'country_info'})
        except Exception as e:
            return render(request, 'Countryinfo_app/error.html', {'error_message': str(e), 'retry_url': 'country_info'})
    return render(request, 'Countryinfo_app/country_form.html')

def country_compare(request):
    if request.method == 'POST':
        country1_name = request.POST.get('country1').title()
        country2_name = request.POST.get('country2').title()
        try:
            country1 = CountryInfo(country1_name)
            country2 = CountryInfo(country2_name)
            
            context = {
                'country1': {
                    'name': country1_name,
                    'region': country1.region(),
                    'subregion': country1.subregion(),
                    'capital': country1.capital(),
                    'currencies': country1.currencies(),
                    'area': country1.area(),
                    'population': country1.population(),
                    'timezones': country1.timezones(),
                    'calling_codes': country1.calling_codes(),
                    'native_name': country1.native_name(),
                    'alt_spellings': country1.alt_spellings(),
                    'languages': country1.languages(),
                    'demonym': country1.demonym(),
                    'tld': country1.tld(),
                    'wiki': country1.wiki(),
                    'latlng': country1.latlng()
                },
                'country2': {
                    'name': country2_name,
                    'region': country2.region(),
                    'subregion': country2.subregion(),
                    'capital': country2.capital(),
                    'currencies': country2.currencies(),
                    'area': country2.area(),
                    'population': country2.population(),
                    'timezones': country2.timezones(),
                    'calling_codes': country2.calling_codes(),
                    'native_name': country2.native_name(),
                    'alt_spellings': country2.alt_spellings(),
                    'languages': country2.languages(),
                    'demonym': country2.demonym(),
                    'tld': country2.tld(),
                    'wiki': country2.wiki(),
                    'latlng': country2.latlng()
                }
            }
            return render(request, 'Countryinfo_app/country_compare.html', context)
        except KeyError:
            return render(request, 'Countryinfo_app/error.html', {'error_message': 'One or both countries not found or data unavailable.', 'retry_url': 'country_compare'})
        except Exception as e:
            return render(request, 'Countryinfo_app/error.html', {'error_message': str(e), 'retry_url': 'country_compare'})
    return render(request, 'Countryinfo_app/country_compare_form.html')



def error(request):
    return render(request, 'Countryinfo_app/error.html', {'error_message': 'An unexpected error occurred.'})

def country_and_capitals(request):
    try:
        countries_capitals = []
        with open("static/COUNTRIESANDCAPITAL1.csv") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                countries_capitals.append({
                    'country': row[0],
                    'capital': row[1],
                    'currency': row[2],
                    'continent': row[3]
                })
        context = {'countries_capitals': countries_capitals}
        return render(request, 'Countryinfo_app/countries_capitals.html', context)
    except FileNotFoundError:
        return render(request, 'Countryinfo_app/error.html', {'error_message': 'CSV file not found.'})
    except Exception as e:
        return render(request, 'Countryinfo_app/error.html', {'error_message': str(e)})

def landing_page(request):
    return render(request, 'Countryinfo_app/landing_page.html')
