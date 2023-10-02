# employee.py

def calculate_da(basic_salary):
    da_percentage = 0.12  # Dearness Allowance is typically 12% of basic salary
    da = basic_salary * da_percentage
    return da

def calculate_hra(basic_salary):
    hra_percentage = 0.20  # House Rent Allowance is typically 20% of basic salary
    hra = basic_salary * hra_percentage
    return hra

def calculate_pf(basic_salary):
    pf_percentage = 0.10  # Provident Fund is typically 10% of basic salary
    pf = basic_salary * pf_percentage
    return pf

def calculate_itax(gross_salary):
    # Simplified Income Tax calculation (adjust as per your country's tax rules)
    income_tax_percentage = 0.15
    itax = gross_salary * income_tax_percentage
    return itax
