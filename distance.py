import csv

# Reads the distance information from distance_data.csv
with open('distance_data.csv') as distance_csv_file:
    distance_csv = list(csv.reader(distance_csv_file, delimiter=','))

# Reads the address information from address_data_csv
with open('address_data.csv') as address_csv_file:
    address_csv = list(csv.reader(address_csv_file, delimiter=','))


# Function to get the floating point distance between two points in the distance_data.csv file. O(1)
def distance_between_addresses(x, y):
    distance = distance_csv[x][y]
    if distance == '':
        distance = distance_csv[y][x]
    return float(distance)


# Function to return the address number from the address string literal. O(n)
def address_number_from_string(address):
    for i in address_csv:
        if address in i[2]:
            return int(i[0])
