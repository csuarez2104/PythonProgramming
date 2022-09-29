print("1-Area of Circle= πr2")
print("2-Area of Rectangle= wl")
print("3-Area of Triangle=  1/2×b×h")
print("4-Area of Rhombus= p*q/2")
print("5-Square Root of a Number= sqrt()")
while True:
    try:
        num = float(input('Please Choose an Operation: '))
        break
    except ValueError:
        print('Invalid Choice, Enter Again.')

if num == 1:
    print("Area of Circle= πr2")
elif num == 2:
    print("Area of Rectangle= wl")
elif num == 3:
    print("Area of Triangle=  1/2×b×h")
elif num == 4:
    print("Area of Rhombus= p*q/2")
elif num == 5:
    print("Square Root of a Number= sqrt()")
