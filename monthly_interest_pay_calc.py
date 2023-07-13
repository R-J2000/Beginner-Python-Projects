# Monthly interest payment calculator

# Get user input
loan_amount = float(input("Enter loan amount: "))
interest_rate = float(input("Enter annual interest rate (%): "))
loan_term = int(input("Enter loan term (years): "))

# Convert interest rate to monthly rate
monthly_rate = (interest_rate / 100) / 12

# Calculate monthly payment
num_payments = loan_term * 12
monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate)**(-num_payments))

# Calculate total payment amount
total_payment = monthly_payment * num_payments

# Calculate total interest paid
total_interest = total_payment - loan_amount

# Display results
print(f"Loan amount: ${loan_amount:.2f}")
print(f"Interest rate: {interest_rate:.2f}%")
print(f"Loan term: {loan_term} years")
print(f"Monthly payment: ${monthly_payment:.2f}")
print(f"Total payment: ${total_payment:.2f}")
print(f"Total interest paid: ${total_interest:.2f}")