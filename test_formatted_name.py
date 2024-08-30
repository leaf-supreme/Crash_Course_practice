#Pytesting Program

from name_fxn import get_formatted_name

def test_first_last_name():
    """Test if First and Last Name will format correctly"""
    formatted_name = get_formatted_name('jimi', 'hendrix',)
    assert formatted_name == "Jimi Hendrix"