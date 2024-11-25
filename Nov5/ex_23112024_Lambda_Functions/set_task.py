#Find the  first non-repeating character in a string using "Set".
def first_non_repeating_char(string):
    for char in string:
        if string.count(char)==1:
            return char

    return None

print(first_non_repeating_char("Swiss"))