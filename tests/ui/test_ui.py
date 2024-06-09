import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui 
def test_check_incorrect_username():
    
    # Створення об'єкту для керування броузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   
       
    # Відкриваємо сторінку https://github.com/Login
    driver.get("https://github.com/Login")

    # Знаходимо поле, в яке будемо вводити неправвильне імєя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача абл поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # Знаходимо поле, і яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")
    
    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME,"commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    
    time.sleep(55)
   
    #Закриваємо броузер
    driver.close()

