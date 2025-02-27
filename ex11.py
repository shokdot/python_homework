def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    if not string:
        return
    string = string.lower()
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Input text: ")
print(count_vowels(string))

