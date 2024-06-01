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