import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


class User:
  
    def __init__(self) -> None:
        self.name=None
        self.second_name=None

    def create(self):
        self.name = 'Вікторія'
        self.second_name='Катрич'

    def remove(self):
        self.name = ''
        self.second_name=''

@pytest.fixture
def user():
    user=User()
    user.create()
    
    yield user

    user.remove()

@pytest.fixture
def github_api():
    apigithub=GitHub()

    yield apigithub


@pytest.fixture
def connectdb():
   db=Database()

   yield db
