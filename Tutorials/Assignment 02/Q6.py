"""
6. Interest Calculator: (2 Mark)
Set for principal amount, interest rate, and time (in years). Calculate and display the simple interest."""

principal_rate = float(input("Principal Amount ::"))
interest_rate = float(input("Interest Rate ::"))
time = float(input("Time in year ::"))

simple_interest = (principal_rate*interest_rate*time)/100
total_amount = principal_rate + simple_interest
print("Simple Interest =",simple_interest)
print("Total Amount =",total_amount)

