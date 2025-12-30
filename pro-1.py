#A school wants a basic program to manage a student’s academic and fee details.

student_name=input("Enter your name=")
roll_number=input('Enter your rollnumber=')
student_class=input("Enter your class=")
print(f"Details \nName:{student_name}, Rollnumber:{roll_number}, Class:{student_class}")

print("\nPlease enter your marks")
marks1=int(input("Enter your mark1="))
marks2=int(input("Enter your mark2="))
marks3=int(input("Enter your mark3="))
total_marks = marks1 + marks2 + marks3
print("Total marks", total_marks)
average=total_marks / 3
print("Average marks", round(average))
if(average>=80):
    print("Pass")
    print("Grade:A+")
elif(average >60 and average < 79):
    print("Pass")
    print("Grade:A")
elif(average > 40 and average < 59):
    print("Pass")
    print("Grade:B")
else:
    print('Fail')
    print("Grade:C")

#Fees details
total_fees=int(input("Enter your total school fee="))
paid=int(input("Enter the paid fees="))
remain_fee = total_fees - paid
print(remain_fee)

if(remain_fee > 0):
    print("Fee Pending")
else:
    print("Fee cleared")

remark=input("Enter your remark:")
print(remark.upper())
print("length of the word is:",len(remark))