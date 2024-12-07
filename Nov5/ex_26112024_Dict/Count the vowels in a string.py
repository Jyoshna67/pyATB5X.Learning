input_string="Hello World"
vowels="aeiou"
vowels_count=0
consents_count=0
for char in input_string:
    if char in vowels:
        vowels_count=vowels_count+1
    else:
        consents_count=consents_count+1
print(consents_count)
print(vowels_count)

