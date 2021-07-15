total = float(input("Enter the total: "))
tip_percentage = int(input("Enter your tip percentage: "))

def decimal(x):
    return x/100

tip_decimal = decimal(tip_percentage)

def tip_calc(y, z):
    return y * z

tip = tip_calc(total, tip_decimal)

def combine(a, b):
    return a + b 

total_amnt = combine(total, tip)
print(total_amnt)
