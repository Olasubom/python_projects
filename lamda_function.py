
from math import sqrt
from functools import reduce
# square = lambda x: x*x
# print(square(2))

# numbers = [2,4,8,10,5]
# sqr = 


# write a lamdafunction that returns the square root of it

# numb = [4,16,25]
# sqr = map(lambda x: sqrt(x),numb) 
# print(list(sqr))

#map means to iterate
#filter if you are working on a condition

que = lambda num : num * num
print(que(2))
doc = lambda a,b : a + b
print(doc(3 , 2))
################################

def funbuilder(x):
    return lambda num : num + x

add_ten =  funbuilder(10)
add_twenty = funbuilder(20)

print(add_ten(7))
print(add_twenty(7))

# higher order function are fution that are built into python


numbers = [5,7,5,12,24 ]
square = map(lambda num: num * num , numbers)
print(tuple(square))
 
# return the remainder of division 
odd_num  = filter(lambda num : num % 3 != 0 , numbers) #checking to make sure it is odd
print(tuple(odd_num))

# to print output as even
odd_num1 = filter(lambda num : num % 2 == 0 , numbers)
print(tuple(odd_num1))

##############
#  acc also know  as the subtotal
# curr  which reprecent the currrent item
# reduce adds all the number together 
number  = (123475)
total = reduce(lambda acc , curr : acc + curr,numbers)
print(total)


names = ["bola" , "ade" , "kunle", "adebayo"]
count = reduce(lambda acc , curr : acc + len(curr),names,0)
print(count)