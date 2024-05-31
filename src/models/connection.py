from sqlalchemy import create_engine
from os.path import abspath, dirname, join

root = dirname(dirname(dirname(abspath(__file__))))

# Caminho do arquivo do banco de dados SQLite
db_path = join(root,"database.db")
print(db_path)

# Criando a engine do SQLAlchemy
engine = create_engine(f"sqlite:///{db_path}")

