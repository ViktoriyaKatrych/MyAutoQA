import pytest

@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Вікторія'

@pytest.mark.check    
def test_change_secondname(user):
    assert user.second_name == 'Катрич'    