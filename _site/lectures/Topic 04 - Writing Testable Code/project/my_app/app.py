import json;

class App:
    def __init__(self, database):
        with open(database) as f:
            self.database = json.load(f)

    @property
    def customers(self):
        return self.database['customers']

    def get_customer(self, id):
        return next(filter(lambda customer: customer['id'] == id, self.customers))

