import sys
import random
#AND all condition must be satisfied if not s"atisfied you get false (&) they must be the same 
#OR  means everything is true except if the condithion is not met it gives you false 
#elif this is gthe same as else/if

# number_one = input("input any number: ")
# value_one = int(number_one)
# number_two = input("input any number: ")
# value_two = int(number_two)

# if (value_two > value_one):
#     print("two is greater than one")
# elif (value_two == value_one):
#     print("both are equal")

# else: 
#     print("one is less than two")

#write a conditional statement to show the relationship between two value
# x=25,y=5
#conditions: x is greater than y,x is divisible by y,is the modulos  of y,else x is less than y 
# you can'nt use more than one "if!" use elif 

# x =25
# y = 5 

# if (x > y):
#     print("X is greater than Y")
# elif (x == y):
#     print("X is equal to Y")   
# elif (x / y):
#     print("X is divisible by Y")    
# elif (x % y):
#     print("X is the modulus  of Y")
# else:
#     print("X is less than Y")    

# print("")



# if x is divisible by y or y is greater than x print out this does not satisfy the condition

# x = 25
# y = 5

# if (x < y or x == y):
#     print("the condition has been met")
# else:
#     print("condition not satisfied")

# print("")

#write a conditional statement to show the relationship between two value
# x=25,y=5
#conditions: x is greater than y,x is divisible by y,is the modulos  of y, x is less than y (and /or) 


# def value(x , y):
#     if (x > y):
#         return("the condition has been met")
#     elif (x < y):
#         return("the condition has not been met")
#     else:
#         return("they are equal")
    
# print(value(13,13))    

# build a simple calculatorthat can perform addition subtraction and exponent
#sys.exit 
#random.choice this  makes the computer pick any random number 
# conditional statement



player_one = input("input any number ")
player = int(player_one)

if (player < 1 or player > 3):
    sys.exit("you execeded the amount of number needed E2")

player_two = random.choice("123") 
computer = int(player_two)    
print("")
print("The value of player is " + str(player) + "!")
print("the value of computer is " + str(computer) + "!")

if (player == 1 and  computer == 3):
    print("YOU WIN!!!")
elif (player == 2 and  computer == 1):
    print("YOU WIN!!!")
elif (player == 3 and computer == 2):
    print("YOU WIN!!!")    
elif (player == computer):
    print("IT A  TIE!!!")
else:
    print("COMPUTER WINS!!!")            


