class Business:
    #current_profit = 0
    def __init__(self, name, monthlyIncome, increasePerYear, startAmount):
        self.name = name
        self.monthlyIncome = monthlyIncome
        self.increasePerYear = increasePerYear
        self.startAmount = startAmount
    
    def calc_new_monthlyIncome(self):
        self.monthlyIncome *= (1 + self.increasePerYear)
    
    def get_monthly_income(self):
        return self.monthlyIncome
    
    def get_start_amount(self):
        return self.startAmount

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
    total_num_months = 0
    savings = Savings(0)
    dri_bonez =     Business("DriBonez", 200, 0.05,0)
    stone_hackle =  Business("Stone Hackle", 500, 0.05, 2500)
    rental1 =       Business("rental1", 350, 0.08, 25000)
    rental2 =       Business("rental2", 350, 0.08, 25000)
    rental3 =       Business("rental3", 350, 0.08, 25000)
    rental4 =       Business("rental4", 350, 0.08, 25000)
    rental5 =       Business("rental5", 350, 0.08, 25000)
    rental6 =       Business("rental6", 350, 0.08, 25000)
    rental7 =       Business("rental7", 350, 0.08, 25000)
    rental8 =       Business("rental8", 350, 0.08, 25000)
    rental9 =       Business("rental9", 350, 0.08, 25000)
    rental10 =      Business("rental10", 350, 0.08, 25000)

    business_array = [dri_bonez, stone_hackle, rental1, rental2, rental3, rental4, 
                      rental5, rental6, rental7, rental8, rental9, rental10]


    for i in range(2): #len(business_array)):
        while (savings.get_current_savings() <= business_array[i+1].get_start_amount()):
            savings.add_to_savings(business_array[i].get_monthly_income())
            total_num_months += 1
        savings.subtract_from_savings(business_array[i+1].get_start_amount())
    print("Total number of months: ", total_num_months)
    print("Total number of years:  ", total_num_months/12)
    
    print("amount in savings ", savings.get_current_savings())
    #take the monthlyIncome from a business and add it to the 
    #   Savings:current_monthly_income ONLY once every 12 turns
    #   as well as add to the current savings
    #do above until purchase price is reached in savings
    #then remove the purchase price from savings 
    #then start to include the entity that was just purchased



if __name__ == "__main__":
    main()