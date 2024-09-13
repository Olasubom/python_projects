import random
import sys
import math
import string

# LEARNING TO USE OF PRINT
first_name ="adebayo"
last_name = " olashubomi"
full_name = first_name + last_name
print(full_name)

print("")

username ="olashubomi32"
domain ="gmail.com"
email = username + "@" +domain
print(email)

print("")

greetings ="Hello,"
name =" Alice"
exclamation ="!"
full_greetings = greetings + name + exclamation
print(full_greetings)

print("")

day ="20"
month ="/july"
year ="/2024"
ddmmyy = day + month + year
print(ddmmyy)

print("")

dog_name="pudding"
# UNDERSTANDING FUNCTION
def name():
    dog_name="bulldog"
    print("this is a " + dog_name)

name()
print("this is a " + dog_name)

print("")


line01= "****************"
line02= "*              *"
line03= "***  Thanks  ***"

print("")
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)



# FIRST TRIA FOR FIRST GAME//
player_one = input("input any number ")
player = int(player_one)

if (player < 1 or player > 3):
    sys.exit("you have exceeded the limit of numbers")


player_two = random.choice("123")
computer = int(player_two)

print("")
print("the point of player is  " + str(player) + "!")
print("the point of computer is " + str(computer) + "!")

if (player == 1 and computer ==  3):
    print("YOU WIN!!!")
elif (player == 2 and computer == 1):
    print("YOU WIN!!!")
elif (player == 3 and computer == 2):
    print("YOU WIN!!!")
elif (player == computer ):
    print("IT A TIE!!!")
else:
    print("COMPUTER WINS!!!")      

# PUTTING THE GAME IN A FUNCTION//
def game():
    player_one = input("input a number 1-3 ")
    player = int(player_one)

    if (player < 1 or player > 3):
        return game()  

    player_two = random.choice("123")      
    computer = int(player_two)

    print("")
    print("the point of player " + str(player) + "!")
    print("the point of computer " + str(computer) + "!")

    if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print("YOU WIN🥳😎")
    elif player == computer:
        print("IT A TIE😱😱")
    else:
        print("COMPUTER WON💀🤖")

    print("play again⁉")

    while True:
        play_again = str(input("\n Y for yes \n Q for quit\n")).lower()
        if play_again not in ["y" , "q"]:
            print("input is not 'Y' or 'Q'")
            continue
        else:
            break
    if play_again == "y":
        return game()
    else:
        print("THANKS FOR PLAYING😁")
        sys.exit("BYE😭😭")      

game()

print("")       
# SOLVING A PROBLEM 
# write a conditional statement to show the relationship between two value
# x=25,y=5
# conditions: x is greater than y,x is divisible by y,is the modulos  of y, x is less than y (and /or) 

x = 25
y = 2

if ((x > y and x / y) or (x % y or x  < y)):
    print("condition has been met")
elif x == y:
    print("x and y are equal")
else:
    print("condition not met")  

print("")       

# first calculator built in a function
def calculator():
    number_one = float(input("input the first number: "))
    number_two = float(input ("input the second number: "))

    
    print("choose an operator")
    print("1. addition (+)")
    print("2. subtraction (-)")
    print("3. division (/)")
    print("4. multiplication (*)")
    print("5. exponetial (**)")

    operator = input("enter the operator you need ")

    if operator == "1":
        result = number_one + number_two
        print(f"your  answser for {number_one} + {number_two} = {result} ")
    elif operator == "2":
        result = number_one - number_two
        print(f"your answer for {number_two} - {number_one} =  {result} ")
    elif operator == "3":
        result = number_one / number_two
        print(f"your answer for {number_one} / {number_two} = {result} ")
    elif operator == "4":
        result = number_one * number_two
        print(f"your answer for  {number_one} * {number_two} = {result}")
    elif operator == "5":
        result = number_one ** number_two
        print(f"your answer for {number_one} ** {number_two} = {result}")
    else:
        print("choose a valid operator")

calculator()

# learning list, turple,dirct 
grocery_list = ["apples" , "milk" , "bread" , "eggs"]
print(grocery_list)
student_grades = (95 , 88 , 72 , 90 , 85)
print(student_grades)
contact_info = {"name":"adebayo" , "phone_number":"+234-811-845-0176" , "email":"olasubomi4@gmail.com"}
print(contact_info)

grocery_list_copy = list(grocery_list)
student_grades_copy = tuple(student_grades)
contact_info_copy = dict(contact_info)

grocery_list_copy.append ("banana")
print(grocery_list_copy)
student_grades_copy_two = list(student_grades_copy)
avg_student_grades = sum(student_grades_copy_two) / len(student_grades_copy_two)
student_grades_copy_two.append(avg_student_grades)
avg_student_grades_two = tuple(student_grades_copy_two)
print(avg_student_grades_two)

contact_info_copy["address:"] = ("No2 KYC street")
print(contact_info_copy)

invitory = {
"apple":0.99,
"banana":0.95,
"milk":2.99,
"bread":2.49,
"fish":3.15,
"egg":3.99,
"cheese":4.99,
"chicken":7.99,
}
print(invitory["egg"])
print(invitory["fish"])
print(invitory["milk"])

movies = {
    "The Shawshank Redeption":9.3,
    "The God Father":9.2,
    "The Dark Knight":9.0,
    "12 Angry Men":8.9,
    "Schindler's List":8.9,
    "The Lord Of The Ring: The Return Of The King":8.9,
}
print(movies)

# Problems
# 1. A local library needs a function to calculate the late fee for overdue books. The library charges $0.25 per day for the first 5 days, and $0.50 per day thereafter. Write a Python function called calculate_late_fee that takes the number of overdue days as an argument and returns the total late fee.
# 2. ⁠A teacher wants to compute the average grade of her class. She has the grades stored in a list and wants to use a loop to sum them up and then divide them by the number of students to find the average. Write a Python program to accomplish this.
# grades = 85, 90, 78, 92, 88, 95, 100


# built a library over due book calculator
def calculate_late_fee ():
    try:
         overdue_days = int(input("input the number of overdue days\nDays = "))
         initial_rate = 0.25
         add_rate = 0.50
             
         if overdue_days <= 5:
           total_fee = overdue_days * initial_rate
           
         else:
             total_fee = (5 * initial_rate) + ((overdue_days - 5) * add_rate)
             return total_fee
    except ValueError:
        sys.exit("input the number of days")
late_fee = calculate_late_fee()

if late_fee is not None:
    print(f"the total late fee is ${late_fee:.2f}")
else:
    sys.exit("BOOK NOT OVERDUE")


# grade calculator
grades = [85, 90, 50, 92, 0, 95, 100]
total_sum = sum(grades)
student_sum = len(grades)

for grade in grades:
    total_sum + student_sum

average_grade = total_sum / student_sum
print(f"the grade of the class is: {average_grade:.2f}")


# 3. A small business owner wants to keep track of the inventory of her store. She uses a dictionary where the keys are the item names and the values are tuples containing the price and quantity in stock. Write a Python program that can print out all the items, their prices, and quantities in a readable format.
# inventory = {
#     "Apples": (1.20, 50),
#     "Bananas": (0.50, 100),
#     "Oranges": (0.75, 80)
#  }


inventory = {
     "Apples": (1.20, 50),
     "Bananas": (0.50, 100),
     "Oranges": (0.75, 80)
     }
print("inventory")
print("**********")

for item, details in inventory.items():
    price,  quantities = details
    print(f"{item}: Price--${price:.2f}, Quantities--{quantities:.2f}")
print("***************************************************************")    

    