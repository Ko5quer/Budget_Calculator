

"""
Calculates the taxes and expenses based on the user income and tax bracket
"""
class Tax:
    def __init__(self, income):
        self.income=income

        #Stores expenses and average spent on expenses in percentage
        self.exp_list=(
            ("Utilities",0.05),
            ("Rent/housing",0.15),
            ("Transport",0.30),
            ("Healthcare",0.03),
            ("Groceries",0.1),
            ("Communication",0.02)
            )
        """
        2D array (minThreshold, max threshold, Tax Rate, Base Tax)
        if income<Threshold then it meets the threshhold in the tax bracket
        Formula for calculating tax:  Tax=(income-minThreshold) * Rate + Tax Base
        """
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
    Calculates tax based on the above tuple list which is the tax bracket and commpares values according
    to the tax bracket to see which tax bracket it falls under
    """
    def taxIncome(self):
        annual=self.income*12
        for i in range(len(self.tax_brack)):
            if(self.tax_brack[i][0]<annual and annual<self.tax_brack[i][1]):
                tax=((annual-self.tax_brack[i][0])*self.tax_brack[i][2]+self.tax_brack[i][3])/12
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
        total=self.income - self.taxIncome()
        return float(total)
        
    def netIncome(self):
        net_income= self.taxed_inc()-self.tot_Expense()
        return net_income
        
    def dispBudget(self):
        lines="_"*50
        dash="-"*50
        print("\n\t\tMonthly Budget")
        print(lines)
        print("\n\t\tIncome")
        print(dash)
        print(f"Gross Monthly Income (Before Tax): R{self.income:.2f}")
        print(f"Gross Monthly Income (After Tax): R{self.taxed_inc():.2f}")
        print(dash)
        print("\n\t\tExpenses")
        print(dash)
        for i in range(len(self.exp_list)):
            expense=float(self.exp_list[i][1])* float(self.taxed_inc())
            print(f"{self.exp_list[i][0]}:\tR{expense:.2f}")
        print(dash)
        netIncome=self.netIncome()
        print(f"\nNet Income: R{netIncome:.2f}\n")
        print(lines)

def menu():
    print("\nBudget Portal")
    print("________________________")
    print("\n\t1. Create New Entry \n")
    print("\t0. Exit \n")



#Main function
if __name__=="__main__":

    #Menu system that stops when the user wants
    while True:
        menu()
        choice=int(input("Select an option: "))
        if(choice==1):
            #Asks user for code and income input
            code=input("Enter user code: ")
            try:
                income=float(input("Enter gross income before tax: "))

                #Declaring class and callng class in the main functions
                budget=Tax(income)
                budget.dispBudget()
            except ValueError:
                print("Invalid input please enter a number")

        elif(choice==0):
            print("Exiting System. Goodbye!!!")
            break
        else:
            print("Please choose between 1 and 0")

