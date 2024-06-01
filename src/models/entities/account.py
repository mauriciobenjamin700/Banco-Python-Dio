from datetime import datetime
from typing import List, Tuple, Union,NoReturn

if not __name__ == "__main__":
    from src.models.entities.base import Base
    from src.models.entities.client import Client
    from src.models.entities.agency import Agency
else:
    from base import Base
    from client import Client
    from agency import Agency

def get_date() -> datetime:
    return datetime.strptime(datetime.today().strftime("%d-%m-%Y %H:%M:%S"),"%d-%m-%Y %H:%M:%S")
def get_string(date: datetime) -> str:
    return date.strftime('%d/%m/%Y %H:%M:%S')
    
    
class Account(Base):
    def __init__(self, 
                 id: int, 
                 balance: float,
                 client: Client,
                 agency: Agency,
                 transactions: List[Tuple[Union[str, datetime]]] = []
                 ) -> None:
        
        self._id = id
        self._balance = balance
        self._client = client
        self._agency = agency
        self._transactions = transactions if transactions is not None else []
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def client(self) -> Client:
        return self._client
    
    @property
    def agency(self) -> Agency:
        return self._agency
    
    @property
    def transactions(self) -> List[str]:    
        return self._transactions
    
    @id.setter
    def id(self, id) -> NoReturn:
        raise ValueError(f"ID cannot be modified to {id}")
    
    @balance.setter
    def balance(self, balance) -> NoReturn:
        raise ValueError(f"Balance cannot be modified to {balance}")
    
    @client.setter
    def client(self, client) -> NoReturn:
        raise ValueError(f"Client cannot be modified to {client}")
    
    @agency.setter
    def agency(self, agency) -> NoReturn:
        raise ValueError(f"Agency cannot be modified to {agency}")
    
    @transactions.setter
    def transactions(self, transactions) -> NoReturn:
        raise ValueError(f"Transactions cannot be modified to {transactions}")
    
    def deposit(self, value: int | float) -> bool:
        if not isinstance(value,(int,float)):
            #raise TypeError("Value must be a int or float")
            return False
        if value < 0:
            #raise ValueError("Value cannot be negative")
            return False
        
        self._balance += value
        self._transactions.append((f"Depósito de R${value:.2f}", get_date()))
        
        return True
                

    def withdraw(self, value: int | float) -> bool:
        if not isinstance(value,(int,float)):
            #raise TypeError("Value must be a int or float")
            return False
        if value < 0:
            #raise ValueError("Value cannot be negative")
            return False
        if value > self._balance:
            return False
        
        self._balance -= value
        self._transactions.append((f"Saque de R${value:.2f}", get_date()))
        
        return True
    
    def statement(self) -> List[str] | list:
        if len(self._transactions) == 0:
            return []
        
        return [f"{text} em {get_string(date)}" for text, date in self._transactions]

if __name__ == "__main__":
    account = Account(1, 100, Client(1, "Mauricio","123","123"), Agency(1, "Santander", 1,None))
    print(account.deposit(100))
    print(account.withdraw(100))
    print(account.statement())
    print(account)