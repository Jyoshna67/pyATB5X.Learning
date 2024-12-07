#another way of creating dictionary
sample=dict(Name="jyo",Age="25")
print(sample)

#Dictionary from two list

keys=["name","age","experience"]
values=["jyoshna","25","QA"]
my_Dict=dict(zip(keys,values))
print(my_Dict)

#Merge two dictionaries

dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}
merged_dict=dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))

#missing keys in dictionary
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4,"e":3}
missing_keys=set(dict1.keys())-set(dict2.keys())
print(missing_keys)