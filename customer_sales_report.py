import csv


infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

csvfile = csv.reader(infile, delimiter=",")

next(csvfile)

outfile.write("Customer | Total\n")

list_1 = []
calc_total = 0
cust_ID_1 = 0


for sales in csvfile:
    customer_ID = int(sales[0])
    subtotal = float(sales[3])
    tax = float(sales[4])
    freight = float(sales[5])

    if customer_ID != cust_ID_1:
        if cust_ID_1 != 0:
            list_1.append([cust_ID_1, calc_total])

        cust_ID_1 = customer_ID
        calc_total = subtotal + tax + freight

    else:
        calc_total += subtotal + tax + freight

for sales in list_1:
    outfile.write("\t" + str(sales[0]) + "\t" + format(sales[1], ">11.2f") + "\n")


outfile.close()
infile.close()
