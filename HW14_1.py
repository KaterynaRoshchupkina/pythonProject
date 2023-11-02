class Company:
    def __init__(self, name, industry, headquarters, founded, revenue):
        self.name = name
        self.industry = industry
        self.headquarters = headquarters
        self.founded = founded
        self.revenue = revenue

    def get_details(self):
        return f'Company Name: {self.name}\n' \
               f'Industry: {self.industry}\n' \
               f'Headquarters: {self.headquarters}\n' \
               f'Founded: {self.founded}\n' \
               f'Annual Revenue: ${self.revenue} billion'


# Example usage:
apple = Company('Apple Inc.', 'Technology', 'Cupertino, California', 1976, 394.52)
print(apple.get_details())
