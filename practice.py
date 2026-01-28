
# String methods
"""
a="Hello,World"
b="Hiii"
print(a)

print(a.upper())
print(a[0:5])
print(a[:-6])
print(a.capitalize())
print(a.split(","))
print(a+ " " + b)
print(a.replace("," , "."))

name="Praveen"
age=22

print("My name is", (name) , "and my age is", (age))
"""
# Dict

"""student = {
             "name" : "Praveen", "Dept" : "IT"
            }
alter = student.update(name="Parvin")
print(student)"""

# List
"""
    fruits = ["Apple", "Banana", "Carrot", "Demo", "Elephant", 1, 2, 3.4, True]
    animal = ["Air", 1, 4, 6, "Balloon"]
    
    joint = fruits + animal
    
    print(animal[3:5])

"""

# Statements
# import camelcase
# # c = camelcase.CamelCase()
# age = "under world"
# print(camelcase.CamelCase().hump(age))
# def demo(a, b, c):
#     print(c, b, a )
# demo(2, 3, 5)


# def demo(**kwargs):
#     # print(kwargs)
#     return kwargs
# print(demo(name="Praveen", age=18, dept="IT"))

def demo(s):
    return " ".join(word.capitalize() for word in s.split(" "))
s=input()
result = demo(s)

