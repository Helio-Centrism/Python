# Create a class called Order which stores items and their prices. Use Dunder function __gt__() to convey that order1 > order2 if the total price of order1 is greater than the total price of order2.

class Order:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def __gt__(self, order2):
        return sum(self.prices) > sum(order2.prices)
    


order1 = Order(["apple", "banana", "mango"], [50, 30, 40])
order2 = Order(["apple", "banana", "mango"], [10, 40, 50])

print(order1 > order2)

