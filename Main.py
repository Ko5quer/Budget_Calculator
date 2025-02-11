income=0
class Tax:
    def __init__(self, income):
        self.income=income

        #Stores expenses and percentage spent
        self.exp_list=(
            ("Utilities",0.05),
            ("Rent/housing",0.15),
            ("Transport",0.30),
            ("Healthcare",0.03),
            ("Groceries",0.1),
            ("Communication",0.02)
            )

        #2D array (minThreshold,max threshold, Tax Rate, Base Tax)
        #if income<Threshold
        #   Tax=(income-minThreshold) * Rate + Tax Base
        self.tax_brack=(
        (1, 237100, 0.18, 0), 
        (237101, 370500, 0.26, 42678),
        (370501, 512800, 0.31, 77362),
        (512801, 673000, 0.36, 121475),
        (673001, 857900, 0.39, 179147),
        (857901 , 1817001, 0.41, 251258),
        (1817002,100000000000000,0.45, 644489)
        )
    """
    Calculates tax based on the above tuple list which is the task bracket
    """
    def taxIncome(self):
        for i in range(len(self.tax_brack)):
            if(self.tax_brack[i][0]<self.income and self.income<self.tax_brack[i][1]):
                tax=(self.income-self.tax_brack[i][0])*self.tax_brack[i][2]+self.tax_brack[i][3]
                return tax
    

    """
    Calculates the total expense based on the tupple that stores the list and displays them
    """
    def tot_Expense(self):
        total=0
        for i in range(len(self.exp_list)):
            expense=self.taxed_inc()*self.exp_list[i][1]
            total=total+expense
        return total
        
    def taxed_inc(self):
        total=self.income-self.taxIncome()
        return total
        
    def netIncome(self):
        net_income= (self.income-self.taxIncome())-self.tot_Expense()
        return net_income


def menu():
    print("\nBudget Portal")
    print("________________________")
    print("\n\t1. Create New Entry \n")
    print("\t0. Exit \n")

def disp_budget(income):
    dash="-"*60
    line="_"*60
    print("\n\t\t\t\tMonthly Budget")
    print(line)
    print("\n\t\t\t\tIncome")
    Calc=Tax(income)
    print(dash)
    print(f"Gross Monthly Income (Before Tax): R{float(income)}")
    print(f"Gross Monthly Income (After Tax): R{float(income-Calc.taxIncome())}")
    print(dash)
    print("\n\t\t\t\tExpenses")
    print(dash)
    for i in range(len(Calc.exp_list)):
        print(f"{Calc.exp_list[i][0]}: \tR{(float(Calc.exp_list[i][1])*float(Calc.taxed_inc()))}")
    print(f"Total Expenses: R{float(Calc.tot_Expense())}")
    print(f"{dash}\n")
    print(f"Net Income: R{float(Calc.netIncome())}")
    print(f"{line}\n")


if __name__=="__main__":
    while True:
        menu()
        choice=int(input("Select an option: "))
        if(choice==1):
            code=input("Enter user code: ")
            income=float(input("Enter gross income before tax: "))
            disp_budget(income)
        elif(choice==2):
            break
        else:
            print("Please choose between 1 and 2")

