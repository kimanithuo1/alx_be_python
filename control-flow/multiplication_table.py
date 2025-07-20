#enter a number and print the multiplication table

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"The multiplication table of {number} and {i} is: {number} x {i} = {number * i}")