


class Living:
    tot_living={}
    sum_cost=0
    def __init__(self,name, cost):
        self.name=name
        self.cost=cost
        Living.tot_living.update({name:cost})
        
    def add_living(name, cost):
        name=name
        cost=int(cost)
        if Income.tot_income-cost < 0:
            print('You can\'t make this transaction')
        else:
            Income.tot_income=Income.tot_income-cost
            Living.sum_cost= Living.sum_cost+ cost
            Living.tot_living.update({name:cost})
        
    def tot_living_cost():
        print(Living.sum_cost)

#Use the food class as a reference to fix all the other classes
class Food:
    tot_food={}
    sum_cost=0
    def __init__(self, name, cost):
        self.name=name
        self.cost=cost
        Food.tot_food.update({name:cost})
        
    def add_food(name, cost):
        name=name
        cost=int(cost)
        if Income.tot_income-cost < 0:
            print('You can\'t make this transaction')
        else:
            Income.tot_income=Income.tot_income-cost
            Food.sum_cost= Food.sum_cost+ cost
            Food.tot_food.update({name:cost})
        
    def tot_food_cost():
        print(Food.sum_cost)
        
        
class Travel:
    tot_travel={}
    sum_cost=0
    def __init__(self, name, cost):
        self.name=name
        self.cost=cost
        Travel.tot_travel.update({name:cost})
        
    def add_travel(name, cost):
        name=name
        cost=int(cost)
        if Income.tot_income-cost < 0:
            print('You can\'t make this transaction')
        else:
            Income.tot_income=Income.tot_income-cost
            Travel.sum_cost= Travel.sum_cost+ cost
            Travel.tot_travel.update({name:cost})
        
    def tot_travel_cost():
        print(Travel.sum_cost)
        
        
class Leisure:
    tot_leisure={}
    sum_cost=0
    def __init__(self, name, cost):
        self.name=name
        self.cost=cost
        Leisure.tot_leisure.update({name:cost})
        
    def add_leisure(name, cost):
        name=name
        cost=int(cost)
        if Income.tot_income-cost < 0:
            print('You can\'t make this transaction')
        else:
            Income.tot_income=Income.tot_income-cost
            Leisure.sum_cost= Leisure.sum_cost+ cost
            Leisure.tot_leisure.update({name:cost})
        
    def tot_leisure_cost():
        print(Leisure.sum_cost)
        
        
class Saving:
    tot_saving={}
    sum_cost=0
    def __init__(self, name, cost):
        self.name=name
        self.cost=cost
        Saving.tot_saving.update({name:cost})
        
    def add_saving(cost):
        cost=int(cost)
        eval=Income.tot_income - cost
        if eval<0:
            print('You do not have enough money')
        else:
            Income.tot_income=Income.tot_income - cost
            Saving.tot_saving.update({'From Income':cost})
            Saving.sum_cost=Saving.sum_cost+cost

    def tot_savings():
        print(Saving.sum_cost)
        
class Expenses:
    all_transactions=0
    all_expenses={}
    def __init__(self):
        self.living=Living.cost
        self.food=Food.cost
        self.travel=Travel.cost
        self.leisure=Leisure.cost
        self.saving= Saving.cost
        
    def get_all_expenses():
        Expenses.all_expenses.update(Travel.tot_travel, Food.tot_food, Living.tot_living, Leisure.tot_leisure)
        print(Expenses.all_expenses)
        
    def get_all_transactions():
        Expenses.all_transactions+= Living.sum_cost+Food.sum_cost+Travel.sum_cost+Leisure.sum_cost
        print(Expenses.all_transactions)
        
class Income:
    tot_income=0
    def __init__(self, money):
        self.money=money
        
    def add_income(money):
        money=money
        Income.tot_income=Income.tot_income + money
        
