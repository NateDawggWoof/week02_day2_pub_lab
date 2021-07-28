import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self): # NEW
        self.pub = Pub("The Prancing Pony", 100.00)
        drink_1 = Drink("Corona", 5)
        drink_2 = Drink("Chang", 10)
        drink_3 = Drink("Stella", 15)
        self.pub.drinks = [drink_1, drink_2, drink_3]

    def test_pub_has_name(self): # NEW
        self.assertEqual("The Prancing Pony", self.pub.name) 

    def test_pub_has_drink(self): # NEW
        self.assertEqual(self.pub.drinks[0], self.pub.check_drink('Corona')) 

    def test_remove_drink(self):
        self.pub.remove_drink('Chang')
        self.assertEqual(2, self.pub.number_of_stock()) 

    def test_add_money_till(self):
        found_drink = self.pub.check_drink('Corona')
        self.pub.add_money_till(found_drink)
        self.assertEqual(105, self.pub.till) 

    def test_give_drink_to_customer(self):
        Customer_1 = Customer("John Smith", 100.00)
        found_drink = self.pub.check_drink('Corona')
        self.pub.place_drink_on_bar(found_drink)
        Customer_1.take_drink(found_drink, self.pub)
        self.assertEqual(1, Customer_1.number_of_drinks()) 

    def test_sell_drink(self):
        Customer_1 = Customer("John Smith", 100.00)
        self.pub.sell_drink(Customer_1, 'Chang', self.pub)    

        self.assertEqual(90.0, Customer_1.wallet)
        self.assertEqual(110.0, self.pub.till)
        self.assertEqual(2, self.pub.number_of_stock())
        self.assertEqual(1, Customer_1.number_of_drinks())
