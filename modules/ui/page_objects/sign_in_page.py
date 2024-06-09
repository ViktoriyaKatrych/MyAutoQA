from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)  

    def try_login(self, username, password):
        # знаходимо поле, в яке бкдемо вводити неправильне ім1я користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо неправильне ім'я користувача або поштову адресу
        login_elem.send_keys(username)

        # Знахожимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID,"password")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")
        
        # Емулюємо клік лівою кноакою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
        

#+++++++++++  My test  ==============

class BasketProductPage(BasePage):
    URL = 'https://rozetka.com.ua/ua/'

    def __init__(self) -> None:
        super().__init__()


    def go_to_page(self):
        self.driver.get(BasketProductPage.URL)
        self.driver.maximize_window()


    def go_to_basket(self):
        self.driver.find_element(By.CLASS_NAME, "header-cart__button")
        btn_element = self.driver.find_element(By.CLASS_NAME, "header-cart__button")
        btn_element.click()


    def check_basket(self):
        message_basket = self.driver.find_element(By.CLASS_NAME, "cart-dummy__heading")
        rr = message_basket.get_attribute("textContent")
        return rr
    

    def find_product(self, product_name):
        product_element = self.driver.find_element(By.NAME, "search")
        product_element.send_keys(product_name)
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, ".button.button_color_green.button_size_medium.search-form__submit")

        btn_elem.click()


    def check_title(self, expected_title):
        return self.driver.title == expected_title
    

    def add_selected_product_to_basket(self):
        buy_btn_elem = self.driver.find_element(By.CSS_SELECTOR,".buy-button.goods-tile__buy-button.ng-star-inserted")
        buy_btn_elem.click()


    def check_basket_no_empty(self):
        btn_basket_elem = self.driver.find_element(By.CSS_SELECTOR, ".buy-button.goods-tile__buy-button.ng-star-inserted.buy-button_state_in-cart")
       
        #icon-basket-filled, click on basket filled icon"
        time.sleep(1)
        btn_basket_elem.click()
        time.sleep(2)

        #find button with text "Оформити замовлення"       
        btn_order_elem = self.driver.find_element(By.CSS_SELECTOR,".rz-checkout-button.ng-star-inserted")
        btn_order_description = btn_order_elem.get_attribute("textContent")
        
        print('######1111 ',  btn_order_description) 
        return btn_order_description
        
              
            