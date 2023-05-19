# Curtis Cheshire
# Student ID: 010713063
# C950 - NHP2
# 5-17-2023

from distance import *
from truck import *
from builtins import ValueError
from package import Package
from hash_table import HashTable

# Reads the package information from package_data.cvs
with open('package_data.csv') as package_csv_file:
    package_csv = list(csv.reader(package_csv_file, delimiter=','))


# Creates package objects from the CSV file and loads them into the hash table. O(n)
# noinspection PyShadowingNames
def load_package_data(filename):
    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')

        for package in package_data:
            package_ID = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_status = package[7]

            package = Package(package_ID, package_address, package_city, package_state, package_zipcode,
                              package_deadline, package_weight, package_status)

            package_hash.insert_into_list(package_ID, package)


# Creates the hash table
package_hash = HashTable()

# Loads the package data into the hash table via the function defined above
load_package_data('package_data.csv')


# "Nearest neighbor" algorithm to determine the delivery order by which package is closest to the current address
# After the closest address is determined, the total milage driven is added up
# The delivery time is also determined and kept track of as the truck moves from address to address
# Finally, the package is delivered from the truck and the algorithm runs again until all packages are delivered
# O(n^3)
# noinspection PyShadowingNames
def nearest_neighbor(truck, mileage, start):
    # Initialization data
    current_address = '4001 South 700 East'
    total_mileage = mileage
    delivery_time = start
    # Initializes the package time_left_hub with the start time of the truck
    for i in truck:
        package = package_hash.search_list(i)
        package.time_left_hub = start
    # Determines the delivery order, updates milage and time, and removes packages from the truck
    while len(truck) > 0:
        start_package = package_hash.search_list(truck[0])
        closest_distance = float(distance_between_addresses(address_number_from_string(current_address),
                                                            address_number_from_string(start_package.address)))
        closest_package_id = truck[0]
        for i in truck:
            next_package = package_hash.search_list(i)
            distance = float(distance_between_addresses(address_number_from_string(current_address),
                                                        address_number_from_string(next_package.address)))
            if distance < closest_distance:
                closest_distance = distance
                closest_package_id = i
        nearest_package = package_hash.search_list(closest_package_id)
        current_address = nearest_package.address
        total_mileage += closest_distance
        delivery_time += datetime.timedelta(hours=closest_distance / 18)
        nearest_package.delivery_time = delivery_time
        truck.remove(closest_package_id)

    return total_mileage


# Gets total mileage between all 3 trucks
mileage1 = nearest_neighbor(first_truck_packages, first_truck_mileage, first_truck_start_time)
mileage2 = nearest_neighbor(second_truck_packages, second_truck_mileage, second_truck_start_time)
mileage3 = nearest_neighbor(third_truck_packages, third_truck_mileage, third_truck_start_time)
total_mileage = mileage1 + mileage2 + mileage3

# This is where the program starts when the user runs the program.
if __name__ == '__main__':
    # Print first line of text along with total mileage
    print(f"\nWelcome to Western Governors University Parcel Service (WGUPS). The total mileage for today's deliveries"
          f" is {total_mileage} miles. Please select an option from the menu below for more information or to "
          f"exit the program. \n")

    exit_program = True
    # Menu of options for the user to select from
    while exit_program:
        print('=' * 75)
        print('1. View all packages and delivery status at a specific time')
        print('2. View a specific package and delivery status at a specific time')
        print('3. Exit the program')
        print('=' * 75)

        # Takes in user selection. If not one of the 3 options, error message pops up and starts over again
        user_input = input('\nPlease enter a numeric option from the menu above: ')

        # Displays all package info according to input time
        if user_input == '1':
            try:
                input_time = input('\nEnter a time to check the status of the packages. (24 hour format: HH:MM:SS): ')
                print('')
                (hrs, mins, secs) = input_time.split(':')
                user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                for i in range(1, 41):
                    package_info = package_hash.search_list(i).package_id
                    package_hub_time = package_hash.search_list(i).time_left_hub
                    package_deadline_time = package_hash.search_list(i).deadline
                    package_delivery_time = package_hash.search_list(i).delivery_time
                    package_address = package_hash.search_list(i).address
                    package_city = package_hash.search_list(i).city
                    package_state = package_hash.search_list(i).state
                    package_zip = package_hash.search_list(i).zipcode
                    if package_hub_time < user_time < package_delivery_time:
                        print(f'Package ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' {package_zip} -- EN ROUTE.')
                    elif user_time < package_hub_time:
                        print(f'Package ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' {package_zip} -- AT HUB.')
                    else:
                        print(f'Package ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' {package_zip} -- DELIVERED at {package_delivery_time}.')
                print('')
            except ValueError:
                print('INVALID ENTRY. Going back to the main menu.\n')
        # Displays 1 package according to input time and package ID
        elif user_input == '2':
            try:
                input_time = input('\nEnter a time to check the status of a package. (24 hour format: HH:MM:SS): ')
                (hrs, mins, secs) = input_time.split(':')
                user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                find_package_by_id = int(input('\nEnter the package ID of the package you wish to view: '))
                if 41 > find_package_by_id > 0:
                    package_info = package_hash.search_list(find_package_by_id).package_id
                    package_hub_time = package_hash.search_list(find_package_by_id).time_left_hub
                    package_deadline_time = package_hash.search_list(find_package_by_id).deadline
                    package_delivery_time = package_hash.search_list(find_package_by_id).delivery_time
                    package_address = package_hash.search_list(find_package_by_id).address
                    package_city = package_hash.search_list(find_package_by_id).city
                    package_state = package_hash.search_list(find_package_by_id).state
                    package_zip = package_hash.search_list(find_package_by_id).zipcode
                    if package_hub_time < user_time < package_delivery_time:
                        print(f'\nPackage ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' {package_zip} -- EN ROUTE.\n')
                    elif user_time < package_hub_time:
                        print(f'\nPackage ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' {package_zip} -- AT HUB.\n')
                    else:
                        print(f'\nPackage ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' {package_zip} -- DELIVERED at {package_delivery_time}.\n')
                else:
                    print('\nINVALID ENTRY. Going back to the main menu.\n')
                    continue
            except ValueError:
                print('\nINVALID ENTRY. Going back to the main menu.\n')
        # Exits the program
        elif user_input == '3':
            exit_program = False
            print('\nThank you for choosing WGUPS. Have a great day!')
            exit()
        else:
            print('\nINVALID ENTRY. Please enter a valid option from the menu.\n')
