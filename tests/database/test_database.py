import sys
import pytest
from modules.common.database import Database
from sqlite3 import IntegrityError, OperationalError, DatabaseError
from datetime import datetime
from datetime import date
from datetime import time

sys.stdout.reconfigure(encoding='utf-8')

#+++++ General tests =============

@pytest.mark.database
def test_database_connection(connectdb):
    rr = connectdb.test_connection()
    print(rr)
   
    assert rr == True


@pytest.mark.database
def test_check_all_users(connectdb):
    users = connectdb.get_all_users()
    count = len(users)
    print(count)

    assert count !=0 and count > -1

   
@pytest.mark.database
def test_check_user_sergiy(connectdb):
    user = connectdb.get_user_adress_by_name('Sergii')

    print(user)

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update(connectdb):
    connectdb.update_product_qnt_by_id(1, 25)
    water_qnt = connectdb.select_product_qnt_by_id(1)
    
    print(water_qnt)
    
    assert water_qnt[0][0] == 25  


@pytest.mark.database
def test_product_insert(connectdb):
    connectdb.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = connectdb.select_product_qnt_by_id(4)

    print(water_qnt)
    
    assert water_qnt[0][0] == 30 


@pytest.mark.database
def test_product_delete(connectdb):
    connectdb.insert_product(99, 'тестові', 'дані', 999)
    qnt = connectdb.select_product_qnt_by_id(99)

    print(qnt)

    connectdb.delete_product_by_id(99)
    qnt = connectdb.select_product_qnt_by_id(99)

    print(qnt)

    assert len(qnt) == 0 


@pytest.mark.database
def test_detailed_orders(connectdb):
    orders = connectdb.get_detailed_orders()
    print('Замовлення', orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'            


#======   My tests ==========

#  Get  all customers.
@pytest.mark.dbcust
def test_check_all_customers(connectdb):
    users = connectdb.get_all_customers()

    l = len(users)
    print("All records are: ", l)
    print(users) 
    
    assert l>0  


# Test Adding new Customer. Inputting correctly data to every field.
# Testing Customers must be from id 500.
# Check how inputed data writted to DB.

@pytest.mark.dbcust
def test_customer_insert(connectdb):
    users = connectdb.get_all_customers()
    count_user = len(users)
    end_user = count_user+500
    connectdb.insert_new_customer(end_user, 'Vasyl', 'S. Bandery, 22', 'Lviv', '2555kk', 'Ukraine')
     
    users = connectdb.get_all_customers()
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


# Test added new Customer and input incorrectly data to Custtomer table:
# Name, City, PostCode, Country fields.

# Testing Customers must have Id from 500.

# Error:  DB allows writing incorectly data to Name, City, PostCode, Country fields.
#         No control inputted data in DB.

@pytest.mark.dbcusterr
def test_customer_insert_no_rigth_data(connectdb):
    users = connectdb.get_all_customers()
    count_user = len(users)
    end_user = count_user+500
    
    connectdb.insert_new_customer(end_user, 8888888, 'S. Bandery, 22', True, 2345, datetime.strptime('2024-5-23','%Y-%m-%d'))

    users = connectdb.get_all_customers()
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


# Select all customers by filter City or Address
@pytest.mark.dbcust
def test_customers_select_by_city_or_street(connectdb):
    users = connectdb.select_customer_by_city_or_address('Lviv', 'S. Bandery, 22')
    print(users)
    count = len(users)
    for i in range (count-1):
        assert users[i][3] == "Lviv" or users[i][2] == 'S. Bandery, 22'

   
# Select and Delete all users by filter City or Address
@pytest.mark.dbcust
def test_customer_delete(connectdb):
    users = connectdb.select_customer_by_city_or_address('Lviv', 'S. Bandery, 22')
    print(users)

    connectdb.delete_customer_by_city_or_address('Lviv', 'S. Bandery, 22')
    users = connectdb.get_all_customers()
    print(users)
    count = len(users)
    for i in range (count-1):
        assert users[i][3] != "Lviv" or users[i][2] != 'S. Bandery, 22'
    

# Adding new Product to DB with incorrectly data quantity.
# System must display exeption
# Errtest  
@pytest.mark.dbproduct
def test_product_insert_not_rigth(connectdb):
    with pytest.raises(OperationalError) as excinfo:
        connectdb.insert_product(6, 'Water', 'PepsiCola', '70 od')
 
    assert "syntax error" in str(excinfo.value)   
   

# Test delete some Product with id=1.
# But this case is Error when this product is in Orders table for some customer.
# DB doesn't check relationship. 
# Rezult this test must be failed.
# Errtest
@pytest.mark.dbproduct
def test_product_delete_by_pkey(connectdb):
    connectdb.insert_product(5, 'Water', 'CocaCola', 60)
    products = connectdb.get_all_products()
    print(products)
    id=1
    product_name_id = products[0][2]
    with pytest.raises(DatabaseError) as excinfo:
        connectdb.delete_product_by_id(id)

    products = connectdb.get_all_products()
    print(products)
    
    assert product_name_id != products[0][2]


#Get all Products
@pytest.mark.dbproduct
def test_check_all_products(connectdb):
    products = connectdb.get_all_products()
    count = len(products)
    print(count)
    print(products)
    connectdb.insert_product(1, 'солодка вода', 'з цукром', 10)
    water_qnt = connectdb.select_product_qnt_by_id(1)
    print(water_qnt)
    products = connectdb.get_all_products()
    new_count = len(products)
    
    assert water_qnt[0][0] == 10
    assert count == new_count-1      

   
# Adding new Orders to table Orders.
@pytest.mark.dborder
def test_insert_new_order(connectdb):
    order = connectdb.get_all_orders()
    count = len(order)
    connectdb.insert_order(2, 504, 2, 5556)
    order = connectdb.get_all_orders()
    newcount = len(order)
    print(order) 
    
    assert newcount == count+1   


# Test to Delete order from table Orders, where id_orders > 1.
@pytest.mark.dborder
def test_delete_order(connectdb):
    id = 1
    connectdb.delete_order_by_id(id)
    order = connectdb.get_all_orders()
    print(order)
    new_id = order[0][0]

    assert new_id < 2        
  
