from unittest import TestCase
from src.generators.charter import Charter

class CharterTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.range = 0.3
        cls.initial = 10
        cls.charter = Charter(cls.initial, cls.range)
    
    def test_generate_next_value(self):
        """ Generates a new price and stores it in the price chart """
        prev_price = self.charter.get_current_price()
        
        self.charter.disable_generate_unchanged()
        self.charter.generate_next()
        self.charter.enable_generate_unchanged()
        
        new_price = self.charter.get_current_price()

        self.assertNotEqual(prev_price, new_price)
        self.assertTrue(abs(new_price - prev_price) <= self.range)
        