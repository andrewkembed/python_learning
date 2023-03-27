import math
import array


class Business:
    num_months_exist = 0
    def __init__(self, name, monthlyIncome=500, increasePerYear=0.10, nextBuyPrice=25000):
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


#issues:::

def main():
    print('Building a Business Empire')
    print()
    #print("Jan\t| Feb\t| Mar\t| Apr\t| May\t| Jun\t| Jul\t| Aug\t| Sept\t| Oct\t| Nov\t| Dec\t|")
    savings_account = Savings(0)

    savings_history_list = []   #records all the monthly savings values for printing later

    business_list =[]           #list of all business currenly created
    business_list.append(Business("dribonez",monthlyIncome=350,increasePerYear=0.05,nextBuyPrice=3000))
    #business_list.append(Business("stoneHackle",monthlyIncome=400,increasePerYear=0.05,nextBuyPrice=3000))

    savings_account.change_current_montly_income(business_list[0].get_monthly_income())

    #while(len(business_list) <= 12):
    while(savings_account.get_monthly_income() <= 10000):
        if(savings_account.get_current_savings() < business_list[len(business_list)-1].get_nextBuyPrice()):
            savings_account.add_to_savings(savings_account.get_monthly_income())
            savings_history_list.append(savings_account.get_current_savings())
            #print("current savings: ", savings_history_list[-1])

            for x in business_list[:-1]:
                x.add_to_month_exist()
                if((x.get_num_months_exist() % 12) == 0):
                    savings_account.change_current_montly_income(-x.get_monthly_income())
                    x.calc_new_monthlyIncome()
                    savings_account.change_current_montly_income(x.get_monthly_income())
             #       print("New Income:", x.get_monthly_income())
        else:
            savings_account.subtract_from_savings(business_list[len(business_list)-1].get_nextBuyPrice())
            if((len(business_list)-1) == 0):
                business_list.append(Business("stoneHackle", monthlyIncome=500, increasePerYear=0.05))
            else:
                bus_name = "business" + str(len(business_list)+1)
                business_list.append(Business(bus_name))
            savings_account.change_current_montly_income(business_list[-1].get_monthly_income())
            print("Business purchased:",business_list[-1].get_business_name())
            print(len(savings_history_list), "Months | ",
                  "{:.2f}".format(len(savings_history_list)/12), "Years |", 
                  "Income: $", "{:.2f}".format(savings_account.get_monthly_income()))
        
    print()
    print()
    #for x in business_list:
    #    print(x.get_business_name())
    #    print(x.nextBuyPrice())




if __name__ == "__main__":
    main()

#want to keep creating new business instances until a certain montly income is reached
#keep track of the montly savings, which is used to purchase / initialize the next business
#once a new business is created, the income is added to the savings in order to buy the next business
#every year the income for each business is increased by x% to account for growth
#once some number of rentals is created, continue to add the other business incomes to savings 
#savings should provide an x amount of income at this point until monthly income goal is reached


        #print(savings_account.get_current_savings(), end='\t| ')
        #if((total_num_months % 12) == 0):
        #    print()
        #    print("*Summary* Years: ", str(total_num_months/12) + 
        #          "  Savings: $", str(savings_account.get_current_savings()) + 
        #          "  Num Businesses: ", len(business_list)-1)
        #    print()

            #if((len(savings_history_list) % 12) == 0):
            #    print("Value increased!")
            #    for x in business_list[:-1]:
            #        x.calc_new_monthlyIncome()
            #        print("\n", x.get_business_name(), end=' ')
            #        print(x.get_monthly_income())