class utilities:
    def __init__(self, income):
        self.income=income

        #Stores expenses and percentage spent
        self.expense=(
            ("Utilities",0.5),
            ("Rent/housing",0.15),
            ("Transport",0.30),
            ("Healthcare",0.03)
            ("Groceries",0.1)
            ("Communication",0.02)
            )

        #2D array (Threshold, Tax Rate, Base Tax)
        #if income<Threshold
        #   Tax=(income-Threshold) * Rate + Tax Base
        self.threshold=(
        (237101, 0.18, 0), 
        (370501, 0.26, 42678),
        (512801, 0.31, 77362),
        (673001, 0.36, 121475),
        (857901,0.39, 179147),
        (1817001,0.41, 251258),
        (1817002,0.45, 644489)
        )


    def total_income(self):
        for i in range(len(self.threshold)):
            if(self.income<self.threshold(i,0)):
                Tax=(self.income-self.threshold(i,0))*self.threshold(i,1) +self.threshold(i,2)
                return Tax
            
    def expense(self):
        for i in range(len(self.expense)):
            expense=self.total_income()*self.expense(i,1)
            print(f"{self.expense(i,0)}: R{self.expense(i,1)}")
            


    
