
# One big dictionary
people = {
  "Yulia":"1234", 
  "David":"1235", 
  "John":"1236",
}

name = input("Name ")

if name in people:
  print(f"Name: {people[name]}")
else:
  print("Not found.")
