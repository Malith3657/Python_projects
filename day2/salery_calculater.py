#an employee enter has basic salery of 100000 and receive a bonus of 15000.
#the employee must also pay 12.5% on their gross salary.
#calculate gross salery, tax amount, take home salery.

basic = float(input("basic_salary - "))
bonus = 15000
gross_salary = basic + bonus
tax = 12.5
tax_amount = gross_salary * 12.5 / 100


print(f"gross_salery - {gross_salary}  "
      f"\ntax_amount - {tax_amount}"
      f"\nhome_salery - {gross_salary - tax_amount}")