

if not __name__ == "__main__":
    from src.models.entities.account import Account
    from src.models.entities.bank import Bank
    from src.models.entities.base import Base
else:
    from account import Account
    from base import Base
    from bank import Bank

class Agency(Base):
    def __init__(self, 
                 id: int, 
                 name: str,
                 number: str,
                 bank: Bank
                 ) -> None:
        self._id = id
        self._name = name
        self._number = number
        self._bank = bank
        
        self._accounts = [] # list of accounts that are associated with the account
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def number(self) -> str:
        return self._number
    
    @property
    def bank(self) -> object:
        return self._bank
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
        
    @number.setter
    def number(self, number: str) -> None:
        self._number = number
        
    def add_account(self, new_account: Account) -> bool:
        
        if isinstance(new_account, Account):
            if not any(account.id == new_account.id for account in self._accounts): # check if account already exists, if not exists, app
                self._accounts.append(new_account)
                return True
            
        return False
    
    def search_account(self, id: int) -> Account | None:
        
        if len(self._accounts) != 0:
            for account in self._accounts:
                if account.id == id:
                    return account
        return None
    
    def remove_account(self, id: int) -> bool:
        
        account = self.search_account(id)
        if account:
            del account
            return True
        
        return False
    
    
    