#enter a number and print the multiplication table

number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 11):
    print(f"The multiplication table of {number} and {y} is: {number} x {y} = {number * y}")