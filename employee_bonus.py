import csv


def main():
    employee = open("EmployeePay.csv", "r")
    if employee.mode == "r":
        bonus = employee.read()
        print(bonus)


main()
