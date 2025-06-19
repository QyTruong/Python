
friends = ['john', 'pat', 'gary', 'michael']
mylist = ['abc', 40, True, 40, "male"]

def greet(name):
    print("hello", name)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

prices = {'apple': .4, 'banana': .5}
my_purchase = {
    'banana': 6,
    'apple': 1,
}

grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)

thistuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
thistuple2 = (1,1,1)

thisset = {'apple', 'banana', 'cherry', False, True, 0}


import glob

from time import  localtime
import datetime

activities = {
    8: 'Sleeping',
    9: 'Commuting',
    17: 'Working',
    18: 'Commuting',
    20: 'Eating',
    22: 'Resting'
}

REFRAIN = '''
%d bottles of beer on the wall,
take one down, pass it around,
=> %d bottles of beer on the wall!
'''
bottles_of_beer = 9

class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def widthdraw(self, amount):
        if (amount > self.balance):
            amount = self.balance
        self.balance -= amount

import csv
def cmp(a, b):
    return (a > b) - (a < b)

if __name__ == '__main__':
    with open('uni.csv', 'w', newline='') as unisFileW:
        writer = csv.writer(unisFileW)
        writer.writerows([
            ['BKU', 'Bach Khoa University', 27.5, 0.5]
            ['HCMUS', 'University of Science', 27.0, -0.5]
            ['OU', 'Open University', 25.5, 0.5]
        ])
    exit(0)

    my_account = BankAccount(15)
    my_account.widthdraw(50)
    print(my_account.balance)
    exit(0)

    while bottles_of_beer > 1:
        print(REFRAIN % (bottles_of_beer, bottles_of_beer - 1))
        bottles_of_beer -= 1
    exit(0)

    time_now = localtime()
    hour = time_now.tm_hour
    print(hour)

    for activity_time in sorted(activities.keys()):
        if hour < activity_time:
            print(activities[activity_time])
            break
    else:
        print('Unknown, AFK or Sleeping')
    exit(0)

    python_files = glob.glob('*.txt')

    for file_name in sorted(python_files):
        print('  ------' + file_name)

        with open(file_name) as f:
            for line in f:
                print("   " + line.rstrip())
    exit(0)


    print(thisset)
    thisset.add('orange')
    print(thisset)
    thisset.remove('banana')
    print(thisset)
    exit(0)

    print(thistuple.__add__(thistuple2))
    exit(0)

    print('I own the grocer $%s' % grocery_bill)
    exit(0)

    print(thisdict)
    exit(0)

    print(f'Initial list: {mylist}')
    mylist.append(99)
    print(f'List after appending: {mylist}')
    exit(0)

    greet('Truong');
    exit(0)

    parents, babies = (1,1)
    while babies < 100:
        print(f'this generation has {babies}')
        parents, babies = (babies, parents + babies)
