# mortgage.py
# 
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_payments = 0

while principal > 0:
    num_payments += 1
    if num_payments == 1:
        payment += 1000
    elif num_payments == 13:
        payment -= 1000
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', round(total_paid,2))
print('Months', num_payments)
