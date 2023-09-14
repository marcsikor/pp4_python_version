import pytest

from main import credit_card

def test_initial_credit():
    # arrange
    card = credit_card.CreditCard('1234-5678')
    # act
    card.assign_credit(1000)
    # assert
    assert card.get_credit() == 1000

def test_initial_credit_v2():
    # arrange
    card1 = credit_card.CreditCard('1234-5678')
    card2 = credit_card.CreditCard('1234-5679')
    # act
    card1.assign_credit(1000)
    card2.assign_credit(2000)
    # assert
    assert card1.get_credit() == 1000
    assert card2.get_credit() == 2000

def test_denies_credit_below_threshold():
    card = credit_card.CreditCard('234')

    # should raise error
    with pytest.raises(ValueError, match='Credit below limit'):
        card.assign_credit(10)    
    
    # should not raise error
    card.assign_credit(100)
    card.assign_credit(101) 