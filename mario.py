def main():
    height = get_height()
    for i in range(height):
        print("#")
        
    # for i in range(height):
    #     print("?", end="") # end is a named argument here and "?" is a positional argument
    # print()
    
    print("?" * height)
    
    
# def get_height():
#     while True:
#         n = int(input("height : "))
#         if n > 0:
#             break
#     return n   # in python declared variables works out of scope also

def get_height():
    while True:
        try:
            n = int(input("height : "))
            if n > 0:
                return n
        except ValueError:
            print("Enter an interger")
    
    
main()