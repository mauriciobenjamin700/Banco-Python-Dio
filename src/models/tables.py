from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.inspection import inspect

if not __name__ == '__main__':
    from src.models.connection import engine
else:
    from connection import engine

class Base(DeclarativeBase):
    def __repr__(self) -> str:
        cls = self.__class__
        column_attrs = inspect(cls).mapper.column_attrs
        columns = {attr.key: getattr(self, attr.key) for attr in column_attrs}
        columns_str = ", ".join(f"{key}={value!r}" for key, value in columns.items())
        return f"{cls.__name__}({columns_str})"


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int]  = mapped_column(Integer,primary_key=True,nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    login: Mapped[str] = mapped_column(String(30), nullable= False, unique=True) 
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    abacate: Mapped[str] = mapped_column(String(30), nullable=True)
    #password = Column(String(255), unique=True, nullable=False)
    
    my_account: Mapped["Account"] = relationship("Account",
                                                 back_populates="my_client",
                                                 uselist=False, # Assumindo que um cliente tem uma conta (um-para-um)
                                                 cascade="all, delete-orphan"
                                                )

class Account(Base):
    __tablename__ = "account"

    account_number: Mapped[int]  = mapped_column(primary_key=True,nullable=False)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    id_client: Mapped[int] = mapped_column(ForeignKey("client.id"))
    
    my_client: Mapped["Client"] = relationship("Client",back_populates="my_account")
    



# Criando as tabelas no banco de dados (se ainda não existirem)

Base.metadata.create_all(engine)
