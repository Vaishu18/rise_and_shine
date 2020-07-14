from beverage import Beverage
from ingredient import Ingredient

class CoffeeMachine(object):
    """
    Attributes
    ----------
    outlet : int
        outlets of the coffee machine
    ingredients : dict
        hash map of all the ingredients stored into the coffee machine
    beverages : dict
        hash map of all the beverages that can be prepared from the coffee machine
    """

    def __init__(self):
        super(CoffeeMachine, self).__init__()
        self.outlet = None
        self.ingredients = {}
        self.beverages = {}

    def addBeverage(self,name,recipe):
        ''' Used to feed a beverage detail into the coffee_machine.
            Parameters:
                name of type str
                recipe of type dict
        '''
        b = Beverage(name,recipe)
        self.beverages[name]=b
        return True

    def addIngredient(self,name,quantity):
        ''' Used to add an ingredient into the coffee_machine.
            Parameters:
                name of type str
                quantity of type int
        '''
        i = Ingredient(name,quantity)
        self.ingredients[name]=i
        return True

    def getBeverage(self,name):
        if name in self.beverages:
            return self.beverages.get(name,None)
        else:
            return None

    def getIngredient(self, name):
        if name in self.ingredients:
            return self.ingredients[name]
        else:
            return None

    def checkIngredient(self,name,value):
        ''' Used to check if an ingredient is
            - available (if there is enough quantity of ingredient for a beverage)
            - insufficient
            - not available
            Parameters:
                name of type str
                value of type int
        '''
        if name in self.ingredients:
            if(self.ingredients[name].quantity-value >= 0):
                return 'available'
            else:
                return 'insufficient'
        else:
            return 'not available'

    def checkBeverage(self,name):
        ''' Used to check if a beverage can be prepared or not.
            checkIngredient() is used as a helper function here.
            Parameters:
                name of type str
        '''
        if name in self.beverages:
            b=self.beverages[name]
            if b and b.name==name:
                for ingredient_name,ingredient_value in b.recipe.items():
                    if self.checkIngredient(ingredient_name,ingredient_value) != 'available':
                        return False
            else:
                return False
        return True

    def makeBeverage(self,beverage):
        ''' This functions checks for all the factors to prepare the beverage.
            Returns appropriate messages for the following scenarios:
            - if a beverage is prepared
            - if any ingredient is insufficient
            - if the beverage is unavailable
            Parameters:
                beverage of type str
        '''
        if(self.checkBeverage(beverage)):
            b=self.getBeverage(beverage)
            if b:
                for ingredient_name,ingredient_value in b.recipe.items():
                    i=self.getIngredient(ingredient_name)
                    i.quantity=i.quantity - ingredient_value
                return beverage+' is prepared'
            else:
                return beverage+' is not available'
        else:
            b=self.getBeverage(beverage)
            for ingredient_name,ingredient_value in b.recipe.items():
                response=self.checkIngredient(ingredient_name,ingredient_value)
                if response != 'available':
                    return beverage+' cannot be prepared because '+ingredient_name+' is '+response
                    break

    def fillIngredient(self,ingredient_name,fill_value):
        ''' This functions is used to refill the existing ingredients or add a new ingredient into the coffee machine.
            Parameters:
                ingredient_name of type str
                fill_value of type int
        '''
        if ingredient_name in self.ingredients:
            self.ingredients[ingredient_name].quantity+=fill_value
        else:
            self.addIngredient(ingredient_name,fill_value)

    def getMenu(self):
        print('Choose your beverage:')
        for b in self.beverages:
            print(b)

    def getStock(self):
        print('Machine Inventory:')
        for i in self.ingredients:
            print(i + ' : '+str(self.ingredients[i].quantity))
