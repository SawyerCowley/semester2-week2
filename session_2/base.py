import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    #conn.row_factory = sqlite3.Row
    return conn

def categories():
    db = get_connection()

    query = '''
    SELECT category
    FROM products;
    '''
    
    cursor = db.execute(query)
    for row in cursor:
        print(row)

    db.close()

def customers():
    db = get_connection()

    query = '''
    SELECT COUNT(customer_id)
    FROM customers;
    '''
    
    cursor = db.execute(query)
    for row in cursor:
        print(row)

    db.close()

def orders():
    user = input("Enter user email - ")

    db = get_connection()

    query = '''
    SELECT p.name
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    WHERE c.email = ?;
    '''
    
    cursor = db.execute(query, (user,))
    print(cursor.fetchall())

    db.close()

def sub2():
    db = get_connection()

    query = '''
    SELECT name
    FROM products
    WHERE price < 2;
    '''
    
    cursor = db.execute(query)
    for row in cursor:
        print(row)

    db.close()

def top5():
    db = get_connection()

    query = '''
    SELECT c.first_name, o.total_amount
    FROM customers c
    JOIN orders o on c.customer_id = o.customer_id
    ORDER BY o.total_amount DESC
    LIMIT 5;
    '''
    
    cursor = db.execute(query)
    for row in cursor:
        print(row)

    db.close()

def order_per_category():
    
    db = get_connection()

    query = '''
    SELECT p.category, count(o.order_id)
    FROM orders o 
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY p.category
    ORDER BY count(o.order_id) DESC;
    '''
    
    cursor = db.execute(query)
    for row in cursor:
        print(row)

    db.close()

def main():

    '''
    categories()
    customers()
    orders()
    sub2()
    top5()
    '''
    order_per_category()

if __name__=="__main__":
    main()
