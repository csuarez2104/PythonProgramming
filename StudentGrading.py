print("Student Grading Program \n")

print("Welcome to Grade Assignment")
name = input("Enter your name: ")
scid = input("Enter your SCID: ")

asg1 = float(input("Enter your percentage on assignment component of grade evaluation: "))
asg2 = float(input("Enter your percentage on lab submissions component of grade evaluation: "))
asg3 = float(input("Enter your percentage on reading exercises component of grade evaluation: "))
asg4 = float(input("Enter your percentage on quizzes component of grade evaluation: "))
asg5 = float(input("Enter your percentage on midterm exam component of grade evaluation: "))
asg6 = float(input("Enter your percentage on project component of grade evaluation: "))

total = (asg1 + asg2 + asg3 + asg4 + asg5 + asg6)
print("Your Grade is ", total, "%")

if total > 100:
    print("Letter Grade: NONE!")
    print("Grade Point: NONE! ")
    print("REDO YOUR MATH!")

elif total >= 94:
    print("Letter Grade: A!")
    print("Grade Point: 4.000! ")
    print("Excellent Performance!")

elif total > 90:
    print("Letter Grade: A-!")
    print("Grade Point: 3.667! ")
    print("Excellent Performance!")

elif total > 87:
    print("Letter Grade: B+!")
    print("Grade Point: 3.333! ")
    print("Good Performance!")

elif total > 84:
    print("Letter Grade: B!")
    print("Grade Point: 3.000! ")
    print("Good Performance!")

elif total > 80:
    print("Letter Grade: B-!")
    print("Grade Point: 2.667! ")
    print("Good Performance!")

elif total > 77:
    print("Letter Grade: C+!")
    print("Grade Point: 2.333! ")
    print("Average Performance!")

elif total > 74:
    print("Letter Grade: C!")
    print("Grade Point: 2.000! ")
    print("Average Performance!")

elif total > 70:
    print("Letter Grade: C-!")
    print("Grade Point: 1.667! ")
    print("Average Performance!")

elif total > 65:
    print("Letter Grade: D+!")
    print("Grade Point: 1.333! ")
    print("Unsatisfactory Performance!")

elif total > 60:
    print("Letter Grade: D!")
    print("Grade Point: 1.000! ")
    print("Unsatisfactory Performance!")

elif total > 55:
    print("Letter Grade: D-!")
    print("Grade Point: 0.667! ")
    print("Unsatisfactory Performance!")

elif total < 54.99:
    print("Letter Grade: F!")
    print("Grade Point: 0.000! ")
    print("Failing Performance!")
