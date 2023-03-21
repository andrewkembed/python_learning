import math


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
    
    def change_currently_montly_income(self, amount):
        self.current_monthly_income += amount



def main():
    print('How long till retirement?')
    stone_hackle_starting_income = 500
    rentals_starting_income = 350
    rentals_apprication = 0.10



    total_num_months = 0
    savings = Savings(0)
    dri_bonez =     Business("DriBonez", 250, 0.075, 0)
    stone_hackle =  Business("Stone Hackle", 0, 0.075, 2500)
    rental1 =       Business("rental1", 0, rentals_apprication, 25000)
    rental2 =       Business("rental2", 0, rentals_apprication, 25000)
    rental3 =       Business("rental3", 0, rentals_apprication, 25000)
    rental4 =       Business("rental4", 0, rentals_apprication, 25000)
    rental5 =       Business("rental5", 0, rentals_apprication, 25000)
    rental6 =       Business("rental6", 0, rentals_apprication, 25000)
    rental7 =       Business("rental7", 0, rentals_apprication, 25000)
    rental8 =       Business("rental8", 0, rentals_apprication, 25000)
    rental9 =       Business("rental9", 0, rentals_apprication, 25000)
    rental10 =      Business("rental10", 0, rentals_apprication, 25000)
    rental11 =      Business("rental11", 0, rentals_apprication, 25000)

    business_array = [dri_bonez, stone_hackle, rental1, rental2, rental3, rental4, 
                      rental5, rental6, rental7, rental8, rental9, rental10, rental11]

    for i in range(len(business_array)):
        if i == (len(business_array) -1 ):
            print("Last business on the list")
            #need to continue to add income to savings
            for z in range(len(business_array)):
                savings.change_currently_montly_income(business_array[z].get_monthly_income())
            print("Current Monthly Income at the end $", savings.get_monthly_income())
            print("Yearly Salary: $",savings.get_current_savings()*12)
        else:
            while(savings.get_current_savings() < business_array[i+1].get_start_amount()):
                for x in range(len(business_array)-1):      #add all incomes to savings
                    savings.add_to_savings(business_array[x].get_monthly_income())

                print("Current Savings: $", savings.get_current_savings())
                savings.add_to_savings(savings.get_monthly_income())
                total_num_months += 1
                if((total_num_months % 12) == 0):
                    print("year: ", total_num_months/12)
                    for y in range(len(business_array)-1):
                        business_array[y].calc_new_monthlyIncome()
            
            savings.subtract_from_savings(business_array[i+1].get_start_amount())
            if i == 0:
                business_array[i+1].change_monthly_income(stone_hackle_starting_income)  #stone_hackle will have different income than rentals
            else:
                business_array[i+1].change_monthly_income(rentals_starting_income)

    print("Total number of months: ", total_num_months)
    print("Total number of years:  ", total_num_months/12)
    
    print("amount in savings ", savings.get_current_savings())
    #take the monthlyIncome from a business and add it to the 
    #   Savings:current_monthly_income ONLY once every 12 turns
    #   as well as add to the current savings
    #do above until purchase price is reached in savings
    #then remove the purchase price from savings 
    #then start to include the entity that was just purchased


                #while (savings.get_current_savings() <= business_array[i+1].get_start_amount()): #aways increase i+1
            #    for x in range(i+1):
            #        savings.add_to_savings(business_array[x].get_monthly_income())
            #        #print("Where: ", business_array[x].get_business_name(), "Saving Amount: ", savings.get_current_savings())
            #    total_num_months += 1
            #savings.subtract_from_savings(business_array[i+1].get_start_amount())




if __name__ == "__main__":
    main()