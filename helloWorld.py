name = input("what is your name? ") #no need to declare the variable type here, python automatically detects the data type
                                    #input funciton gives you string
print("hello, " + name)
print("hello,", name) #print takes more arguments , two in case of this situation
print(f"hello, {name}") #f = format string

try:
    num = int(input('Enter an integer : '))
    print('Number', num)
except ValueError:
    print('Invalid Input : please enter an integer.')
    
#for loop in python
for i in [0, 1, 2]:
    print("hello world")
    
for i in range(3):       #range gives you the number one by one, it doesn't allocate a array of 3 in the memory in the starting, range datatype is better 
    print("hello world")    