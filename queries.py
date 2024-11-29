# pylint:disable=C0111,C0103

import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
a = conn.cursor()

def query_orders(db):
    # return a list of orders displaying each column
    query = """SELECT *
    FROM Orders
    ORDER BY OrderID
    """
    db.execute(query)
    query_orders_list = db.fetchall()
    return query_orders_list


def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query = """SELECT *
    FROM Orders
    WHERE ? < OrderDate AND OrderDate <= ?
    ORDER BY OrderDate
    """
    db.execute(query, (date_from, date_to))
    get_orders_range_list = db.fetchall()
    return get_orders_range_list


def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta

    query = """SELECT *, JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) diff
    FROM Orders
    ORDER BY diff
    """
    db.execute(query)
    get_waiting_time_list = db.fetchall()
    return get_waiting_time_list
