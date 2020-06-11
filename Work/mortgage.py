# mortgage.py
# 
# Exercise 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_payments = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    num_payments += 1
    if num_payments == extra_payment_start_month:
        payment += extra_payment
    elif num_payments == extra_payment_end_month:
        payment -= extra_payment
    principal *= 1 + rate/12
    if payment > principal:
        payment = principal
    principal -= payment
    total_paid = total_paid + payment
    print(num_payments, round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid,2)) # Total paid 880074.1
print('Months', num_payments)
