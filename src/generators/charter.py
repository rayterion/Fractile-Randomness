import random

class Charter:
    def __init__(self, initial_price=1.0, deviation=0.1, generate_unchanged=True):
        self.deviation = deviation
        self.prices = [initial_price]
        self.generate_unchanged = generate_unchanged

    def get_current_price(self):
        return self.prices[len(self.prices) - 1]
    
    def disable_generate_unchanged(self):
        self.generate_unchanged = False

    def enable_generate_unchanged(self):
        self.generate_unchanged = True

    def generate_next(self):
        next_price = self.get_current_price() + random.random() * self.deviation
        self.prices.append(next_price)

    

