def validate_string(string: str):
    if not isinstance(string, str):
        return False
    if len(string) == 0:
        return False
    
    return True

def validate_strings(*args: str):
    for string in args:
        if not validate_string(string):
            return False
    
    return True

def validade_id(integer: int):
    if not isinstance(integer, int):
        return False
    if integer < 0:
        return False
    
    return True