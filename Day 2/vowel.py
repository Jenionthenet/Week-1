letter = input("Enter your letter: ")

def vowel_or_no(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        print("Vowel")
    else:
        print("Not Vowel")

vowel_or_no(letter)
