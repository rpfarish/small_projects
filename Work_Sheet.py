# Python Tutorial for Beginners [Full Course] Learn Python for Web Development

# 1
#print('Ryan Farish')
#print("o----")
#print(" ||||")
#print('*' * 10)


# 2
'''
price = 10
price = 20
rating = 3.4
name = "ahhh"
is_good = True
name = "John Smith"
age = 20
new_patient = True
'''

#3
'''
name = input("What is your name? ")
#print("Hi " + name)
color = input("Enter your favorite color. ")
print(name.capitalize() + " likes " + color.lower() + ".")
'''
#4
'''
from datetime import datetime

my_date = datetime.now()
birth_year = input("Birth Year: ")
def my_age():
    print(my_date.year - int(birth_year))
my_age()
print(type(my_date))
print(type(birth_year))

weight = float(input("Enter your weight(lbs): "))
weight *= 0.453592
print(weight)
'''
# 5
'''
course = "Python for Beginners"
print(course[7:10].upper())
print(course[7:].lower())
print(course[:].lower())
another = course[:]
print(another)
'''
# 6 Formatted String
'''
first = "John"
last = "Smith"
print(first + " "  + last + " is a coder. ")
msg = f"{first} {last} is a coder"
print(msg)
'''
# 7 String Methods
'''
course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.find("n"))
print(course.find("e"))
print(course.replace("for", "with"))
print("Python" in course)
# Title method: converts the first character to Uppercase and remaining to Lowercase
print(course.title())
'''
# 8
# Python uses order of operation
import math
#print(math.pi)
# 9
'''
price = int(input("Enter the house price: "))
has_good_credit = True
down_payment = .10
if has_good_credit:
    down_payment = .1 * price
else:
    down_payment = .2 * price
print(f"Down payment: ${int(down_payment)}")
'''
# 10 Logical Operators
'''
has_good_credit = True
is_criminal = True
if not is_criminal and has_good_credit:
    print("You are eligible for a loan.")
'''
#11 Comparision Operators
'''
temp = 30
if temp == 30:
    print("It's a hot day")
else:
    print("It's not a hot day!")
'''
'''
name = input("Enter your name:")

if len(name) < 3:
    print("Please select a longer name")
elif len(name) > 50:
    print("Please select a shorter name")
else:
    msg = f"Your name: '{name}' looks good!"
    msg = msg.title()
    print(msg)
'''
# 12 Weight Converter
'''
weight = float(input("Enter your weight: "))
unit = input("Enter the unit you want to convert into,\n lbs or kg: ")
lbs_to_kg = 0.453592
kg_to_lbs = 2.20462
if unit == "kg".lower():
    weight *= lbs_to_kg
elif unit == "lbs".lower():
    weight *= kg_to_lbs
print(weight)
'''
# 13 While Loops
'''
i = 0
while i <= 5:
    print('*' * i)
    i += 1
print("Done")
'''
# 14 Guessing Game
'''
secret_num = 9
apple_yay = 0
guess_limit = 3
while apple_yay < guess_limit:
    # Wasn't working bcs of unmatched ()
    guess = int(input("Enter a number: "))
    apple_yay += 1
    if secret_num == guess:
        print("You Win!")
        break
else:
    print("Sorry You Failed :(")
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
'''
# 15 Car Game
cmd = ""
car_start = False
car_stopped = True
while True:
    cmd = input(">").lower()
    if cmd == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")

    elif cmd == "start" and not car_start:
        print("Car stared...Ready to go!")
        car_stopped = False
        car_start = True
    elif cmd == "start" and car_start:
        print("Car already started.")
        car_start = True

    elif cmd == "stop" and car_stopped:
        print("Car already stopped")
    elif cmd == "stop" and not car_stopped:
        print("Car stopped.")
        car_start = False
        car_stopped = True


    elif cmd == "quit":
        print("Bye!")
        break
    else:
        print("I'm sorry I didn't understand.")












