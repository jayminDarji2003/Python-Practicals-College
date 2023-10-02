# Create a program name "employee.py" and implement the function DA, HRA, PF, and ITAX.Create another program that uses the function of employee module and calculates gross and salaries of an employee.

# main.py

import employee

# Input employee details
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

# Calculate DA, HRA, and PF using functions from the employee module
da = employee.calculate_da(basic_salary)
hra = employee.calculate_hra(basic_salary)
pf = employee.calculate_pf(basic_salary)

# Calculate Gross Salary
gross_salary = basic_salary + da + hra

# Calculate Income Tax
itax = employee.calculate_itax(gross_salary)

# Calculate Net Salary
net_salary = gross_salary - pf - itax

# Display the results
print("\nEmployee Details")
print("Name:", employee_name)
print("Basic Salary:", basic_salary)
print("Dearness Allowance (DA):", da)
print("House Rent Allowance (HRA):", hra)
print("Provident Fund (PF):", pf)
print("Gross Salary:", gross_salary)
print("Income Tax (ITAX):", itax)
print("Net Salary:", net_salary)
