import math
import array


class Business:
    num_months_exist = 0
    def __init__(self, name, monthlyIncome=350, increasePerYear=0.10, nextBuyPrice=25000):
        self.name = name
        self.monthlyIncome = monthlyIncome
        self.increasePerYear = increasePerYear
        self.nextBuyPrice = nextBuyPrice
    
    def calc_new_monthlyIncome(self):
        self.monthlyIncome *= (1 + self.increasePerYear)
    
    def get_monthly_income(self):
        return self.monthlyIncome
    
    def get_nextBuyPrice(self):
        return self.nextBuyPrice
    
    def get_business_name(self):
        return self.name
    
    def change_monthly_income(self, amount):
        self.monthlyIncome += amount
    
    def get_num_months_exist(self):
        return self.num_months_exist
    
    def add_to_month_exist(self):
        self.num_months_exist += 1

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

    #####Initial Conditions
    db_monthlyIncome = 300
    db_increasePerYear = 0.10
    db_nextBuyPrice = 3000

    sh_monthlyIncome = 650
    sh_increasePerYear = 0.10
    #######################

    print("********** Building a Business Empire **********")
    print()
    savings_account = Savings(0)

    business_list =[]
    business_list.append(Business("Dri-Bonez",monthlyIncome=db_monthlyIncome,
                                  increasePerYear=db_increasePerYear,nextBuyPrice=db_nextBuyPrice))

    savings_account.change_current_montly_income(business_list[0].get_monthly_income())

    while(len(business_list) <= 7):     #limiting the number of rentals to 5
        if(savings_account.get_current_savings() < business_list[len(business_list)-1].get_nextBuyPrice()):
            savings_account.add_to_savings(savings_account.get_monthly_income())

            for x in business_list:
                x.add_to_month_exist()
                if((x.get_num_months_exist() % 12) == 0):
                    savings_account.change_current_montly_income(-x.get_monthly_income())
                    x.calc_new_monthlyIncome()
                    savings_account.change_current_montly_income(x.get_monthly_income())
        else:
            savings_account.subtract_from_savings(business_list[len(business_list)-1].get_nextBuyPrice())
            if((len(business_list)-1) == 0):
                business_list.append(Business("Stone Hackle", 
                                              monthlyIncome=sh_monthlyIncome, 
                                              increasePerYear=sh_increasePerYear))
            else:
                bus_name = "Rental" + str(len(business_list)-1)
                business_list.append(Business(bus_name))
            savings_account.change_current_montly_income(business_list[-1].get_monthly_income())
            print("Business purchased:",business_list[-1].get_business_name())
            print(business_list[0].get_num_months_exist(), "Months | ",
                  "{:.2f}".format(business_list[0].get_num_months_exist()), "Years |", 
                  "Income: $", "{:.2f}".format(savings_account.get_monthly_income()),
                  "Savings after Purchase: $", savings_account.get_current_savings())
    print()
    print("*** SUMMARY OF BUSINESSES ***")
    print("Name\t\tExist (Years)\tEnding Income per Month")
    for y in business_list:
        print(y.get_business_name(), "\t", 
              "{:.2f}".format(y.get_num_months_exist()/12), "\t\t", 
              "${:.2f}".format(y.get_monthly_income()))
    print("\nMonthly Income: $", "{:.2f}".format(savings_account.get_monthly_income()))
    print("Years to Complete:", "{:.2f}".format(business_list[0].get_num_months_exist()/12))
    print("Amount Remaining in Savings: $",savings_account.get_current_savings())
        

if __name__ == "__main__":
    main()