# Creates the package class
class Package:

    # Initializes package object. O(1)
    def __init__(self, package_id, address, city, state, zipcode, deadline, mass, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass
        self.status = status
        self.time_left_hub = None
        self.delivery_time = None

    # Prints package object information. O(1)
    def __str__(self):
        return f'{self.package_id}, {self.address}, {self.city}, {self.state}, {self.zipcode}, {self.deadline},' \
               f' {self.delivery_time}'
