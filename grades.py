"""
Programmer: Carlos Suarez
Program : Grades
Python 3.10.9
First Writen : 10-31-2022, 8:51:00 AM
Last Updated : 10-31-2022, 8:51:00 AM
"""
grades = [15, 23, 22, 21, 20]

print(grades)
index = int(input("Which assignment grade do you want to know: \t"))
print("The grade you received in assignment-1 is", grades[index-1])

for i in range(0, len(grades)):
    grades[i] = grades[i] + 2

print("Displaying the updated grades \n", grades)
