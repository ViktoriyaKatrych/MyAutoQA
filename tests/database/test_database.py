import sys
import pytest
from modules.common.database import Database
from sqlite3 import IntegrityError, OperationalError, DatabaseError
from datetime import datetime
from datetime import date
from datetime import time

sys.stdout.reconfigure(encoding='utf-8')

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)    


@pytest.mark.database
def test_check_user_sergiy():
    db = Database()
    user = db.get_user_adress_by_name('Sergii')

    print(user)
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    
    print(water_qnt)
    
    assert water_qnt[0][0] == 25  


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    print(water_qnt)
    assert water_qnt[0][0] == 30 


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    qnt = db.select_product_qnt_by_id(99)

    print(qnt)

    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    print(qnt)

    assert len(qnt) == 0 


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print('Замовлення', orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'            


#   My tests

#Get infor all customers
@pytest.mark.dbusers
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    l = len(users)
    print("All records are: ", l)
    print(users)   


# Test Adding new Customer. Inputting correctly data to every field.
# Testing Customers must be from id 500.
# Check how inputed data writted to DB.

@pytest.mark.dbusers
def test_user_insert():
    db = Database()
    users = db.get_all_users()
    count_user = len(users)
    end_user = count_user+500
    db.insert_new_user(end_user, 'Vasyl', 'S. Bandery, 22', 'Lviv', '2555kk', 'Ukraine')
     
    users = db.get_all_users()
    print(users)

    newcount_user = len(users)
    print(newcount_user)
   
    assert newcount_user == count_user+1   
    assert users[count_user][0] == end_user
    assert users[count_user][1] == 'Vasyl'
    assert users[count_user][2] == 'S. Bandery, 22'
    assert users[count_user][3] == 'Lviv'
    assert users[count_user][4] == '2555kk'
    assert users[count_user][5] == 'Ukraine'


# Test Adding new Customer. Inputting incorrectly data to every field.
# Testing Customers must have Id from 500.
# DB allows writing incorectly data

@pytest.mark.dbuserserr
def test_user_insert_no_rigth_date():
    db = Database()
    users = db.get_all_users()
    count_user = len(users)
    end_user = count_user+500
    #print ("Converted date:", datetime.strptime('2024-5-23','%Y-%m-%d'))
 
    db.insert_new_user(end_user, 8888888, 'S. Bandery, 22', True, 2345, datetime.strptime('2024-5-23','%Y-%m-%d'))

    users = db.get_all_users()
    print(users)

@pytest.mark.dbuserserr
def test_user_insert_no_rigth():
    db = Database()
    users = db.get_all_users()
    count_user = len(users)
    end_user = count_user+500
    db.insert_new_user(end_user, 8888888, 'S. Bandery, 22', True, 2345, 2024-5-23)

    users = db.get_all_users()
    print(users)    
  

# Test before Added Customer with incorrectly data. 
# Check how inputed data writte to DB.

@pytest.mark.dbuserserr
def test_detailed_users():
    db = Database()
    users = db.get_all_users()

    count_users = len(users)
    print("All records are: ", count_users)
    print(users)      
   
    assert users[count_users-1][0] == (count_users-1)+500
    print({users[count_users-1][0]}, {(count_users-1)+500})

    assert users[count_users-1][1] != 8888888
    assert users[count_users-1][2] == 'S. Bandery, 22'
    
    assert users[count_users-1][3] != True
    print({users[count_users-1][3]}, True)


    assert users[count_users-1][4] == '2345'

    assert users[count_users-1][5] != datetime.strptime('2024-5-23','%Y-%m-%d')
    print({users[count_users-1][5]}, datetime.strptime('2024-5-23','%Y-%m-%d'))



# Select all users by filter City or Address
@pytest.mark.dbusers
def test_users_select_by_city():
    db = Database()
    users = db.select_users_by_city('Lviv', 'S. Bandery, 22')
    print(users)

# Select and Delete all users by filter City or Address
@pytest.mark.dbusers
def test_users_delete():
    db = Database()
    users = db.select_users_by_city('Lviv', 'S. Bandery, 22')
    print(users)

    db.delete_users_by_city('Lviv', 'S. Bandery, 22')
    users = db.get_all_users()
    print(users)

#Get all Products
@pytest.mark.dbproduct
def test_check_all_products():
    db = Database()
    products = db.get_all_products()
    print(products)  

# Adding new Product to DB with correctly data    
@pytest.mark.dbproduct
def test_product_insert():
    db = Database()
    db.insert_product(5, 'Water', 'CocaCola', 60)
    water_qnt = db.select_product_qnt_by_id(5)

    print(water_qnt)
    assert water_qnt[0][0] == 60

@pytest.mark.dbproduct222
def test_product_insert1():
    db = Database()
    db.insert_product(1, 'Солодка вода', 'З цукром', 10)
    water_qnt = db.select_product_qnt_by_id(1)

    print(water_qnt)
    assert water_qnt[0][0] == 10    

# Adding new Product to DB with incorrectly data quantity.
# System must display exeption  
@pytest.mark.dbproducterr
def test_product_insert_notrigth():
    with pytest.raises(OperationalError) as excinfo:
        db = Database()
        db.insert_product(6, 'Water', 'PepsiCola', '70 od')
 
    assert "syntax error" in str(excinfo.value)   
    #    assert sqlite3.OperationalError: near "grn": syntax error
    #assert OperationalError() ==True
    #print("Error inputed data")

# Test delete some Product, if this product is in Orders table for some order.
@pytest.mark.dbproducterr
def test_product_delete_orders():
    db = Database()
    products = db.get_all_products()
    print(products)
    db.delete_product_by_id(1)

    products = db.get_all_products()
    print(products)
 
      


# Get all Orders
@pytest.mark.dborders
def test_check_all():
    db = Database()
    order = db.get_all()

    print(order)   

# Adding new Orders to table Orders. Get all orders.
@pytest.mark.dborders
def test_insert_new_order():
    db = Database()
    db.insert_order(2, 504, 2, 5556)
    order = db.get_all()
    print(order)    

# Test to Delete order from table Orders.
@pytest.mark.dborderserr
def test_delete_order():
    db = Database()
    db.delete_order_by_id(2)
    order = db.get_all()
    print(order)        
  
