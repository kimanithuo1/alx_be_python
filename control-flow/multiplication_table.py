#enter a number to print its multiplication table

number = int(input("Enter a number to see its multiplication table: "))

#Print the multiplication table
for i in range(1, 11):
    print(f"The multiplication table of {number} is: {number} x {i} = {number * i}")