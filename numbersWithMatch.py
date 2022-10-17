"""
Programmer: Carlos Suarez
Program : Numbers Type
Python 3.7.9
First Writen : 9-26-2022, 8:46:00 AM
Last Updated : 10-05-2022, 8:16:00 AM
"""

print("Welcome to Mathematical Operations")
print("1-Odd Numbers \n 2-Even Numbers \n 3-Prime Numbers \n 4-Perfect Numbers \n 5-Palindrome Numbers")

choice = int(input("Choose the operation: "))

match choice:
 case 1:
    print("Odd Numbers")
    for i in range(0, 101):
        if i % 2 != 0:
            print(i, end=' ')

 case 2:
    print("Even Number")
    for i in range(0, 101):
        if i % 2 == 0:
            print(i, end=' ')

 case 3:
    print("Prime Numbers")
    counter = 0
    for n in range(1,101):
        for i in range(2,int(n/2+1)):
            if n % i == 0:
                counter=counter+1
            if counter==0:
                print(n, end=' ')
            counter = 0

 case 4:
    print("Perfect Numbers")
    for i in range(1, 51):
        sum = 0
        for n in range(1, i):
            if i % n==0:
                sum = sum + n
            if sum == i:
                print(i, end=' ')

 case 5:
    print("Palindrome Numbers")
    number=int(input("Please Enter your number: "))
    reverse=0
    originalNumber=number
    while number > 0:
        remainder=int(number%10)
        reverse=int(reverse*10+remainder)
        number=int(number/10)
    if originalNumber==reverse:
        print(originalNumber, "is a Palindrome Number")
    else:
        print(originalNumber, "is not a Palindrome Number")
