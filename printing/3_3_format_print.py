cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passangers / cars_driven


print("There are", cars, "cars available.")
print("There are only ", drivers, "drivers available")
print("There will be", cars_not_driven,  "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("we have",passangers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# before Python 3.7 formating using .format() method:
# print("There are {} cars available.".format(cars))
# print("There are only {} drivers available".format(drivers))
# print("There will be {} empty cars today.".format(cars_not_driven))
# print("We can transport {} people today.".format(carpoo_capacity))
# print("we have {} to carpool today.".format(passengers))
# print("We need to put about {} in each car.".format(average_passengers_per_car))


# After Python 3.7 new format String 'f':

# print(f"There are {cars} cars available.")
# print(f"There are only {drivers} drivers available")
# print(f"There will be {cars_not_driven} empty cars today.")
# print(f"We can transport {carpool_capacity} people today.")
# print(f"we have {passangers} to carpool today.")
# print(f"We need to put about {average_passengers_per_car} in each car.")


# Old formating with %:
name = 'Dilshad'
age = 37
print('Hi, My name is %s and I am %d years old.' % (name, age))