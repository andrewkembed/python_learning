class Business:
    #current_profit = 0
    def __init__(self, name, monthlyIncome, increasePerYear):
        self.name = name
        self.monthlyIncome = monthlyIncome
        self.increasePerYear = increasePerYear
    
    def calc_new_monthlyIncome(self):
        self.monthlyIncome *= (1 + self.increasePerYear)
    
    def get_monthly_income(self):
        return self.monthlyIncome

class Savings:

    current_monthly_income = 0      #tracks how much making per month

    def __init__(self, current_savings):
        self.current_savings = current_savings      #how much have saved
    
    def add_to_savings(self, deposit):
        self.current_savings += deposit
    
    def subtract_from_savings(self, withdraw):
        self.current_savings -= withdraw
    
    def get_monthly_income(self):
        return self.current_monthly_income
    
    def get_current_savings(self):
        return int(self.current_savings)



def main():
    print('How long till retirement?')
    savings = Savings(0)
    dri_bonez = Business("DriBonez", 200, 0.05)
    stone_hackle = Business("Stone Hackle", 500, 0.05)
    rental1 = Business("rental1", 350, 0.08)
    rental2 = Business("rental2", 350, 0.08)
    rental3 = Business("rental3", 350, 0.08)
    rental4 = Business("rental4", 350, 0.08)
    rental5 = Business("rental5", 350, 0.08)

    while (savings.get_current_savings() <= 2500):
        savings.add_to_savings(dri_bonez.get_monthly_income())
        print ("Current Savings: ", savings.get_current_savings())
    #take the monthlyIncome from a business and add it to the 
    #   Savings:current_monthly_income ONLY once every 12 turns
    #   as well as add to the current savings
    #do above until purchase price is reached in savings
    #then remove the purchase price from savings 
    #then start to include the entity that was just purchased



if __name__ == "__main__":
    main()