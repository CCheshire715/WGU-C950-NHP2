import datetime

# Manually load each truck with packages according to the deadline and special notes
# IDs of packages that have to be delivered early (leaves at 8:00)
first_truck_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
first_truck_mileage = 0.0
first_truck_start_time = datetime.timedelta(hours=8)

# IDs of packages that are delayed or are required to be on truck 2 (leaves at 9:10)
second_truck_packages = [3, 6, 18, 25, 28, 32, 33, 35, 36, 38, 39]
second_truck_mileage = 0.0
second_truck_start_time = datetime.timedelta(hours=9, minutes=10)

# IDs of packages that are EOD delivery or wrong address (leaves at 10:25)
third_truck_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]
third_truck_mileage = 0.0
third_truck_start_time = datetime.timedelta(hours=10, minutes=25)
