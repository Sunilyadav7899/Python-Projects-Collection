# Input
monthly_rent = int(input("Enter your total monthly rent: "))
monthly_food_expenses = int(input("Enter monthly food expenses: "))
electricity_units_consumed = int(input("Enter monthly used electricity units: "))
cost_per_unit = int(input("Enter the charge per electricity unit: "))
number_of_persons = int(input("Enter the number of persons living in the flat: "))

# Calculating the expenses
electricity_bill = electricity_units_consumed * cost_per_unit
total_expenses = monthly_rent + monthly_food_expenses + electricity_bill
amount_per_person = round(total_expenses / number_of_persons)

# Printing Output
print(f"\nTotal monthly expenses: {total_expenses}")
print(f"Each person will pay: {amount_per_person}")

# OUTPUT
# Enter your total monthly rent: 5000
# Enter monthly food expenses: 2000
# Enter monthly used electricity units: 300
# Enter the charge per electricity unit: 10
# Enter the number of persons living in the flat: 3

# Total monthly expenses: 10000
# Each person will pay: 3333