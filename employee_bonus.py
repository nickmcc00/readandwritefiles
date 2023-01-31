import csv


infile = open("EmployeePay.csv", "r")

csvfile = csv.reader(infile, delimiter=",")


for data in csvfile:
    print(data)


infile.close()
