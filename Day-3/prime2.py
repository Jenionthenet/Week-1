number = int(input("Enter a number to check if it is a prime number: "))

if number > 1:
  for index in range(2, number):
    if(number % index) == 0:
      print(f"{number} is not a prime number.")
      break
    else:
      print(f"{number} is a prime number.")
      break
else:
  print(f"{number} is a prime number.")
