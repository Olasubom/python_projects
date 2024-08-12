# #formatting of str
# #lisy are date type that can be refenced with a common name(variable name)
# #they are represented with a square [] or the list()

# Cars = ["volvo" , "benz" , "lexus"]
# Cars.append (["bmw" , "toyota"])
# Cars += ["brt", "ferarri"]
# Cars = ["valvo" , "benz" , "lexus" , "bmw" , "toyota", "brt" , "ferarri"]
# Cars.remove ("ferarri")
# print(type(Cars))
# print(Cars[3:7])

# car_copy = list(Cars)
# print(car_copy)
# car_copy.sort()
# print(car_copy)
# car_copy.pop()
# print(car_copy)
# car_copy.insert(5 , "hive")
# print(car_copy)
# car_copy_2 = car_copy[1:4]
# print(car_copy_2)

# print(Cars)
# print(car_copy)
# print(car_copy_2)

# car_copy.pop()
# print(car_copy)
# del car_copy_2[0]
# print(car_copy_2)


# car_copy.clear()
# print(car_copy)
# print(car_copy)
# print(Cars)
# print(car_copy_2)


#[] used for the  key for  dict()// for copy
#tuple()//for copy

fruit = ["apple" , "banana" , "orange" , "pinapple"]

#tuple of student information
student = ("alice" , 25 , "computer_science" , "biology")

#dictionary of contact information
contact = {"name":"Bob" , "phone":"123-456-7890" , "email":"bob@gmail.com"}

fruit_copy = list(fruit)
student_copy = tuple(student)
contact_copy = dict(contact)

print(fruit_copy)
print(student_copy)
print(contact)

fruit_copy.append("mango")
fruit_copy.append("carrot")
print(fruit_copy)
student_copy_two = list (student_copy)
student_copy_two.append("bola")
student_copy_two.append(26)
student_copy_two = tuple (student_copy_two)
print(student_copy_two)

contact_copy["City:"] = ("Lagos")
contact_copy["Country"] = ("Nigeria")
print(contact_copy)

del fruit_copy[5]
print(fruit_copy)

student_copy_three = list(student_copy_two)
student_copy_three.pop(5)
student_copy_three = tuple(student_copy_three)
print(student_copy_three)

contact_copy.pop("Country")
print(contact_copy)