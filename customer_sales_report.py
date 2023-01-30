import csv


infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

csvfile = csv.reader(infile, delimiter=",")

next(csvfile)

outfile.write("Customer | Total\n")

for sales in csvfile:
    customer_ID = sales[0]
    calculated_total = sales[3]
    outfile.write("\t" + customer_ID + " " + "\t" + calculated_total + "\n")

outfile.close()
