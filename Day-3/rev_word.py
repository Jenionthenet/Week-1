word = input("Enter a word: ")
rev_word = ""

for index in range(len(word) -1, -1, -1):
  rev_word += word[index]   

print(rev_word)
