roles = {
    'admin': ['Kateryna', 'Dmytro', 'Nadia'],
    'maintainer': ['Oleksandr', 'Sergiy'],
    'manager': ['Anastasiya', 'Olena'],
    'developer': ['Anton', 'Lubov']
}

user_name = input("Please enter username: ")
user_role = 'guest'

for role, user_list in roles.items():
    if user_name in user_list:
        user_role = role
        break

print(f'Hello, {user_role}')
