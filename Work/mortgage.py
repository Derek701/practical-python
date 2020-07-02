# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_payments = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    num_payments += 1
    if num_payments == extra_payment_start_month:
        payment += extra_payment
    principal *= 1 + rate/12
    if payment > principal:
        payment = principal
    principal -= payment
    total_paid += payment
    print(f'{num_payments:>3} {total_paid:>9.2f} {principal:>9.2f}')
    if num_payments == extra_payment_end_month:
        payment -= extra_payment

print(f'Total paid {total_paid:0.2f}') # Total paid 878202.57
print(f'Months {num_payments:0}') # Months 310
