import csv


infile = open("EmployeePay.csv", "r")

csvfile = csv.reader(infile, delimiter=",")

# next(csvfile)

if infile.mode == "r":
    pay = infile.read()
    print(pay)
