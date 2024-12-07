my_dic={"a":1,"b":3,"c":3,"d":4}
unique_value=set()
result={}
for key,value in my_dic.items():
    if value not in unique_value:
        result[key]=value
        unique_value.add(value)
print(result)

