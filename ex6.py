word = input("Please input word\n")
rev_word = word[::-1]
if word == rev_word:
    print("word is palindrome")
else:
    print("word isn't palindrome")
