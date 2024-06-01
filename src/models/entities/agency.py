class Agency:
    def __init__(self, 
                 id: int, 
                 name: str,
                 number: str,
                 bank: object):
        self._id = id
        self._name = name
        self._number = number
        self._bank = bank