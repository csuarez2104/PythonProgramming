"""
Programmer: Carlos Suarez
Program : Function to Compute the Average of Three Numbers
Python 3.10.9
First Writen : 10-16-2022, 8:46:00 AM
Last Updated : 10-16-2022, 8:16:00 AM
"""


def average(a, b, c):  # function definition for average calculation
    avg = (a + b + c) / 3
    return avg


print("Program to Calculate Average of Three Numbers")
a = float(input("enter the value of a :\t"))
b = float(input("enter the value of b :\t"))
c = float(input("enter the value of c :\t"))
result = average(a, b, c)  # calling the average function
print("Average of Given Numbers:\t", result)
