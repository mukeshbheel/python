import csv

# file = open("phonebook.csv", "a")
# name = input("Name : ")
# number = input("Number : ")

# writer = csv.writer(file)
# writer.writerow([name, number])

# file.close()

with open("phonebook.csv", "a") as file:
    name = input("Name : ")
    number = input("Number : ")
    
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name":name, "number":number})

    # writer = csv.writer(file)
    # writer.writerow([name, number])



# phoneBook = {
#     "carter":"6454535353",
#     "mukesh":"9877878786"
# }

# name = input("Name : ")
# if name in phoneBook:
#     number = phoneBook[name]
#     print(f"Number : {number}")