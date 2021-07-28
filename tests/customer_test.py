import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John Smith", 100.00)

    def test_check_customer_money(self):
        drink_1 = Drink("Corona", 5)
        self.assertEqual(True, self.customer.check_customer_money(drink_1)) 

    def test_remove_customer_money(self):
        drink_1 = Drink("Corona", 5)
        self.assertEqual(95.0, self.customer.remove_money_customer(drink_1)) 

    def test_drinking(self):
        Customer_1 = Customer("John Smith", 100.00)
        drink_1 = Drink("Corona", 5, 10)
        Customer_1.hand.append(drink_1)
        print(len(Customer_1.hand))
        Customer_1.drinking(drink_1)
        self.assertEqual(10, Customer_1.drunkenness) 

        