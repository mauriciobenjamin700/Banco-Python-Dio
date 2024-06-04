from src.models.tables import create_tables, Bank, Agency
from src.models.connection import Session

#print("\n\nVou Criar o Banco de Dados ...")

# Criando as tabelas se ainda não existirem
create_tables()

#print("\n\nCriei o Banco de Dados")

with Session() as s:
    # Verificar se o banco padrão já existe
    existing_bank = s.query(Bank).filter_by(name="Administrador", number="007").first()
    if not existing_bank:
        print("Banco padrão não existe, criando agora...")
        default_bank = Bank(name="Administrador", number="007")
        s.add(default_bank)  # adicionando o banco para poder usar seu ID
        s.commit()  # Precisamos comitar aqui para garantir que o ID do banco seja gerado antes de usá-lo na agência
    else:
        default_bank = existing_bank
        print("Banco padrão já existe.")
    
    # Verificar se a agência padrão já existe
    existing_agency = s.query(Agency).filter_by(name="LocalHost", number="001", id_bank=default_bank.id).first()
    if not existing_agency:
        print("Agência padrão não existe, criando agora...")
        default_agency = Agency(name="LocalHost", number="001", id_bank=default_bank.id)
        default_bank.agencies.append(default_agency)
        s.add(default_agency)
        try:
            s.commit()
            print("Registros inseridos com sucesso!")
        except Exception as e:
            s.rollback()
            print(f"Erro ao inserir registros: {e}")
    else:
        print("Agência padrão já existe.")
