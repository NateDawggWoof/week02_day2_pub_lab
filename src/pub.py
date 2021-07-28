class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.bar = []
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)
    
    def check_drink(self, drink_name):
        for drink in self.drinks:
            if drink_name == drink.name:
                return drink

    def remove_drink(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                self.drinks.remove(drink)
    
    def add_money_till(self, drink):
        self.till += drink.price

    def place_drink_on_bar(self, drink):
        self.bar.append(drink)

    def number_of_stock(self):
        return len(self.drinks)

    def sell_drink(self, customer, drink_name, pub):
        # 1. check_drink
        drink_request = self.check_drink(drink_name)
        if drink_request != None:
            print('it worked!')
            # 2. check_customer_money
            if customer.check_customer_money(drink_request) == True:

                # 3. remove_customer_money
                customer.remove_money_customer(drink_request)
        
                # 4. add_money_to_till
                self.add_money_till(drink_request)
                
                # 5. remove_drink_stock
                self.remove_drink(drink_request.name)

                # 6. place_drink_on_bar
                self.place_drink_on_bar(drink_request)

                # 7. customer -> take_drink
                customer.take_drink(drink_request, pub)

            else:
                print("Sorry you don't have enough money")
                return
        else:
            print('Sorry not found')
            return
        
            