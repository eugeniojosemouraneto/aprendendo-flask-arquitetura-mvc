from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities import PeopleTable, PetsTable


class PeopleRepository:

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        with self.__db_connection as database:
            try:
                person_data = PeopleTable(
                    first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
                )
                database.session.add(person_data)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_person(self, person_id: int) -> PeopleTable:
        with self.__db_connection as database:
            try:
                return (
                    database.session.query(PeopleTable)
                    .outerjoin(PetsTable, PetsTable.id == PeopleTable.person_id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PetsTable.name.label("pet_name"),
                        PetsTable.type.label("pet_type"),
                    )
                )  # retornando informações de pessoa com o nome do seu pet associado

            except NoResultFound:
                return None
