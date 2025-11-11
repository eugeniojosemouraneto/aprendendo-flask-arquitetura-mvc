import pytest
from src.models.sqlite.settings import db_connection_handler
<<<<<<< HEAD
from src.models.sqlite.repositories import PetsRepository, PeopleRepository
=======
from src.models.sqlite.repositories import PetsRepository
>>>>>>> 55d3b87d7719a39499e22db41db79def163e325b


db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="integração com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection=db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)


@pytest.mark.skip(reason="integração com o banco de dados")
def test_delete_pets():
    repo = PetsRepository(db_connection=db_connection_handler)
    repo.delete_pets(name="belinha")  # pegando um nome que está armazenado


<<<<<<< HEAD
def test_insert_person():
    repo = PeopleRepository(db_connection=db_connection_handler)
    repo.insert_person(first_name="test name", last_name="test last", age=77, pet_id=2)
=======
# def test_
>>>>>>> 55d3b87d7719a39499e22db41db79def163e325b
