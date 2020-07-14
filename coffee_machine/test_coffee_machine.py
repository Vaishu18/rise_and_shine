import pytest
from coffee_machine import CoffeeMachine

class TestCoffeeMachine(object):
    coffee_machine=CoffeeMachine()
    coffee_machine.outlet = 4

    def test_add_ingredient(self):
        assert self.coffee_machine.addIngredient('hot_water',500) == True
        assert self.coffee_machine.addIngredient('hot_milk',500) == True
        assert self.coffee_machine.addIngredient('ginger_syrup',100) == True
        assert self.coffee_machine.addIngredient('sugar_syrup',100) == True
        assert self.coffee_machine.addIngredient('tea_leaves_syrup',100) == True

    def test_add_beverage(self):
        assert self.coffee_machine.addBeverage('hot_tea',{"hot_water": 200,"hot_milk": 100,"ginger_syrup": 10,"sugar_syrup": 10,"tea_leaves_syrup": 30}) == True
        assert self.coffee_machine.addBeverage('black_tea',{"hot_water": 300,"ginger_syrup": 30,"sugar_syrup": 50,"tea_leaves_syrup": 30}) == True

    def test_get_beverage(self):
        assert self.coffee_machine.getBeverage('green_tea') == None
        assert self.coffee_machine.getBeverage('black_tea').name == 'black_tea'

    def test_get_ingredient(self):
        assert self.coffee_machine.getIngredient('hot_milk').name == 'hot_milk'
        assert self.coffee_machine.getIngredient('green_mixture') == None

    def test_make_beverage(self):
        assert self.coffee_machine.makeBeverage('hot_tea') == 'hot_tea is prepared'
        assert self.coffee_machine.makeBeverage('green_tea') == 'green_tea cannot be prepared because green_mixture is not available'
        
