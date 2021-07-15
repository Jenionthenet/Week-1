word = input("Enter a word: ")
rev_word = ""

for index in range(len(word) -1, -1, -1):
    rev_word += word[index]

if rev_word == word:
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome, sorry.")