from modules.ui.page_objects.sign_in_page import SignInPage
import pytest
from modules.ui.page_objects.sign_in_page import BasketProductPage
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong pssword")

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо броузер
    sign_in_page.close()

    
#=========   My test   ++++++++++

# Test Baasket Product is empty
@pytest.mark.uirz
def test_basket_product_empty_object():
    basket_product = BasketProductPage()
    basket_product.go_to_page()
   
    basket_product.go_to_basket()

    assert basket_product.check_basket() == "Кошик порожній"
    
    time.sleep(10)
    basket_product.close()


# Test input some Product to Search field and find this product
@pytest.mark.uirz
def test_search_product_object():
    basket_product = BasketProductPage()
    basket_product.go_to_page()
   
    basket_product.find_product("ecoflow")
    time.sleep(7)

    assert basket_product.check_title('ROZETKA — Результати пошуку: "ecoflow" | Пошук')


# Test Add searched Product to Basket and Basket not empty 
@pytest.mark.uirz
def test_add_to_basket_product_object():
    basket_product = BasketProductPage()
    basket_product.go_to_page()
    
    basket_product.find_product("ecoflow")
    time.sleep(3)
    basket_product.add_selected_product_to_basket()
    time.sleep(3)
    assert basket_product.check_basket_no_empty() == " Оформити замовлення "
    
    time.sleep(10)
    basket_product.close()