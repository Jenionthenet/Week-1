number = int(input("Enter a number: "))

def prime_or_not(x):
    if  (x != 2 and x != 3 and x != 5 and x != 7) and (x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0):
        print("Your number is not a prime number.")
    else:
        print("Your number is a prime number.")

prime_or_not(number)
