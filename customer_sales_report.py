import csv
import os
import sys

CSRFILE = 'sales.csv'

infile = open(CSRFILE, 'r', newline = '')
csvfile = csv.reader(infile, delimiter = ',')
next(csvfile)

outfile = open('salesreport.csv', 'w', newline = '')
writer = csv.writer(outfile, delimiter = ',')
header = ['Customer ID' '\t' 'Calculated Total']
writer.writerow(header)

cust_id = '250'
cust_total = 0


for i in csvfile:
    if cust_id != i[0]:
        outfile.write(cust_id + "\t\t\t" + str("%.2f" % cust_total) + "\n")

        cust_id = i[0]
        cust_total = 0

    total = float(i[3]) + float(i[4]) + float(i[5])
    cust_total += total

outfile.write(cust_id + "\t\t\t" + str("%.2f" % cust_total) + "\n")

outfile.close()
