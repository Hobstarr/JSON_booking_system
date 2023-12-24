import os
from uuid import uuid4
import json
import pandas as pd

class Customer:
    '''
    creates a customer with name and age
    and allows you to manipulate their data
    and store it in .json file format.
    :param: name: the customers name
    :param: age : the customers age
    '''
    def __init__(self, name, age):
        self.user_id = str(uuid4()).split('-')[4]
        self.name = name
        self.age = age
        self.comments_dict = {}

    def add_comments(self, new_comment):
        comments_length = len(self.comments_dict)
        self.comments_dict[(str(comments_length))] = new_comment

    def save(self):
        json_data = {'user_id':self.user_id, 
                'name':self.name,
                'age':self.age,
                'comments': self.comments_dict}
        
        with open(f'customers/{str(self.user_id)}.json', 'w') as f:
            json.dump(json_data, f)

    def print_comments(self):
        comments_length = len(self.comments_dict)
        name = self.name

        print(f'\n{name} has made {comments_length} comments:')
        print(f'-----')
        for i, dict_key in enumerate(self.comments_dict):
            print(f'{i+1}: {self.comments_dict[dict_key]}')


def new_customer(name, age):
    return Customer(name, age)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_all_customers(method = 'plain'):
    fileList = []
    for filename in os.listdir('customers/'):
        if filename.endswith('.json'):
            fileList.append(os.path.join('customers/', filename))

    customer_list = []
    for file in fileList:
        with open(file, encoding='utf-8', mode='r') as currentFile:
            data = json.load(currentFile)

            name = data['name']
            age = data['age']
            user_id = data['user_id']
            comments = data['comments']

            customer_loaded = Customer(name, age)
            customer_loaded.comments_dict = comments
            customer_loaded.user_id = user_id
            customer_list.append(customer_loaded)

    return customer_list

def print_all_customers(method = 'plain'):
    fileList = []
    for filename in os.listdir('customers/'):
        if filename.endswith('.json'):
            fileList.append(os.path.join('customers/', filename))

    if method == 'plain':
        print(f"\n\nPrinting all entries in '{bcolors.OKGREEN}customers/{bcolors.ENDC}'")
        for file in fileList:
            with open(file, encoding='utf-8', mode='r') as currentFile:
                data = json.load(currentFile)
                print(f'------'
                f"\t{bcolors.FAIL}user_id:{bcolors.ENDC} {data['user_id']}\n" +
                f"\tname: {data['name']}\n" +
                f"\tage: {data['age']}\n")

    if method == 'dataframe':
        df = pd.DataFrame()
        user_ids = []
        names = []
        ages = []

        for file in fileList:
            with open(file, encoding='utf-8', mode='r') as currentFile:
                data = json.load(currentFile)
                user_ids.append(data['user_id'])
                names.append(data['name'])
                ages.append(data['age'])

        df['user_id'] = user_ids
        df['name'] = names
        df['age'] = ages
        print(df)

def find_customers(search_term, search_domain):
    fileList = []
    for filename in os.listdir('customers/'):
        if filename.endswith('.json'):
            fileList.append(os.path.join('customers/', filename))

    print(f"\n\nSearching for '{search_term}' in '{bcolors.OKGREEN}customers/{bcolors.ENDC}'")
    for file in fileList:
        with open(file, encoding='utf-8', mode='r') as currentFile:
            data = json.load(currentFile)
            if search_term.lower() in data[search_domain].lower():
                print(f'------'
                    f"\t{bcolors.FAIL}user_id:{bcolors.ENDC} {data['user_id']}\n" +
                    f"\tname: {data['name']}\n" +
                    f"\tage: {data['age']}\n")
                
def load_customer(user_id):
    print(str(user_id))
    file = os.path.join('customers/', f'{str(user_id)}.json')
    print(file)
    with open(file, encoding='utf-8', mode='r') as currentFile:
        data = json.load(currentFile)
        name = data['name']
        age = data['age']
        comments = data['comments']

        customer_loaded = Customer(name, age)
        customer_loaded.comments_dict = comments
        customer_loaded.user_id = user_id

        return customer_loaded

if __name__ == '__main__':
    john = new_customer('John Doe', 25)
    john.add_comments('This was a great trip')
    john.add_comments('Would not recommend')
    john.add_comments('Excellent!')
    john.print_comments()
    john.save()

    find_customers('john', 'name')

    import numpy as np
    from faker import Faker
    fake = Faker()
    import random

    for i in range(20):
        new_cust = new_customer(fake.name(), int(np.random.normal(40, 7)))
        for i in range(0,random.randint(0,10)):
            new_cust.add_comments(fake.text()[0:30])
        new_cust.save()

    print_all_customers()





