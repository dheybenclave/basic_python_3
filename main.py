import asyncio
from builtins import *
from operator import *
from common.file_handling import *
from student import Student
from question import Question
from activities import Activities, Course


# ASYNC

async def callbacks():
    print("asdasdsa")
    print("last text")

async def asd(callback):
    print("dssd")
    await asyncio.sleep(0)
    task = asyncio.create_task(callback)
    await task



asyncio.run(asd(callbacks()))

# INHERITANCE

student1 = Student("Dheo Clavera", "BSCS", "3", True, False)
activities = Activities(student1.name, student1.major, student1.gpa, student1.is_probation, student1.is_pass)
my_logger(activities.sport())


course_student = Course("John Doe", "BSBA", "3", True, False)

my_logger(course_student.get_major())
course_student.set_major("CSP")
my_logger(course_student.get_major())

# CLASS AND OBJECT


student1 = Student("Dheo", "Computer Science", "3", True, False)
student2 = Student("Ella", "Business", "4", True, False)

my_logger(f'Name: {student1.name} | Dean Lister? : {student1.on_dean_list()}')

# MULTIPLE QUIZ

question_lists = [
    "What is the color of apple? \n (a) Green\Red \n(b) Pink \n(c) Gray\nAnswer : ",
    "What is the color of sky? \n (a) Blue \n(b) Pink \n (c) Gray \nAnswer : ",
    "What is the color of Sun? \n (a) Green\Red \n(b) Yellow \n(c) Black \nAnswer : ",
    "What is the color of Leaves? \n (a) Green\Red \n(b) Pink \n(c) Gray \nAnswer : "
]

questions = [
    Question(question_lists[0], "a"),
    Question(question_lists[1], "b"),
    Question(question_lists[2], "a")
]


def run_test(question_list):
    score = 0
    for question in question_list:
        answer = input(question.prompts)
        if answer == question.answer:
            score += 1
    my_logger(f'You got {str(score)} / {str(len(question_list))} Correct')


run_test(questions)


try:

    my_logger("\n**CREATE FILE**")
    create_files(input("Enter File Name  : "), input("Enter Extension File : "), input("Enter Message Body : "))

    my_logger(f'\n**READ FILE**')
    read_in_files(input("Enter File Name Path with Extension : "))

    my_logger("\n**APPEND/ADD IN FILE**")
    write_in_files(input("Enter File Name Path with Extension : "), input("Enter Row Value : "))

    my_logger("\n**UPDATING VALUE IN FILE**")
    update_value_in_files(input("Enter File Name with Extension : "), int(input("Enter Row Index Line : ")), input("Enter Message Body : "))

    my_logger("\n**DELETE VALUE IN FILE**")
    delete_value_in_files(input("Enter File Name with Extension : "), int(input("Enter Row Index Line : ")))

    my_logger("\n**COPY FILE**")
    copy_file(input("Enter Source File Path with File Name and Extension : "), input("Enter Destination File Path without File Name: "), input("Enter File Name: "))

    my_logger("\n**MOVE FILE**")
    move_file(input("Enter Source File Path with File Name and Extension : "), input("Enter Destination File Path without File Name: "))

    my_logger("\n**DELETE FILE**")
    delete_file(input("Enter Source File Path with File Name and Extension : "))


except FileExistsError:
    my_logger(FileExistsError)


# BUILD TRANSLATOR | REPLACE | CONVERT

def translator(phrase):
    _translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            _translation = _translation + "d"
        else:
            _translation = _translation + letter

    return _translation.capitalize()


input_translator = input("Enter a word to translate : ")
my_logger(translator(input_translator))

# 2D List and NESTED LOOPS

list_of_number = [  # 2D List is auto sorted
    [4, 5, 6, 7, 1],
    [12, 64, 15, 616],
    [125],
]

my_logger(f'get specfic row cols: {list_of_number[1][2]}')

for row1 in list_of_number:
    for cols in row1:
        print(cols)


# CALCULATOR # FOR LOOP #TRY EXCEPT

def calculate(num1, ops, num2):
    list_of_operators = {
        "+": add(num1, num2),
        "-": sub(num1, num2),
        "*": mul(num1, num2),
        "/": floordiv(num1, num2)
    }

    for key, value in list_of_operators.items():
        if ops == key:
            my_logger(f'Answer : {num1} {ops} {num2} = {round(value) if str(value).split(".")[1] == "0" else value}')


try:
    input_num1 = float(input("Enter First Number : "))
    operator = input("Enter Operator : ")
    input_num2 = float(input("Enter Second Number : "))

    calculate(input_num1, operator, input_num2)

except ZeroDivisionError as err:
    my_logger(f'Invalid Input ZeroDivisionError:  {err} ')
except ValueError as err:
    my_logger(f'Invalid Input ValueError: {err} ')


# IF  [> , < , = , >= , <= , !=,]

def max_num(num1, num2, num3):
    my_logger(f'{num1} is {"" if (num1 >= num2 and num1 >= num3) else "not"} the biggest number')


max_num(1, 2, 3)

# IF STATEMENT
is_male = True
is_pinoy = False

if is_male:
    my_logger("You are Male")
if is_male and is_pinoy:
    my_logger("You are Male with Pinoy Pride")
elif is_male and not is_pinoy:
    my_logger("You are Male is your not pinoy hehe")
else:
    my_logger("You are female or Not Pinoy")


# FUNCTIONS
def deduct_tax(based_salary):
    compute = float(based_salary * 0.88)
    my_logger(f' Your take home salary : {compute}')


get_based_salary = float(input("Enter Salary : "))
deduct_tax(get_based_salary)

# TUPLES = is static variable, cannot change
coordinates = (3, "asd")
# coordinates[1] = 123
print(coordinates[1])

# LIST
listOfName = ["Dheo", "Bensurto", "Claveria"]
completeName = ["First Name", "Middle Name", "Surname"]

completeName.insert(0, "Mr")
# completeName.remove.txt("Mr")

copyName = listOfName.copy()
copyName.reverse()
print(f'You information is {listOfName} | \n {copyName} \n')

# INPUT AND VARIABLES
inputName = input("Enter Name : ")
inputSalary = float(input("Enter Salary : "))
inputAge = input("Enter Age : ")
inputGender = input("Are you Male ? Y or N : ")

tax = int(inputSalary) * 0.12
afterTaxSalary = int(inputSalary) - tax

print(
    f'\nMy name, {inputName}, my first name is "{inputName.split(" ")[0]}" \n'
    f'I\'m {inputAge} yrs old \n'
    f'You are {"Male" if ["Y", "Yes", "YES"].__contains__(inputGender) else "Female"} \n'
    f'and my before tax salary is {inputSalary} \n'
    f'after the tax deduction with tax value {tax}  \n'
    f'my take home salary will be {round(afterTaxSalary)} \n')


def print_hi(name1):
    # Use a breakpoint in the code line below to debug your script.
    if name1 == "Dheo Claveria":
        name1 = "Dhey"

    print(f'Hi, {name1}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(inputName)
