my_dict= {
    "Name":"Jyoshna",
    "Age":"25",
    "Role":"QA"

}
print(my_dict["Role"])

#delete
del my_dict["Age"]
print(my_dict)

#Iteration
for key,value in my_dict.items():
    print(key+"--->",value)
