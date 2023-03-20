class Business:
    #current_profit = 0
    def __init__(self, name, monthlyIncome, increasePerYear):
        self.name = name
        self.monthlyIncome = monthlyIncome
        self.increasePerYear = increasePerYear
    
    def calc_new_monthlyIncome(self):
        self.monthlyIncome *= (1 + self.increasePerYear)

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



def main():
    print('How long till retirement?')
    b1 = Business("lotion" ,200, 0.05)
    b1.calc_new_monthlyIncome()
    print(b1.monthlyIncome)


if __name__ == "__main__":
    main()