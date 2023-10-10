from collections import namedtuple

person = namedtuple('Person', ['Name', 'Age'])
details = [person('Kateryna', 37), person('Dmytro', 40), person('Nadia', 17)]

expected_datatypes = (str, int)

for p in details:
    name_valid = isinstance(p.Name, expected_datatypes[0])
    age_valid = isinstance(p.Age, expected_datatypes[1])

    if name_valid and age_valid:
        print(f'Name: {p.Name}, Age: {p.Age}')
    else:
        name_expected = expected_datatypes[0]
        name_actual = p.Name
        age_expected = expected_datatypes[1]
        age_actual = p.Age

        print(f'Warning! Invalid data type. Expected Name: {name_expected}, Actual Name: {name_actual}, Expected Age: {age_expected}, Actual Age: {age_actual}')
