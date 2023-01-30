import csv
import os
import sys

EMPFILE = 'EmployeePay.csv'

infile = open(EMPFILE, 'r', newline = "")

reader = csv.reader(infile)


for row in reader:
    i = 0
    emp_id = row[0]
    first_name = row[1]
    last_name = row[2]
    salary = row[3]
    bonus = row[4]
    i += 1

    print(
        format(emp_id, '<10'), 
        format(first_name, '<14'), 
        format(last_name, '<16'), 
        format(salary, '<14'), 
        format(bonus, '<14')
    )

