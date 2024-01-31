import pytest
from app.account import *

@pytest.fixture
def empty_account():
    return(Account(0))

@pytest.fixture
def account():
    return Account(20)
