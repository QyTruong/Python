import glob
import csv
import datetime
from time import localtime
from collections import defaultdict


# 5 Function
def greet(name):
    print("Hello, " + name)

# 14 Classes
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            amount = self.balance
        self.balance -= amount

# 15 Csv
def cmp(a, b):
    return (a > b) - (a < b)

if __name__ == '__main__':
    choice = input("Your choice: ")

    match choice:
        case "1":
            # Output
            print('Hello, world!')

        case "2":
            # Input
            name = input("What is your name?\n")
            print('Hi, %s.' % name)

        case "3":
            # For loop
            friends = ['john', 'pat', 'gary', 'michael']
            for i, name in enumerate(friends):
                print("iteration {iteration} is {name}".format(iteration=i, name=name))

        case "4":
            # Tuple assignment
            parents, babies = (1,1)
            while babies < 100:
                print('this, generation has {0} babies'.format(babies))
                parents, babies = (babies, parents + babies)

        case "5":
            # Functions
            greet('Jack')
            greet('Jill')
            greet('Bob')

        case "6":
            #List
            my_list = ['abc', 34, True, 40, 'male']

            print(f'Initial list: {my_list}')

            my_list.append(99)
            print(f'List after appending: {my_list}')

        case "7":
            # Dictionary
            this_dict = {
                'brand' : 'Ford',
                'model' : 'Mustang',
                'year' : 1964,
            }
            print(this_dict)

        case "8":
            # Dictionaries, generator expressions
            prices = {'apple' : .4, 'banana' : .5}
            my_purchase = {
                'apple' : 1,
                'banana' : 6,
            }
            grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
            print('I owe the grocer $%.2f' % grocery_bill)

        case "9":
            # Tuple
            this_tuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
            print(this_tuple)

        case "10":
            # Sets
            this_set = {'apple', 'banana', 'cherry', False, True, 0}
            print(this_set)

            this_set.add('orange')
            print(this_set)

            this_set.remove('banana')

            print(this_set)

        case "11":
            # Glob
            python_files = glob.glob('*.txt')
            for file_name in sorted(python_files):
                print('   -------' + file_name)

                with open(file_name) as f:
                    for line in f:
                        print('   ' + line.rstrip())
                print()

        case "12":
            # Time, conditionals, from...import, for...else
            activities = {
                8 : 'Sleeping',
                9 : 'Commuting',
                17 : 'Working',
                18 : 'Commuting',
                20 : 'Eating',
                22 : 'Resting'
            }

            time_now = localtime()
            hour = time_now.tm_hour
            print(hour)

            for activity_time in activities:
                if hour < activity_time:
                    print(activities[activity_time])
                    break
            else:
                print('Unknown, AFK or sleeping!')

        case "13":
            # while loop
            REFRAIN = '''
            %d bottles of beer on the wall,
            take one down, pass it around,
            => %d bottles of beer on the wall,
            '''

            bottles_of_beer = 9
            while bottles_of_beer > 1:
                print(REFRAIN % (bottles_of_beer, bottles_of_beer - 1))
                bottles_of_beer -= 1

        case "14":
            # Classes
            my_account = BankAccount(15)
            my_account.withdraw(50)
            print(my_account.balance)

        case "15":
            # Csv
            with open('uni.csv', 'w', newline='') as fw:
                writer = csv.writer(fw)
                writer.writerows([
                    ['BKU', 'Bach Khoa University', 27.5, 0.5],
                    ['HCMUS', 'University of Science', 27.0, -0.5],
                    ['OU', 'Open University', 25.5, 0.5],
                ])
            with open('uni.csv', 'r', newline='') as fr:
                unis = csv.reader(fr)

                status_labels = {
                    -1 : 'down',
                    0 : 'unchanged',
                    1 : 'up'
                }

                for ticker, name, mark, change in unis:
                    status = status_labels[cmp(float(change), 0.0)]
                    print(f'{ticker} | {name} | {mark} | {change} | {status}')

        case "16":
            #defaultdict
            d = defaultdict(list)
            print(d)

            d['fruits'].append('mango')
            d['vegetables'].append('banana')
            print(d)

            print(d['juices'])

            d = defaultdict(int)
            print(d)
            print(d['a'])



