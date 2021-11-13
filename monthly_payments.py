
# Taking input from the user
print('Please enter the following information: ')
initial_loan_P = float(input("Initial amount of loan: "))
int_rate_r = float(input('Annual interest rate (in %): '))
num_years_n = float(input('Number of years: '))
print("")  # empty line

# Calculations and using formula
int_rate_r = int_rate_r / 100 / 12
num_years_n = num_years_n * 12

x = (1 + int_rate_r) ** num_years_n
monthly_pay = initial_loan_P * (int_rate_r * x / (x - 1))
total_pay = monthly_pay * num_years_n
interest_pay = total_pay - initial_loan_P

# Showing the results
print(f"Monthly payment: ${monthly_pay:.2f}")
print(f"Total paid: ${total_pay:.2f}")
print(f"Interest Paid: ${interest_pay:.2f}")
