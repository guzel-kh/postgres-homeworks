"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='123456'
) as conn:
    with conn.cursor() as cur:
        csvpath_customers = "../homework-1/north_data/customers_data.csv"
        with open(csvpath_customers, 'r', encoding='windows-1251') as file:
            data = csv.DictReader(file)
            for row in data:
                customer_id, company_name, contact_name = row["customer_id"], row["company_name"], row["contact_name"]
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customer_id, company_name, contact_name))

        csvpath_employees = "../homework-1/north_data/employees_data.csv"
        with open(csvpath_employees, 'r', encoding='windows-1251') as file:
            data = csv.DictReader(file)
            for row in data:
                employee_id, first_name, last_name, title, birth_date, notes = \
                    row["employee_id"], row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (employee_id, first_name, last_name,title, birth_date, notes))

        csvpath_orders = "../homework-1/north_data/orders_data.csv"
        with open(csvpath_orders, 'r', encoding='windows-1251') as file:
            data = csv.DictReader(file)
            for row in data:
                order_id, customer_id, employee_id, order_date, ship_city = row["order_id"], row["customer_id"], \
                    row["employee_id"], row["order_date"], row["ship_city"]
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (order_id, customer_id, employee_id, order_date,
                                                                       ship_city))


conn.close()


# csvpath = "../homework-1/north_data/customers_data.csv"
# with open(csvpath, 'r', encoding='windows-1251') as file:
#     data = csv.DictReader(file)
#     for row in data:
#         customer_id, company_name, contact_name = row["customer_id"], row["company_name"], row["contact_name"]
#         # print(customer_id, company_name, contact_name)
#         with conn:
#             with conn.cursor() as cur:
#                 cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customer_id, company_name, contact_name)) # Добавление данных (1 строка)
#                     # rows = cur.fetchall()
#                     # for row in rows:
#                     #     print(row)
