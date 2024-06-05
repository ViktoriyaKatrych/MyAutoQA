import sqlite3
from sqlite3 import IntegrityError, OperationalError

class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'C:/Users/Viktoriya/WorkAutoQA'+r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")    

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    
    
    def get_user_adress_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record   

    def insert_product(self, product_id, name, description,qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()  

    def delete_product_by_id(self, product_id):
        query = f'DELETE FROM products WHERE id = {product_id}'
        self.cursor.execute(query)
        self.connection.commit()


    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

 #Individual
    def get_all(self):
        query = "SELECT * FROM orders"
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    
    
    def get_all_users(self):
        query = "SELECT * FROM customers"
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    
    
    
    def insert_new_user(self, user_id, username, address, city, postCode, country):
        query = f"INSERT INTO customers(id, name, address, city, postalCode, country) \
            VALUES ({user_id}, '{username}', '{address}', '{city}', '{postCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()  


    def select_users_by_city(self, city, address):
        query = f"SELECT id, name FROM customers WHERE city = '{city}' OR address = '{address}'" 
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 


    def delete_users_by_city(self, city, address):
        query = f"DELETE FROM customers WHERE city = '{city}'  OR address = '{address}'"
        self.cursor.execute(query)
        self.connection.commit()


    def get_all_products(self):
        query = 'SELECT * FROM products'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    
    

    
    def insert_order(self, order_id, customer_id, product_id, order_date):
        query =f'INSERT OR REPLACE INTO orders(id, customer_id, product_id, order_date) \
                VALUES ({order_id}, {customer_id}, {product_id}, {order_date})'
        self.cursor.execute(query)
        self.connection.commit()  

    def delete_order_by_id(self, order_id):
        query = f'DELETE FROM orders WHERE id = {order_id}'
        self.cursor.execute(query)
        self.connection.commit()    

       