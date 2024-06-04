if __name__ == "__main__":
    from os.path import abspath, dirname
    import sys
    
    sys.path.append(dirname(dirname(abspath(__file__))))
    
    from models.entities.client import Address, Contact, Client
    from controllers.funcs.validats import (validate_string, 
                                            validate_strings,
                                            validade_id)
    from controllers.constant.strings import STRING_OPTIONAL
    from controllers.constant.errors import ERROR_ID
    
else:
    from src.models.entities.client import Address, Contact, Client
    from src.controllers.funcs.validats import (validate_string, 
                                                validate_strings,
                                                validade_id)
    from src.controllers.constant.errors import (ERROR_ID, 
                                                 ERROR_CONTACT, 
                                                 ERROR_REQUIERED_FILD,
                                                 ERROR_INSTANCE) 
    
def create_address(
    id: int,
    cep: str,
    street: str, 
    number: str) -> Address:
    
    if not validade_id(id):
        raise TypeError(ERROR_ID)
    
    if not validate_strings(cep, street, number):
        raise ValueError(ERROR_REQUIERED_FILD)
    
    return  Address(id,cep,street,number)

def create_contact(
    id: int,
    phone: str, 
    email: str) -> Contact:
    
    if not validade_id(id):
        raise TypeError(ERROR_ID)
    
    if not validate_string(phone) and not validate_string(email): # case almost types of contacts are invalid, raise an erorr
        raise ValueError(ERROR_CONTACT)
    
    if validate_string(phone): # if just pass the email, its ok
        return Contact(id,phone, STRING_OPTIONAL)
        
    if validate_string(email):
        return Contact(id,STRING_OPTIONAL,email)

def create_cliente(
    id: int,
    name: str,
    login: str,
    password: str,
    contact: Contact,
    address: Address) -> Client:
    
    if not validade_id(id):
        raise TypeError(ERROR_ID)
    
    if not validate_strings(name, login, password):
        raise ValueError(ERROR_REQUIERED_FILD)
    
    return Client(id,name,login,password,contact, address)

def register_client(
    id_client: int,
    name_client: str,
    login_client: str,
    password_client: str,
    id_contact: int,
    phone_client: str,
    email_client: str,
    id_address: int,
    cep_client: str,
    street_client: str,
    house_number_client: str) -> bool:
    
    contact = create_contact(id_contact, phone_client, email_client)
    address = create_address(id_address, cep_client, street_client, house_number_client)
    cliente = create_cliente(id_client, name_client, login_client, password_client, contact, address)
    
    return cliente
    