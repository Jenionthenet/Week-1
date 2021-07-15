price = float(input("Enter the price: "))
percentage = int(input("Enter the tip percentage: "))

def percent_to_decimal(x):
    return x/100

decimal = percent_to_decimal(percentage)

def tip(y, z):
    return y * z

tip_amount = tip(price, decimal)
print(tip_amount)
