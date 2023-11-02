class Worker:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_details(self):
        return f'Name: {self.name}\n' \
               f'Position: {self.position}\n' \
               f'Salary: ${self.salary} per month'

    def promote(self, new_position, salary_increase):
        self.position = new_position
        self.salary += salary_increase


# Example usage:
john = Worker('John Smith', 'Software Engineer', 6000)
print(john.get_details())

# Promote John to a higher position and increase his salary
john.promote("Senior Software Engineer", 1000)
print(john.get_details())
