# Feature	List	Tuple	Dictionary
# Ordered	Yes	    Yes	    No
# Mutable	Yes	    No	    Yes
# Syntax	[]	    ()	    {}
# Access	Index	Index	Key

# """
# # Lists hold multiple values and can be referenced with a common name.
# # Lists starts with the zero index from the left and -1 from the right.
# # Use the index to get the position of a value in the list.
# # Use the len function to get the length of the list.
# # Use the append() and extend() function to add a new value to the list. you can also use the += operator with [] to add
# # The insert method uses two arguments(location, value).
# # Slices are used to insert and replace ranges of values.
# # the remove() method is used to remove a value from the list.
# # the del keyword is used to delete an entire list or a subset of a list.
# # the clear() method is used to clear a list and make it empty.
# # the pop() method is used to remove the last value from the list.
# # ways to create a copy of a list are : .copy(), list() and [:] methods
 # the sorted(variable, method) function is used to sort globally without changing the original list.
 # tuples values cannot be changed. it is created using () or the tuple() function.
# packing and unpacking a tuple is the process of adding and removing values in a tuple.
#  Dictionaries can be created using the {"key": "value"} or the dict() constructor function


names =["list", "john" , "sara"]
data = ["list" , "john" ,"true"]
empty =[]

print("john" in names)
print(names[1])
print(names[2])
print(names.index("john"))
print(names[2 :])
print(len(data))
names.append("bola")
print(names)
names += ["james"]
print(names)
names.extend(["dave" , "joe"])
print(names)
# names.extend(data)
# print(names) this add a list to a list
names.insert(0 , "bob")
print(names)
# to insert more than one value 
names[2:2] = ["bayo" , "timi"]
print(names)
# this  stars and end at the same value it did not remove any value from the previous value

names[1:3] = ["Greag","morty"]
print(names)
# this replaces the privious with the curreent one this means it starts at 1 and  ends at 3 so it also remove the values there ["bayo" ,"timi"]

names.remove("timi")
print(names)

print(names.pop())
print(names)

del names[0]
print(names)

data.clear()
print(data)

names.sort()
print(names)

names.sort(key=str.lower)
print(names)


nums =[4,2,5,1,10]
nums.reverse()
print(nums)
# diffence between reverse and sort reverse
nums.sort(reverse=True)
print(nums)

# to copy in list 

nums_copy = nums.copy()
mynums = list(nums)
yournum = nums[:]

print(nums_copy)
mynums.sort()
print(mynums)
print(yournum)

# tuple 
 








#  dictionary
info = {
    "name" : "bola",
    "address": "ikorodu"

}

info2 = dict(name= "bola", address ="ikorodu")
print(info)
print(info2)
print(info["name"])
print(info.get("address"))
# to get all keys in a dict
print(info2.keys())
print(info2.values())
# to return as turple 
print(info.items())

info["name"] = "ade"
info.update({"number": "818310113"})
print(info)




