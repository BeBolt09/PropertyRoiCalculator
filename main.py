#Creating Class
class RoiCalculator:
    #Initializing the data needed from user
    def __init__(self,purchase,expenses,income):
        self.purchase=purchase
        self.income= income
        self.expenses= expenses
    #Creating a cashFlow method
    def getCashFlow(self):
        cashFlow=self.income - self.expenses
        #Adding a new global self.variable to be accessed by the whole class
        self.cashFlow=cashFlow
        #returning the cashflow so user can have access to that information
        return (f"Our monthly CashFlow is: ${cashFlow}, our annual CashFlow is: ${cashFlow*12}")
    #Creating a roi method
    def getCashOnCashRoi(self):
        downPayment=self.purchase/5
        closingCost=self.purchase*0.015
        repairs=self.purchase*0.035
        #Total cost of initial investment to calculate ROI
        total=downPayment+closingCost+repairs
        #Calculating ROI
        cashOnCashRoi=(self.cashFlow*12)/total
        #Returning the ROI
        return (f"Our Cash on Cash ROI is: {cashOnCashRoi*100}%")

print("Hello, please enter the following amounts to calculate your ROI on this property")
roi1=RoiCalculator(int(input("\nWhat is the purchase price?\n$")),int(input("What are the monthly expenses?\n$")),int(input("What is the monthly income?\n$")))
print(roi1.getCashFlow())
print(roi1.getCashOnCashRoi())
