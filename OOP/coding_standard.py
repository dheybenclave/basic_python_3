import time
from collections import OrderedDict

from common.common_global import my_logger
import functools

my_logger("=============================================================")
'''
TIME MANIPULATION
'''

time_object = time.localtime()
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
my_logger(local_time)

time_input = "January 12, 1998"
time_object_input = time.strptime(time_input, "%B %d, %Y")
local_time_input = time.strftime("%B %d %Y %H:%M:%S", time_object_input)
my_logger(local_time_input)


my_logger("=============================================================")
'''
ZIP FUNCTION  = CONVERT TO TUPLES AND OBJECT
'''

usernames = ["john", "doe", "susan", "baker"]
passwords = ["123", "pass123", "ssap321"]
last_login = ["1/1/2001", "1/1/2121", "1/1/2032"]

users = zip(usernames, passwords, last_login)
for i in users:
    my_logger(f'ZIP : {i}')


my_logger("=============================================================")
'''
COMPREHENSION
LIST
DICTIONARY
'''
cities_covid = {
    'Navotas': 330,
    'Malabon': 150,
    'Caloocan': 1000,
    'Valenzuela': 200
}
sort_cities_by_most_number_covid =sorted(cities_covid.items(), key=lambda item: item[1], reverse=True)


def get_result(value):
    value = f'is under quarantine CASES: {value}' if (value > 300) else 'can go around CAMANAVA CASES: {value}'
    return value

check_covid_result = {
    key: get_result(value)
    for key, value in sort_cities_by_most_number_covid  # loop the cities
}
my_logger(check_covid_result)

''' #SIMPLY WITHOUR DICTIONARY COMPREHENSION
for key, value in sort_cities_by_most_number_covid:
    my_logger(
        f'{key} : is under quarantine CASES: {value}'
        if (value > 300) else
        f'{key} can go around CAMANAVA CASES: {value}'
    )
'''


my_logger("=============================================================")

students_grades = [
    ("Dheo", 70),
    ("John", 91),
    ("Doe", 80),
    ("Baker", 74),
    ("Susan", 85),
]

#passed_grades = list(filter(lambda x: x >= 75, students_grades)) #filter with lambda
#passed_grades = [i for i in students_grades if i >= 75]  #can also filter with  if condition loop

evaluate_grades = [  #can also filter with passed if else condition loop
    f'{i[0]} is PASSED with grade {i[1]}' if i[1] >= 75 else f'{i[0]} FAILED is with grade {i[1]}'
    for i in students_grades ]

show_result = lambda datas : list(map(print, datas))
my_logger(show_result(evaluate_grades))

my_logger("=============================================================")
''''
MAP
FILTER
REDUCE
'''
factorial = [5,12,7,21,1] #multiply itself by index 1 and 2 until end
result =functools.reduce(lambda x, y: x * y , factorial)
my_logger(f'Factorials result: {result}')

word_to_covert = "Dheo Claveria"
my_logger(f'after before  list {word_to_covert}')

letters = list(filter(lambda c: c != " ", word_to_covert))  # remove space
# letters = list(word_to_covert.replace(" ","")) #remove space also
my_logger(f'after converting list {letters}')

# repeatative perform for index 1 and 2 until end
words_to_reduce = functools.reduce(lambda x, y: x + y , letters)

my_logger(f'after reducing the list {words_to_reduce}')

my_logger("=============================================================")
friends = [
    ("dheo", 20),
    ("claveria", 17),
    ("bensurto", 25)
]
legal_age = lambda age: age[1] >= 18

drinking_buddies = list(filter(legal_age, friends))
for i in drinking_buddies:
    my_logger(f'Filter Function : {i}')

my_logger("=============================================================")
store = [
    ("shirt", 14.00),
    ("dress", 124.50),
    ("shorts", 50.00)
]

to_euros = lambda data: (data[0], round(data[1] * 0.82))

store_euros = map(to_euros, store)
printer = lambda msg: my_logger(f'Message for Map Conversion {msg}')
show_map_list = lambda map_list: list(map(printer, map_list))

show_map_list(store_euros)
my_logger("=============================================================")

'''
Sort
'''

abc = ("d", "a", "b", "e", "x", "y", "p")  # tuples = tuples is static variables

sorted_abc = sorted(abc)

my_logger(sorted_abc)

for x in sorted_abc:
    my_logger(f' sorted : {x}')

abc_2d = [
    ("dheo", 3, True),
    ("bensurto", 1, True),
    ("claveria", 5, False),
]

sorted_abc_2d = sorted(abc_2d)

salary = lambda salaries: salaries[1]  # will return the 2nd params of abc_2d tuples list [3,1,5]

sorted_abc_2d.sort(key=salary)  # set what will be the key to sort

for x in sorted_abc_2d:
    my_logger(f' sort with and 2d tuples : {x}')

sorted_abc_2d_reverse = sorted(abc_2d)
sorted_abc_2d_reverse.sort(key=salary, reverse=True)  # set what will be the key to sort and reverse

for x in sorted_abc_2d_reverse:
    my_logger(f' sort with and 2d tuples and reverse: {x}')

sorted_abc_2d_iterable = sorted(abc_2d, key=salary)

for x in sorted_abc_2d_iterable:
    my_logger(f' sorted with and 2d tuples : {x}')

my_logger("=============================================================")

printer = lambda s : my_logger(f'loop inside lambda {s}')

loop = lambda sort_list : list(map(printer, sort_list))

loop(sorted_abc_2d_iterable)
my_logger("=============================================================")

loop(sorted_abc_2d_reverse)

my_logger("=============================================================")

'''
Lambda : = lamba parameter : expression
variable will become method with parameter provided and set in the lambda expression
use the lambda for quick return function with params needed
'''

# set x as parameter of object
double = lambda x: x * 2
my_logger(f'lambda double :  {double(3)}')

# set x and y  as parameter of object
multiply = lambda x, y: x * y
my_logger(f'lambda multiply:  {multiply(3, 2)}')

full_name = lambda fname, lname: f'Full Name {fname} {lname}'
my_logger(f'lambda full_name : {full_name("Dheo", "Claveria")}')

age_check = lambda age: "You're old" if age >= 18 else "You're minor"
my_logger(f'lambda age :  {age_check(18)}')

my_logger("=============================================================")
'''
high order function
'''


def divisor(x):
    def divident(y):
        return x / y

    return divident


div = divisor(12)
my_logger(f'divide set params {int(div(2))}')

my_logger("=============================================================")

'''
assign function to variable
best way to async
'''

my_logger("=============================================================")


def function_with_function_aguments(pass_function):
    change_value = "change value"

    if callable(pass_function):
        pass_function()
    else:
        my_logger(f'not a function | Value: "{pass_function}"')

    my_logger(f'Call this function function_with_function_aguments')


def helloworld():
    my_logger("Hello World")


pass_hello = helloworld
not_function = "string variable to"

function_with_function_aguments(pass_hello)
function_with_function_aguments(not_function)

my_logger("=============================================================")
'''
Warlus operations = assignment expression
is repeated 
'''
my_logger("=============================================================")
numbers = [2, 8, 0, 1, 1, 9, 7, 7]

description = {
    "length": (num_length := len(numbers)),  # repeat it self checking the length
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_length,
}
my_logger(description)
my_logger(sum(numbers))

my_logger("=============================================================")

cities = ["Vancouver", "Oslo", "Houston", "Warsaw", "Graz", "Holguín"]

# witnesses = [city for city in cities if city.startswith("H")]


# my_logger
if any((witness := city).startswith("H") for city in cities):
    print(f"{witness} starts with H")
else:
    print("No city name starts with H")

my_logger("=============================================================")
foods = list()

#    get the input value of user and check if the input is not equal to "quit" return bool
while food := input("What food you like? :") != "quit":
    foods.append(food)


if __name__== '__main__':
    pass