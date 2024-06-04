from typing import List

if not __name__ == '__main__':
    import sys
    from os.path import abspath, dirname
    
    sys.path.append(dirname(abspath(__file__)))
    
    from agency import Agency

class Bank:
    def __init__(self,
                 id: int,
                 name: str,
                 number: str,
                 agencies: List[Agency] = []
                 )-> None:

        self._id = id
        self._name = name
        self._number = number
        
        self._agencies = agencies # list of agencies that are associated with the bank
        
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
        def agencies(self) -> list:
            return self._agencies
        
        @name.setter
        def name(self, name: str) -> None:
            self._name = name
        
        @number.setter
        def number(self, number: str) -> None:
            self._number = number
        
        @agencies.setter
        def agencies(self, agency: Agency) -> None:
            self._agencies.append(agency)
        
        
    def add_agency(self, new_agency: Agency) -> bool:
    
        if isinstance(new_agency, Agency):
            if not any(agency.id == new_agency.id for agency in self._agencies): # check if agency already exists, if not exists, app
                self._agencies.append(new_agency)
                return True
            
        return False
    
    def search_agency(self, id: int) -> Agency | None:
        
        if len(self._agencies) != 0:
            for agency in self._agencies:
                if agency.id == id:
                    return agency
        return None
    
    def remove_agency(self, id: int) -> bool:
        
        agency = self.search_agency(id)
        if agency:
            del agency
            return True
        
        return False
        
        