#Interest Calculator
finalAccountValue       =   float(input("Enter Final Account Value: "))
annualInterestRate      =   (float(input("Enter Annual Interest Rate: ")))/100
numberOfYears           =   int(input("Enter Number of Years: "))
initialDepositAmount    =   finalAccountValue/((1+annualInterestRate)**numberOfYears)
print   ("The initial deposit amount should be:", initialDepositAmount)