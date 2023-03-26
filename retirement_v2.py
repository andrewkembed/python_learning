import math
import array


class Business:
    #current_profit = 0
    def __init__(self, name, monthlyIncome, increasePerYear, buyPrice):
        self.name = name
        self.monthlyIncome = monthlyIncome
        self.increasePerYear = increasePerYear
        self.buyPrice = buyPrice
    
    def calc_new_monthlyIncome(self):
        self.monthlyIncome *= (1 + self.increasePerYear)
    
    def get_monthly_income(self):
        return self.monthlyIncome
    
    def get_start_amount(self):
        return self.buyPrice
    def get_business_name(self):
        return self.name
    
    def change_monthly_income(self, amount):
        self.monthlyIncome += amount

class Savings:

    current_monthly_income = 0      #tracks how much making per month

    def __init__(self, current_savings):
        self.current_savings = current_savings      #how much have saved
    
    def add_to_savings(self, deposit):
        self.current_savings += deposit
    
    def subtract_from_savings(self, withdraw):
        self.current_savings -= withdraw

    def get_current_savings(self):
        return int(self.current_savings)
        
    def get_monthly_income(self):
        return self.current_monthly_income
    
    def change_current_montly_income(self, amount):
        self.current_monthly_income += amount



def main():
    print('How long till retirement?')



if __name__ == "__main__":
    main()

#want to keep creating new business instances until a certain montly income is reached
#keep track of the montly savings, which is used to purchase / initialize the next business
#once a new business is created, the income is added to the savings in order to buy the next business
#every year the income for each business is increased by x% to account for growth
#once some number of rentals is created, continue to add the other business incomes to savings 
#savings should provide an x amount of income at this point until monthly income goal is reached
