# # print("odd number")
# #
# # for i in range (0, 101):
# #     if i%2 != 0:
# #         print(i, end=' ')
#
# print("even number")
#
# for i in range (0,101):
#     if i%2 ==0:
#         print(i, end=' ')


# print("Prime Numbers")
# counter=0 #intializing counter variale to 0
# for n in range(1,101): #iterating for number between 2 and n/2+1
#     for i in range(2,int(n/2+1)): #checking number of diviors for a number
#         if n%i==0: #check for remainder is 0
#             counter=counter+1 #increase the counter if you find a divisor
#     if counter==0: #decision to see if counter is 0 i.e no divisors
#         print(n, end=' ') #printing if the number is prime
#     counter=0
#
print("Perfect Numbers from First 100 Natural Numbers")
check = 0
sum = 0
n = 6
for i in range(1, int(n / 2) + 1):
    check = n % i
    if check == 0:
        sum = sum + i
if sum == n:
    print(n, end=' ')
