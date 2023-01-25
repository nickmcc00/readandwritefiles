import csv


def main():
    customers = open("customers.csv", "r")
    if customers.mode == "r":
        contents = customers.read()
        print(contents)


main()
