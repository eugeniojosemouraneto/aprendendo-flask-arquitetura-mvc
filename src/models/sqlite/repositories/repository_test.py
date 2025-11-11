import pytest
from src.models.sqlite.settings import db_connection_handler
from src.models.sqlite.repositories import PetsRepository


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


# def test_
