#Input positive integer that represents size of the pattern

pattern_size = int(input("Enter the size of the pattern: "))

row= 0

#Draw the square pattern

while row < pattern_size:
  for col in range(pattern_size):
    print("*", end="")
  print()
  row += 1