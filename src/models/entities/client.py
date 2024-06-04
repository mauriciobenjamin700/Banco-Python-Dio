from ast import Add


class Contact:
    def __init__(self, 
                 id: int,
                 phone: str, 
                 email: str) -> None:
        
        self._id = id
        self._phone = phone
        self._email = email
        
        @property
        def id(self) -> int:
            return self._id
        
        @property
        def phone(self) -> str:
            return self._phone
        
        @property
        def email(self) -> str:
            return self._email
        
        @id.setter
        def id(self, id: int) -> None:
            raise ValueError("Can't set a id property on Contact")
        
        @phone.setter
        def phone(self, phone: str) -> None:
            self._phone = phone
        
        @email.setter
        def email(self, email: str) -> None:
            self._email = email

class Address:
    def __init__(self, 
                 id: int,
                 cep: str,
                 street: str, 
                 number: str) -> None:
        
        self._id = id
        self._cep = cep
        self._street = street
        self._number = number
        
        @property
        def id(self) -> int:
            return self._id
        
        @property
        def cep(self) -> str:
            return self._cep
        
        @property
        def street(self) -> str:
            return self._street
        
        @property
        def number(self) -> str:
            return self._number
        
        @id.setter
        def id(self, id: int) -> None:
            raise ValueError(f"ID cannot be modified to {id}")
        
        @cep.setter
        def cep(self, cep: str) -> None:
            self._cep = cep
            
        @street.setter
        def street(self, street: str) -> None:
            self._street = street
        
        @number.setter
        def number(self, number: str) -> None:
            self._number = number
                    

class Client:
    """
    Está classe representa a entidade Cliente no Sistema.
    
    Atributs:
        id: int
        name: str
        login: str
        password: str
    
    Methods:
        sign_int(): bool
        sign_out(): bool
    
    """
    def __init__(self, 
                 id: int, 
                 name: str,
                 login: str,
                 password: str,
                 contact: Contact,
                 Address: Address
                 ) -> None:
        
        self._id = id
        self._name = name
        self._login = login
        self._password =  password
        
        
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def login(self) -> str:
        return self._login
    
    @property
    def password(self) -> str:
        return self._password
    
    @id.setter
    def id(self, id: int) -> None:
        raise ValueError(f"ID cannot be modified to {id}")
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
        
    @login.setter
    def login(self, login: str) -> None:
        self._login = login
        
    @password.setter
    def password(self, password: str) -> None:
        self._password =  password
        
    def sign_in(self) -> bool:
        ...
    
    def sign_out(self) -> bool:
        ...
        
