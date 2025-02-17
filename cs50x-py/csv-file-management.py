import csv
file = open("phonebook.csv", "a") # append mode
name = input("Name: ")
lastname= input("Last name: ")

# writer = csv.writer(file)
# writer.writerow([name, lastname])

writer = csv.DictWriter(file, fieldnames=["name", "last name"])
writer.writerow({"name":name, "last name": lastname})

file.close()
