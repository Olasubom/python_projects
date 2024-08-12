# def sum(num1 ,num2):   #this is called a parameter and they never change
#     print(num1 + num2)
# sum(2 , 3)  # this is an arguement,that use the defination of the function.argumment  can change with every function call.
# sum(5, 9)
# sum(6, 7)      

def  sum(num1=0 , num2=0):
    if (type(num1)is not  int or type(num2) is not  int):
        return
    return num1 + num2
total = sum(1, 2)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("dave" ,"john")    

def mult_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_name_items(first = "john", last = "sera")
#the output came out  as  dict because of the  **
# i tried usind another name (kwargs) annd  it  worked!!

