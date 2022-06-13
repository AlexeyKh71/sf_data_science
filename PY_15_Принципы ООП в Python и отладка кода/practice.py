import pandas as pd
import math as mt

class DepartmentReport():
    def __init__(self,company):
        self.company = company
        self.revenues = []
            
    def add_revenue(self, amount):
        if not hasattr(self, 'revenues'):  
            self.revenues = [] 
        self.revenues.append(amount)  
    
    def average_revenue(self):
        txt = "Average department revenue for {comapny:}: {average:.0f}"
        return txt.format( comapny=self.company, average = sum(self.revenues)/len(self.revenues))
 
 
report = DepartmentReport("Danon")
report.add_revenue(1_000_000)
report.add_revenue(400_000)

print(report.average_revenue())
# => Average department revenue for Danon: 700000