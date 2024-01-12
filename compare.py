s = input("Do you agree? ")
# if s == "Y" or s == "y":
#     print("Agree")
# elif s == "N" or s == "n":
#     print("Disagree")
s = s.lower() #string are immutable in python, python allocates new memory with new string and assign to s and removes the old memory
    
if s in ["y", "yes"]:
    print("Agree")
elif s in ["n", "no"]:
    print("Disagree")   
    
# difference in method and function
# method is a function which is build into the datatype itself ex : "heelo".lower()

# in struct in c only values can be inserted into a data type
# in object oriented programming in python methods can also build in into data types ex: string functions
