"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """

    query = '''
            SELECT f.title, s.screen, t.price
            FROM customers c
            JOIN tickets t ON c.customer_id = t.customer_id
            JOIN screenings s ON t.screening_id = s.screening_id
            JOIN films f ON s.film_id = f.film_id
            WHERE c.customer_id = ?
            ORDER BY f.title
            '''
    
    cursor = conn.execute(query, (customer_id,))
    films = cursor.fetchall()
    return films
    pass


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """

    query = '''
            SELECT s.screening_id, f.title, COUNT(t.ticket_id)
            FROM screenings s
            JOIN films f ON s.film_id = f.film_id
            JOIN tickets t ON s.screening_id = t.screening_id
            GROUP BY f.film_id
            ORDER BY COUNT(t.ticket_id) DESC
            '''
    
    cursor = conn.execute(query)
    sales = cursor.fetchall()
    return sales
    pass


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    pass