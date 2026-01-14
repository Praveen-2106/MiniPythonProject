# function to perform avg and grade

def average(marks):
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        print("Grade: A+")
    elif avg >=80:
        print("Grade: A")
    elif avg >= 70:
        print("Grade: B+")
    elif avg >= 60 :
        print("Grade: B")
    elif avg >= 40:
        print("Grade: C")
    else:
        print("Fail")