from sqlalchemy import create_engine


# Caminho do arquivo do banco de dados SQLite
db_path = "test.sqlite"

# Criando a engine do SQLAlchemy
engine = create_engine(f"sqlite:///{db_path}")

