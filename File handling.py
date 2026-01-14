# File handling operations
# Read Write Append Extend
from random import sample

#Read

demo = open('sample.txt', "a")
sam = demo.write("\nThis is added2.")
demo.close()
print(sam)

#with automatically closes the file
with open('sample.txt', "a") as file:
    file.write("Hello USer!")
    file.write("\nWelcome!")