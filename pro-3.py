# Account name generator

print("GREETINGS! FROM BANK OF SCAM","\n","WELCOME TO THE ACCOUNT CREATION PAGE")
name = str(input("Enter your full name : "))
num = int(input("Enter your full account number : "))

#operations

convert = name.lower().replace(" ", "")
last = str(num)[-2:]
username = convert + last 
length = username.__len__()

#prints

print(" SUCCESSFULLY CREATED!", "\n", "FullName : ",name, "\n", "Account Number: ",num, "\n", "UserName : ",username, "\n", "Length : ",length)

