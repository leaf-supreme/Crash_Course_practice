import pytest 
from Employee_class import Employee


def test_give_default_raise():
    """Testing the default raise of 5000"""
    lacy = Employee('lacy','smith',85_000)
    lacy.give_raise()
    assert lacy.year_money == 90000
    
def test_give_non_stad_raise():    #test fxn cant have same name as other test as it will only run 1
    """Test for  a non standard raise of 6000"""
    jody = Employee('jody','smith',85_000)
    jody.give_raise(6000)
    assert jody.year_money == 91000    # jody.year_money != jody.year_money()
    
#use test fixture so i dont have to create a new employee everytime
@pytest.fixture
def employee_a():
    """Creaet Generic Employee for test fixture"""
    employee_a = Employee('Employee_A', "Smith", 50_000)
    return employee_a
    
def test_give_std_raise(employee_a):
    """Test to give 5000 standard raise"""
    employee_a.give_raise()
    assert employee_a.year_money == 55_000
    
def test_give_non_std_raise(employee_a):
    """Test to give non-standard raise (6_000)"""
    employee_a.give_raise(6000)
    assert employee_a.year_money == 56_000
    
def test_give_non_reg_rasie_to_test_test(employee_a):
    """This is a test for pytest to see if it increase amout by 1"""
    employee_a.give_raise(200_000)
    assert employee_a.year_money == 250_000