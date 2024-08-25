from Employee_class import Employee


def test_give_default_raise():
    """Testing the default raise of 5000"""
    lacy = Employee('lacy','smith',85000)
    lacy.give_raise()
    assert lacy.year_money == 90000
    
def test_give_non_std_raise():
    jody = Employee('jody','smith',85000)
    jody.give_raise(6000)
    assert jody.year_money == 91000     # jody.year_money != jody.year_money()