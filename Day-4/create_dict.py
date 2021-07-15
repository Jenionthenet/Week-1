first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

name = {}

def create_name(first, last):
    name["first_name"] = first
    name["last_name"] = last

full_name = create_name(first_name, last_name)

print(f'My name is {name["last_name"] + ", " + name["first_name"]}.')


