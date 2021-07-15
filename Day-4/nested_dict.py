addresses = []

while True:
    number = input("Enter address number: ")
    street = input("Entet street name: ")
    city = input("Enter city: ")
    state = input("Enter state: ")

    address = {"number": number, "street": street, "city": city, "state": state }

    addresses.append(address)

    choice = input("Enter q to quit or any key to continue: ")
    if choice == "q":
        break


user = {"first_name": "Jenifer", "last_name": "Ine", "addresses" : addresses }

print(user)