class Customer:
    def __init__(self, name, wallet, age = 0):
        self.name = name
        self.wallet = wallet
        self.capacity = []
        self.hand = []
        self.age = age
        self.drunkenness = 0

    def check_customer_money(self, drink):
        if self.wallet >= drink.price:
            return True

    def remove_money_customer(self, drink):
        if self.check_customer_money(drink):
            self.wallet -= drink.price
            return self.wallet

    def take_drink(self, drink, pub):
        pub.bar.remove(drink)
        self.hand.append(drink)

    def number_of_drinks_in_hand(self):
        return len(self.hand)

    def drinking(self, drink):
        self.drunkenness += drink.alcohol_units
        self.hand.remove(drink)
