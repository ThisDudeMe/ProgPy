import pytest
from app.account import *


@pytest.mark.parametrize("earned, spent, expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(earned, spent, expected):
    my_account = Account(earned)
    my_account.spend_cash(spent)
    assert my_account.balance == expected


def test_account_add_cash(account):
    account.add_cash(80)
    assert account.balance == 100

def test_account_spend_cash(account):
    account.spend_cash(10)
    assert account.balance == 10

def test_account_spend_cash_raise_exception(empty_account):
    with pytest.raises(InsufficentAmount):
        empty_account.spend(200)
