import sys
import math
import random
import string


# def candy_store():
#     large_jar = ["lollipop" , "chocolate" , "gummies" , "taffies"]
#     random_candies =[]
#     random_num  = random.choice([1,2,3,4])
#     random_candies.append(random_num)

#     for candies in range(1):
#         random_candie = random.choice(large_jar)
#         random_candies.append(random_candie)

#     print(random_candies)
# candy_store()    



# def savings_plan():
#     num_of_weeks = int(input("input the  numbers of weeks\n"))
#     initial_amount = 100
#     additional_amount = 25
#     total_savings = initial_amount
#     current_week = 0

#     while  current_week < num_of_weeks:
#         total_savings  +=  additional_amount
#         current_week += 1
#     print(f"the total savings for {num_of_weeks} weeks is ${total_savings} ")


# savings_plan()

# def taxi_fare(distance_kilometer):
    
#     base_fee = 500
#     per_kilometer_travelled = 20
#     total_fee = base_fee + (per_kilometer_travelled * distance_kilometer)
#     return total_fee
# kilometer = int(input("the number of kilometer travelled: "))
# fee = taxi_fare(kilometer)
# print(f"your total fee for {kilometer} kilometer is ${fee}")

# print("")


# def discount_cal(price):
#     c_f_d = 10000
#     discount_fee = 0.10

#     if price > c_f_d:
#         discount = price * discount_fee
#         final_price = price - discount

#     else:
#         final_price =  price

#     return final_price
# goods_price = int(input("Enter the price of goods bought: "))
# final_price = discount_cal(goods_price)
# print(f"Price: ${goods_price}")
# print(f"After adding discount: ${final_price} ")

# def lone_calculator():
#     lone_amount = int(input("input the amount of  loan collected: "))
#     lone_intrest = float(input("intrest rate "))
#     loan_term = int(input("input terms "))

#     def calculate_payment():
#         nonlocal lone_amount,lone_intrest,loan_term
#         intrest = (lone_amount * lone_intrest * loan_term) /100
#         return intrest
#     return calculate_payment()
# total = lone_calculator()
# print(f"the total intrest of the loan is ${total:.2f}")


# def factorial(n):
#     if n <= 1:
#         return n
#     else:
#         return n * factorial(n - 1)

# f_o_c = factorial(int(input("your factorial is ")))
# print(f"your factoria is {f_o_c}") 

# def palindrome(word):
#     word = word.lower()
#     return word  == word[::-1]
# word = str(input("input word "))
# result = palindrome(word)
# print(f"is {word} a palindrome? {result}")

# perform the following operations on the followin variable 

# convert both variable to list 
# concatinate both variables 
# print the value physics in courses in slicing method 
# add both variable in accending other

# courses = "biology","chemistry", "physics", "mathematics" ,"geography"


courses = "biology","chemistry", "physics", "mathematics" ,"geography"
# print(courses)
cars = "bmw","toyota","lexus","vovo","tesla"

courses_copy = list(courses)
# cars_copy = list(cars)
# courses_copy += (cars_copy)
# # print(courses_copy)
# courses_copy2 = courses_copy
# courses_copy2[:: 2]
# print(courses_copy2)
# courses_copy.sort
# # print(courses_copy)
# cars_copy.sort
# # print(car_copy)
courses_copy_slice = courses_copy[2:-2]
print(courses_copy_slice)












            

# Write a function to calculate the monthly payment for a loan. The function should take the loan amount, interest rate, and loan term as input. Use a closure to calculate the interest rate based on the loan amount.2