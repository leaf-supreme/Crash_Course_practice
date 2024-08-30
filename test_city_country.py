from city_fxns import city_functions

def test_city_country_name():
    """Test is City and Country are formatted correctly """
    city_country = city_functions('san jose', 'california')
    assert city_country == 'San Jose, California'
    
def test_city_country_pop_size():
    "Test if City, Country, and pop size are formatted"
    saratoga = city_functions('saratoga', 'california', 180000)
    assert saratoga == 'Saratoga, California has a population of -180000'