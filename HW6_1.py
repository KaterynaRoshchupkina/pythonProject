from collections import namedtuple

person = namedtuple('Person', ['Name', 'Age'])
details = [person('Kateryna', 37), person('Dmytro', 40), person('Nadia', 17)]

expected_datatypes = (str, int)

for person in details:
    if isinstance(person.Name, expected_datatypes) and isinstance(person.Age, expected_datatypes):
        print(f'Name: {person.Name}, Age: {person.Age}')
    else:
        print(f"Warning! Invalid data type. Expected {expected_datatypes}, Actual Name: {type(person.Name)}, Age: {type(person.Age)}")
