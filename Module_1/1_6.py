#Accessing Records and Variables Python


# Accessing Variables
age = 25
print("Age:", age)

# Accessing List Elements
numbers = [1, 2, 3, 4, 5]
first_number = numbers[0]
last_number = numbers[-1]
print("First number:", first_number)
print("Last number:", last_number)

# Accessing Dictionary Values
person = {'name': 'John', 'age': 30, 'city': 'New York'}
person_name = person['name']
print("Person's name:", person_name)

# Accessing Tuple Elements
coordinates = (10, 20)
x_coordinate = coordinates[0]
y_coordinate = coordinates[1]
print("X Coordinate:", x_coordinate)
print("Y Coordinate:", y_coordinate)

# Accessing Class Attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_instance = Person(name='Alice', age=25)
print("Person's name:", person_instance.name)
print("Person's age:", person_instance.age)

# Accessing Elements in Nested Data Structures
data = {'person': {'name': 'Bob', 'age': 35, 'city': 'London'}}
person_name = data['person']['name']
print("Person's name:", person_name)
