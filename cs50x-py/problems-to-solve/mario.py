# Write a program that recreates a half-pyramid using hashes (#) for blocks,

try:
    height = int(input("Height: "))
except ValueError:
    print("You must enter a integer number.")

for i in range(1, height+1, 1):
    print((height-i) * " ", end="")
    print(i * "#")


