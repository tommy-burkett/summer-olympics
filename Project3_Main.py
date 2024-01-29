from Project3_Functions import *

# Function 1
# insert 3 letter country code, ALL, or empty string into code
code = input('Enter a three letter country code: ')
print('Total Medals ' + '(' + code + '):')
for key, val in totalMedalsByCountry(code).items():
    print(key + ':', val) 
print('\n')


# Function 2
# insert a sport and a minimum medal earned
sport = input('Enter a Summer Olympics sport: ')
medal = input('Enter a minimum medal of your choice: ')
countriesWithMedal = (countriesWithMedalInSport(sport, medal))
with open('countries.csv', 'r', encoding='utf-8') as file:
    text = file.readlines()
    countryList = []
    for countries in countriesWithMedal:
        for word in text:
            countryName = word.split(',')[COUNTRY_IDX]
            countryCode = word.split(',')[CODE_IDX]
            if countries == countryCode:
                countryList.append(countryName)

# state all medals listed in output
if medal == 'Bronze':
    medals = 'Bronze or Silver or Gold'
if medal == 'Silver':
    medals = 'Silver or Gold'
if medal == 'Gold':
    medals = 'Gold'
# Print method format
print(sport + ' Winners ' + '(' + medals + '):')
for fullName in countryList:
    print(fullName)
print('\n')


# Function 3
country = input('Enter a three letter country code: ')
minYear = input('Enter a minimum Summer Olympic year: ')
maxYear = input('Enter a maximum Summer Olympic year: ')
tupleList = goldMedalsByCountryAndYears(country, minYear, maxYear)
with open('countries.csv', 'r', encoding='utf-8') as file:
    text = file.readlines()[REMOVE_FIRST_LINE_IDX:]
    for tuples in tupleList:
        for word in text:
            countryName = str(word.split(',')[COUNTRY_IDX])
            countryCode = word.split(',')[CODE_IDX]
            if country == countryCode:
                fullName = country.replace(country, countryName)
                years = '(' + str(minYear) + '-' + str(maxYear) + '):'

print(fullName + ' Gold Medals ' + years)
for name, year, discipline, event, gender in tupleList:
     print(year + ': ' + gender + "'s " + discipline + ', ' + event + ':: ' + name)
