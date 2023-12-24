import os
import unittest
import json

from main import Customer, new_customer, print_all_customers

class TestMain(unittest.TestCase):
    def test_new_customer_json_fields_success(self):
        new_cust = new_customer('new_person', '35')
        
        filename = os.path.join('customers/', f'{new_cust.user_id}.json')
        with open(filename, encoding='utf-8', mode='r') as file:
            data = json.load(file)

        self.assertEqual(data['name'], 'new_person')
        self.assertEqual(data['age'], '35')
        
print_all_customers('plain')