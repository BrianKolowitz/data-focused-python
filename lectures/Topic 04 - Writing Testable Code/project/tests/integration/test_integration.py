import unittest

from my_app.app import App


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='tests/integration/fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 3)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer['name'], "Org XYZ")
        self.assertEqual(customer['address'], "10 Red Road, Reading")

if __name__ == '__main__':
    unittest.main()