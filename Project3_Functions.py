# Remove first line from text files
REMOVE_FIRST_LINE_IDX = 1

# Indexes from summer.csv
YEAR_IDX = 0
CITY_IDX = 1
SPORT_IDX = 2
DISCIPLINE_IDX = 3
ATHLETE_IDX = 4
COUNTRIES_IDX = 5
GENDER_IDX = 6
EVENT_IDX = 7
MEDAL_IDX = 8

# Indexes from countries.csv
COUNTRY_IDX = 0
CODE_IDX = 1

def totalMedalsByCountry(code='ALL'):
    Gold = 0
    Silver = 0
    Bronze = 0
    medalList = {'Gold': Gold, 'Silver': Silver, 'Bronze': Bronze}
    with open('summer.csv', 'r', encoding='utf-8') as file:
        text = file.readlines()[REMOVE_FIRST_LINE_IDX:]
        for word in text:
            countries = word.split(',')[COUNTRIES_IDX]
            medal = word.split(',')[MEDAL_IDX].strip()
            if code == countries:
                if medal == 'Gold':
                    medalList['Gold'] += 1
                elif medal == 'Silver':
                    medalList['Silver'] += 1
                elif medal == 'Bronze':
                    medalList['Bronze'] += 1
            elif code == 'ALL' or '':
                if medal == 'Gold':
                    medalList['Gold'] += 1
                if medal == 'Silver':
                    medalList['Silver'] += 1
                if medal == 'Bronze':
                    medalList['Bronze'] += 1
    
    return medalList


def countriesWithMedalInSport(sport, minMedal='Bronze'):
    listOfCountries = []
    with open('summer.csv', 'r', encoding='utf-8') as file:
        text = file.readlines()[1:]
    
        for word in text:
            countries = word.split(',')[COUNTRIES_IDX]
            medal = word.split(',')[MEDAL_IDX]
            sports = word.split(',')[SPORT_IDX]
            if sport == sports:
                if minMedal == 'Bronze' or minMedal == '' and medal == 'Bronze\n':
                    listOfCountries.append(countries)
                    listOfCountries = list(set(listOfCountries))
                if minMedal == 'Silver' and medal == 'Silver\n' or medal == 'Gold\n':
                    listOfCountries.append(countries)
                    listOfCountries = list(set(listOfCountries))
                if minMedal == 'Gold' and medal == 'Gold\n':
                    listOfCountries.append(countries)
                    listOfCountries = list(set(listOfCountries))
    
    return listOfCountries


def goldMedalsByCountryAndYears(code, minYear='1896', maxYear='2014'):
    with open('summer.csv', 'r', encoding='utf-8') as file:
        text = file.readlines()[REMOVE_FIRST_LINE_IDX:]
        listOfLines = tuple()
        listOfTuples = []
        
        for word in text:
            name = word.split(',')[ATHLETE_IDX]
            year = word.split(',')[YEAR_IDX]
            discipline = word.split(',')[DISCIPLINE_IDX]
            event = word.split(',')[EVENT_IDX]
            gender = word.split(',')[GENDER_IDX]
            countries = word.split(',')[COUNTRIES_IDX]
            medal = word.split(',')[MEDAL_IDX]
            if minYear == '' and maxYear == '':
                if code == countries:
                    if medal == 'Gold\n':
                        listOfLines = (name, year, discipline, event, gender)
                        listOfTuples.append(listOfLines)
            elif int(minYear) <= int(year) and int(maxYear) >= int(year):
                if code == countries:
                    if medal == 'Gold\n':
                        listOfLines = (name, year, discipline, event, gender)
                        listOfTuples.append(listOfLines)
            
    return listOfTuples