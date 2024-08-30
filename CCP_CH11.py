#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#_______________________ CHAPTER 11 Testing Your Code_______________________________________________

# firstly make sure pip is upgraded ($ python -m pip install --upgrade pip)
# You can use this to install an upgrade on any  ($ python -m pip install --upgrade package_name)
# the same goes for installing   ($ python -m pip install --user package_name)
# e.g. $ python -m pip install --user pytest   

from name_fxn import get_formatted_name

print('Enter "q" at any time to quit')
while True:
    first = input(f'\nPlease input your first name: ')
    if first == 'q':
        break
    last = input(f'\nInput your last name: ')
    if last =='q':
        break
    
    formated_name = get_formatted_name(first, last)
    print(f"\n Neatly Formatted name: {formated_name}")
# in order to run pytest from terminal i needed to run $ python -m pytest and it worked. 
# the terminal is running from same location as where pytest is i think...not sure why its an issue
    
#____________________________________ 11.1 City Country 
#making a new fuction and adding code written in different files just to sum up what was done

'''def get_formatted_name(first, last):
    """Return a neatly formatted name"""
    full_name = f'{first} {last}'
    return full_name.title()


from name_fxn import get_formatted_name

def test_first_last_name():
    """Test if First and Last Name will format correctly"""
    formatted_name = get_formatted_name('jimi', 'hendrix',)
    assert formatted_name == "Jimi Hendrix"
    
    
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

from city_fxns import city_functions

def test_city_country_name():
    """Test is City and Country are formatted correctly """
    city_country = city_functions('san jose', 'california')
    assert city_country == 'San Jose, California'
    
def test_city_country_pop_size():
    "Test if City, Country, and pop size are formatted"
    saratoga = city_functions('saratoga', 'california', 180000)
    assert saratoga == ('Saratoga, California has a population of -180000')'''

#Common uses and assertions for test classes
# assert a == b
# assert a != b
# assert a  (True or False)
# assert not a
# assert element in/not in list 

# Fixtures esentially set up a test env.
# they require a decerator which goes at the front of a function
# @pytest.fixture
# def language_survey(): and so on ->
# you are building am object or function that other tests can call upon 

class AnonymousSurvey:
    """Collect anonamous answers to survey questions"""
    def __init__(self,question):
        """Store a question and prepair to store responses"""
        self.question = question 
        self.responses = []
        
    def show_question():
        """Show survey question"""
        print(self.question)
        
    def store_response(self, new_response):
        """store a single new response"""
        self.responses.append(new_response) 
        
    def show_results(self):
        """Show all responses"""
        print("Survey Results: ")
        for response in self.responses:
            print(f" - {response}")
            
'''from CCP_CH11 import AnonymousSurvey

# define question
question = "What languages did you first learn to speak? "
language_survey = AnonymousSurvey(question)

# show questions and response
language_survey.show_question()
print("Enter 'q' to quit at any time \n")
while True:
    response = input('Language ')
    if response == 'q':
        break 
    language_survey.store_response(response)
    
#Show results of survey
print(f"\nThank you to everyone who participated in the survey!")
language_survey.show_question()'''

# To test the survery reposnse 
# 1 single test for multiple resposes 

'''def test_store_three_responses():
    """Test three responses"""
    question = "What languages did you first first learn to speak? "
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Mandrin', 'Spanish',]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses'''
        
# testing using a fixture
# @pytest.fixture
# def language_survey():
# """A Survey that will be avalaible to all test functions"""
#    question = "What languages did you first first learn to speak? "
#    language_survey = AnonymousSurvey(question)
#    return language_survey
# def test_store_single_response():
#     """Test single response stored"""
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses
#