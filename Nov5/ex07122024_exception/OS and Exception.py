import os
print(os.getcwd())  #returns current working directory
files=os.listdir() #returns parent directory
print(f"files in current directory:{files}")   #returns all files in the directory
print(os.name) #windows name