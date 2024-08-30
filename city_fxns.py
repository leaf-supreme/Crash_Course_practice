def city_functions(city, country, population=None):
    """Return formatted name of city and coutry"""
    if population: 
        return (f'{city.title()}, {country.title()} has a population of -{population}')
    else:
        city_country = (f'{city.title()}, {country.title()}')
        return city_country

san = city_functions('san jose', 'california')
print(san)

saratoga = city_functions('Saratoga','CA', 90000)
print(saratoga)