from sqlalchemy import create_engine, select, String, Integer, Float
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)

engine = create_engine("sqlite:///zapateria.db")


class Base(DeclarativeBase):
    pass


class Zapato(Base):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    modelo: Mapped[str] = mapped_column(
        String(100)
    )

    talla: Mapped[int] = mapped_column(
        Integer
    )

    precio: Mapped[float] = mapped_column(
        Float
    )


def inicializar_bd():
    Base.metadata.create_all(engine)


def crear_zapato(modelo, talla, precio):

    with Session(engine) as session:

        zapato = Zapato(
            modelo=modelo,
            talla=talla,
            precio=precio
        )

        session.add(zapato)
        session.commit()

        return True


def listar_zapatos():

    with Session(engine) as session:

        return session.scalars(
            select(Zapato)
        ).all()


def buscar_zapato(id_zapato):

    with Session(engine) as session:

        return session.get(
            Zapato,
            id_zapato
        )


def actualizar_precio(id_zapato, nuevo_precio):

    with Session(engine) as session:

        zapato = session.get(
            Zapato,
            id_zapato
        )

        if zapato is None:
            return False

        zapato.precio = nuevo_precio

        session.commit()

        return True


def eliminar_zapato(id_zapato):

    with Session(engine) as session:

        zapato = session.get(
            Zapato,
            id_zapato
        )

        if zapato is None:
            return False

        session.delete(zapato)

        session.commit()

        return True