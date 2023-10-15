family = {
    'grandpa': ('Alex', 76),
    'grandma': ('Nona', 74),
    'dad': ('Greg', 48),
    'mom': ('July', 45),
    'son_older': ('Bob', 18),
    'son_middle': ('Alex', 15),
    'son_young': ('Mark', 10)
}
min_age = max_age = family[list(family.keys())[0]][1]
for member, (name, age) in family.items():
    if age < min_age:
        min_age = age
    if age > max_age:
        max_age = age
age_difference = max_age - min_age
print(f'The age difference between the oldest and youngest family member is {age_difference} years')
