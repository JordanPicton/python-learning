# Defining variables:
tax_rate = 0.4
threshold = 11000

# Main Program
name = input("Please input your name: ")
entry = input("Please input your salary: ")

salary = int(entry)
tax_payable = (salary - threshold) * tax_rate
pay = salary - tax_payable

# Using .rjust below sets the amount of characters specified within the first value of the rjust function.
# Meaning X characters are wanted here, but if there isn't any then fill them until we get those X characters.
print("Payslip for:", name.rjust(10, " "))
print("Salary.....", str(salary).rjust(10, " "))
print("less tax...", str(tax_payable).rjust(10, " "))
print("           ", "-"*10)
print("Take home..", str(pay).rjust(10, " "))