import csv


infile = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")

csvfile = csv.reader(infile, delimiter=",")

next(csvfile)

outfile.write("Customer Name, Customer Country\n")


for info in csvfile:
    customer_name = info[1] + " " + info[2]
    country = info[4]
    outfile.write(customer_name + ", " + country + "\n")

outfile.close()
infile.close()
