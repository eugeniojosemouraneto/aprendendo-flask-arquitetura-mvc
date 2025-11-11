# Setting Up a Python Virtual Environment and Installing Dependencies
pip install virtualenv
python3 -m venv venv
.\venv\Scripts\activate
python.exe -m pip install --upgrade pip

# Install dependencies
.\venv\Scripts\pip freeze > requirements.txt

# Linting
pip install pylint

# Pytest
pytest -s -v
pytest -s -v src\models\sqlite\repositories\pets_repository_test.py