# Main

O Alembic permite que realizemos manipulações nas estruturas do banco de dados sem que precisamos recriar o banco de dados do zero. Ele permite persistir os dados enquanto atualizamos a estrutura do banco.

## Alembic Install

```bash
poetry add  alembic
```

## Alembic configs

Inicialize o alemnbic na raiz do seu projeto usando o combando:

```bash
alembic init alembic
```

Faça as configurações a seguir para que alambic consigo se adaptar ao seu problema

- arquivo ``alembic.ini`` troque o conteúdo da variavel a baixo para o url de conexão do seu Banco de Dados, no meu caso o SQL exige o diretório do SQLite
  - ``sqlalchemy.url = sqlite:///path/to/your/database.db``
- No diretório ``alembic``, abra o arquivo ``env.py`` e configure para usar seu modelo SQLAlchemy. Substitua as linha:
  - ``from myapp import mymodel`` pelo import referente a sua classe Base feita em cima do DeclarativeBase do SQLAlchemy. No meu caso foi `from src.models.tables import Base
  - ``target_metadata`` para usar o ``metadata`` do seu modelo, ficando assim: ``target_metadata = Base.metadata``

## Alembic Commands

Realiza um "Commit" com as novas mudanças nas tabelas acessadas por `Base.metadata`

```bash
alembic revision --autogenerate -m "update"
```

Realiza um "Push" das mudanças commitadas para o banco de dados e garante que o banco irá mantelas

```bash
alembic upgrade head
```

Checa se a versão atual é igual a versão esperada, este é usado apenas para testes e visualização.

```bash
alembic current
```
