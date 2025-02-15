import csv
import os
import sys

#File Names
CUSTFILE = 'customers.csv'


infile = open(CUSTFILE, 'r', newline = '')

csvfile = csv.reader(infile, delimiter =',')

outfile = open('customer_country.csv', 'w', newline = '')
next(csvfile)

writer = csv.writer(outfile)
header = ['Customer Name', 'Country']
writer.writerow(header)
i = 0


for row in csvfile:
    first_name = row[1]
    last_name = row[2]
    country = row[4]

    data = [[first_name + ' ' + last_name, country]]

    writer.writerows(data)
    i += 1


print(i)
outfile.close()

#print(format(first_name, '<14s'), format(last_name, '<16s'), format(country, '<14s'))


