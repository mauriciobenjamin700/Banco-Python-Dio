import pytest
from datetime import datetime

from os.path import abspath, dirname
import sys
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

from src.models.entities.account import Account, get_date, get_string
from src.models.entities.client import Client
from src.models.entities.agency import Agency

# Mock para Client
class MockClient(Client):
    def __init__(self, id, name, doc, phone):
        self._id = id
        self._name = name
        self._doc = doc
        self._phone = phone

# Mock para Agency
class MockAgency(Agency):
    def __init__(self, id, name, code, address):
        self._id = id
        self._name = name
        self._code = code
        self._address = address

def test_account_creation():
    client = MockClient(1, "Mauricio", "123", "123")
    agency = MockAgency(1, "Santander", 1, None)
    account = Account(1, 100.0, client, agency)

    assert account.id == 1
    assert account.balance == 100.0
    assert account.client == client
    assert account.agency == agency
    assert account.transactions == []

def test_account_deposit():
    client = MockClient(1, "Mauricio", "123", "123")
    agency = MockAgency(1, "Santander", 1, None)
    account = Account(1, 100.0, client, agency)

    result = account.deposit(50)
    assert result is True
    assert account.balance == 150.0
    assert len(account.transactions) == 1
    assert "Depósito de R$50.00" in account.transactions[0][0]

def test_account_withdraw():
    client = MockClient(1, "Mauricio", "123", "123")
    agency = MockAgency(1, "Santander", 1, None)
    account = Account(1, 100.0, client, agency)

    result = account.withdraw(50)
    assert result is True
    assert account.balance == 50.0
    assert len(account.transactions) == 1
    assert "Saque de R$50.00" in account.transactions[0][0]

    result = account.withdraw(100)
    assert result is False
    assert account.balance == 50.0
    assert len(account.transactions) == 1

def test_account_statement():
    client = MockClient(1, "Mauricio", "123", "123")
    agency = MockAgency(1, "Santander", 1, None)
    account = Account(1, 100.0, client, agency)

    account.deposit(50)
    account.withdraw(30)
    
    statement = account.statement()
    assert len(statement) == 2
    assert "Depósito de R$50.00" in statement[0]
    assert "Saque de R$30.00" in statement[1]

def test_account_setters():
    client = MockClient(1, "Mauricio", "123", "123")
    agency = MockAgency(1, "Santander", 1, None)
    account = Account(1, 100.0, client, agency)

    with pytest.raises(ValueError):
        account.id = 2

    with pytest.raises(ValueError):
        account.balance = 200.0

    with pytest.raises(ValueError):
        account.client = MockClient(2, "João", "456", "456")

    with pytest.raises(ValueError):
        account.agency = MockAgency(2, "Bradesco", 2, None)

    with pytest.raises(ValueError):
        account.transactions = [("Depósito de R$100.00", get_date())]
