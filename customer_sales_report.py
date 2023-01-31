import csv


infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

csvfile = csv.reader(infile, delimiter=",")

next(csvfile)

outfile.write("Customer | Total\n")


for sales in csvfile:
    customer_ID = int(sales[0])
    subtotal = float(sales[3])
    tax = float(sales[4])
    freight = float(sales[5])
    calc_total = subtotal + tax + freight
    outfile.write("\t" + str(customer_ID) + "\t" + str(calc_total) + "\n")


outfile.close()
infile.close()
