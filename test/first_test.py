''' import main code '''
from main import greeter

def test_first_test():
    ''' pp4 first test '''  

    a = 2
    b = 2

    result = a + b
    assert result == 4


def test_greet():
    ''' greet test '''
    #arrange
    name = "Uwu"
    #act
    result = greeter.greet(name)
    #assert
    assert result == "Hello Uwu xd"
