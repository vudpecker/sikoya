import unittest
from exercise.concepts.db_pgsql import add_customer_table

class AddCustomerTableTest(unittest.TestCase):
    def test_connect_to_db(self):
        customers = add_customer_table.connect_to_db()
        print(customers)