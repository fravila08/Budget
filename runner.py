#expenses Living, Food, Travel, Savings, and Leisure
#new expenses need to be aggrevated to expenses
#income
#divide monthly cost by income to get monthly percentage 
from expenses import Food
from expenses import Living
from expenses import Travel
from expenses import Leisure
from expenses import Saving
from expenses import Income
from expenses import Expenses


menu='''
1.Add Income
2.See current Balance
3.Add to Savings from current Balance
4.See current Savings
5.Add or see Expenses
6. Exit
'''
menu2='''What kind of expense would you like to Add or Inspect?
1.Food
2.Inspect Food
3.Living
4.Inspect Living
5.Travel
6.Inspect Travel
7.Leisure
8.Inspect Leisure
9.List of all expenses
10.Expense Total
11.Back to Main Menu
'''
gdbye='Have a nice day Jon'
qstion='Would you like to check something else? (yes/no)'
print('Hello Jon, what would you like to do today?')
quest=input(menu)
while int(quest) <6:
    if quest=='1':
        money=input('How much would you like to add?')
        Income.add_income(int(money))
        print(f'Your new balnce is {Income.tot_income}')
        follow=input(qstion)
        if follow.lower() == 'yes':
            quest=input(menu)
        else:
            print(gdbye)
            break
    if quest=='2':
        print(f'Your current balance is {Income.tot_income}')
        follow=input(qstion)
        if follow.lower() == 'yes':
            quest=input(menu)
        else:
            print(gdbye)
            break
    if quest == '3':
        cost=input(f'How much money would you like to transfer to your Savings? p.s. you may include a short memo before entering amount')
        Saving.add_saving(cost)
        print(f'Your current Savings is {Saving.sum_cost} and your balance is {Income.tot_income}')
        follow=input(qstion)
        if follow.lower() == 'yes':
            quest=input(menu)
        else:
            print(gdbye)
            break
    if quest=='4':
        print(f'Your current Savings are {Saving.sum_cost}')
        follow=input(qstion)
        if follow.lower() == 'yes':
            quest=input(menu)
        else:
            print(gdbye)
            break
    if quest=='5':
        quest2=input(menu2)
        if quest2 == '1':
            name=input('What is the name of the expense?')
            cost=input('How much did it cost?')
            Food.add_food(name, cost)
            print(f'Your new Balane is {Income.tot_income}')
            if follow.lower() == 'yes':
                quest=input(menu)
            else:
                print(gdbye)
                break
        if quest2=='2':
            print(Food.tot_food)
        if quest2=='3':
            name=input('What is the name of the expense?')
            cost=input('How much did it cost?')
            Living.add_living(name, cost)
            print(f'Your new Balane is {Income.tot_income}')
            if follow.lower() == 'yes':
                quest=input(menu)
            else:
                print(gdbye)
                break
        if quest2=='4':
            print(Living.tot_living)
        if quest2=='5':
            name=input('What is the name of the expense?')
            cost=input('How much did it cost?')
            Travel.add_travel(name, cost)
            print(f'Your new Balane is {Income.tot_income}')
            if follow.lower() == 'yes':
                quest=input(menu)
            else:
                print(gdbye)
                break
        if quest2=='6':
            print(Travel.tot_travel)
        
        if quest2=='7':
            name=input('What is the name of the expense?')
            cost=input('How much did it cost?')
            Leisure.add_leisure(name, cost)
            print(f'Your new Balane is {Income.tot_income}')
            if follow.lower() == 'yes':
                quest=input(menu)
            else:
                print(gdbye)
                break
        if quest2=='8':
            print(Leisure.tot_leisure)
        if quest2== '9':
            Expenses.get_all_expenses()
        if quest=='10':
            Expenses.get_all_transactions()
        if quest2=='11':
            quest=input(menu)
            
        