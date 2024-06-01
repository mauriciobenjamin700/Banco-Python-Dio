from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.inspection import inspect
from typing import List

if not __name__ == '__main__':
    from src.models.connection import engine
    print("\n\nnão estou na main\n\n")
else:
    from connection import engine
    print("\n\nestou na main\n\n")

class Base(DeclarativeBase):
    def __repr__(self) -> str:
        cls = self.__class__
        column_attrs = inspect(cls).mapper.column_attrs
        columns = {attr.key: getattr(self, attr.key) for attr in column_attrs}
        columns_str = ", ".join(f"{key}={value!r}" for key, value in columns.items())
        return f"{cls.__name__}({columns_str})"


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int]  = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    login: Mapped[str] = mapped_column(String(256), nullable= False, unique=True) 
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    
    my_account: Mapped["Account"] = relationship("Account",
                                                 back_populates="my_client",
                                                 uselist=False, # Assumindo que um cliente tem uma conta (um-para-um)
                                                 cascade="all, delete-orphan"
                                                )

class Account(Base):
    __tablename__ = "account"

    id: Mapped[int]  = mapped_column(primary_key=True)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    id_client: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)
    id_agency: Mapped[int] = mapped_column(ForeignKey("agency.id"), nullable=False)
    
    my_client: Mapped["Client"] = relationship("Client",
                                               back_populates="my_account", 
                                               uselist=False)
    
    my_agency: Mapped["Agency"] = relationship("Agency",
                                               back_populates="accounts",
                                               uselist=False
                                               )
    

class Agency(Base):
    __tablename__ = "agency"
    
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    number: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    id_bank: Mapped[int] = mapped_column(ForeignKey("bank.id"), nullable=False)
    
    accounts: Mapped[List["Account"]] = relationship("Account",
                                                     back_populates="my_agency",
                                                     uselist=True,
                                                     cascade="all, delete-orphan",
                                                    )
    my_bank: Mapped["Bank"] = relationship("Bank",
                                           back_populates="agencies", 
                                           uselist=False)

class Bank(Base):
    __tablename__ = "bank"
    
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    number: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    
    agencies: Mapped[List["Agency"]] = relationship("Agency",
                                                     back_populates="my_bank",
                                                     uselist=True,
                                                     cascade="all, delete-orphan",
                                                    )

# Criando as tabelas no banco de dados (se ainda não existirem)
def create_tables() -> None:
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()