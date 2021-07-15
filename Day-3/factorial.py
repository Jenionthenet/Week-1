number = int(input("Enter a number to find its factorial: "))
factorial = 1

if number == 0:
    factorial = 0

else:
    for index in range(1, number + 1):
       factorial *= index
print(f"The factorial for {number} is {factorial}.")