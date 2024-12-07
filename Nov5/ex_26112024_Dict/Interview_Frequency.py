#Frequency of characters in a string.
#write a program to count the frequency of characters in a string
#string="automation"

string=input("Enter a string")
char_count={}
for char in string:
    char_count[char]=char_count.get(char,0)+1
print(char_count)

