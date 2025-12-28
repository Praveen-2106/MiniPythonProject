"""String operations"""

name = (str(input("ENTER STRING: ")))
num = (int(input("ENTER NUMBER: ")))
print("BEFORE" "\n", name, "\n", num)

#operations
modified = name.replace(" ", "").lower()
length = len(modified)

#vowel

vowel = "aeiou"
count = 0   #Initialize( From 0)
count += modified.count("a")
count += modified.count("e")
count += modified.count("i")
count += modified.count("o")
count += modified.count("u")

result = num * length
greater = result > 100

#printing

print("\n", "AFTER" , "\n", "STRING=", modified, "\n", "\n", "LENGTH=" , length, "\n", "COUNT=", count, "\n", "RESULT=", result, "\n", "GREATER THAN 100=", greater)