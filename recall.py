# data types
# #string => " ",' '

# st = "Hello,World!"
# print(st)
# print(type(st))
#
# #Methods ------------------------ index value [] => start:stop:step
# # print(st[5::3])

# print(len(st))

# res = st.split(",")
# print(res)

# res = st.replace(",","-")   # ---------------------> old , new
# print(res)

#concatenation
# st1 = 10
# print(st*st1)

# #STRING REVERSABLE

# st2 = "Welcome all!"

# print(st2[::-1])     #=> start:stop:step


#list   => mutable

list1 = ["apple", "banana", "cat", "dog", "eagle"]
print(list1)

list2 = [1,2,3,4,5,6]
print(list2)
#Methods
list1[0]="Ant"          #=> Update
print(list1)

list1.append("12345678890")
print(list1)

list2.pop(2)
print(list2)

print(list1[1])

# del list2
# print(list2)

# list2.clear()
# print(list2)

# list2.sort()    #---->ASC
list2.sort(reverse=True)
print(list2)

#dict      =>key:value

dict1 ={
    "name":"minion",
    "age":21,
    "color":"yellow",
}
print(dict1)
print(dict1["name"])
#Methods
#get & values & keys
print(dict1.get("name"))
print(dict1.values())
print(dict1.keys())

#items
print(dict1.items())

#add
dict1["email"] = "minion@email.com"
print(dict1)


