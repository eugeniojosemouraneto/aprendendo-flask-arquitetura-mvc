from typing import List
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities import PetsTable


class PetsRepository:

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List:
        with self.__db_connection as database:
            try:
                return database.session.query(PetsTable).all()

            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session.query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )
                database.session.commit()

            except Exception as exception:
                database.session.rollback()  # voltar o banco para como ele estava antes do try, ou seja, retorna o banco para como ele estava antes da tentativa de deleção
                raise exception
