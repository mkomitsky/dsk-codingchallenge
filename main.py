count = int(input("How many number would you like to sunnarize?"))
sum = 0
for i in range(count):
  sum += int(input(f"Enter number {i+1}:"))
print(f"The sum of the numbers is: {sum}")