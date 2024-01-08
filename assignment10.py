'''Assignment 10'''


##1.

# a=1
# for i in range(1,4,1):
#     for j in range(1,4,1):
#         if(a<=3):
#             print(a*a,end="   ")
#         else:
#             print(a*a,end="  ")
#         a+=1
#     print()



##2.

# a=65
# for i in range(1,4,1):
#     for j in range(1,4,1):
#         print(chr(a),end=" ")
#         a+=1
#     print()
# print()



##3.


# for i in range(1,5,1):
#     for j in range(65,69,1):
#         print(chr(j),end=" ")
#     print()

'''ALTERNATIVE CODE'''

# a=65
# for i in range(1,5,1):
#     for j in range(1,5,1):
#         print(chr(a),end="  ")
#         a+=1
#     a=65
#     print()



##4.

#In this program variable 'a'=1, then 1 is added in squared of 'a' then it is printed; then 'a' is incremented by 1 
# a=1
# for i in range(1,4,1):
#     for j in range(1,4,1):
#         print((a**2)+1,end="   ")
#         a+=1
#     print()

'''ALTERNATIVE'''

#In this program variable 'a' = 2 and variable 'diff'=1, then value of 'a' is printed after that 2 is added in 'diff', then 'diff' is added in 'a' again value is printed until loops are completes 
# a=2
# diff=1
# for i in range(1,4,1):
#     for j in range(1,4,1):
#         if(a<=9):
#             print(a,end="   ")
#         else:
#             print(a,end="  ")
#         diff+=2
#         a+=diff
#     print()




##5.


# a=1
# for i in range(1,5,1):
#     for j in range(1,5,1):
#         if(a%2==1):
#             print(a**2,end="    ")
#         else:
#             print(a,end="    ")
#         a+=1
#     print()



##6.


# for i in range(1,5,1):
#     for j in range(1,5,1):
#         print(i,end="   ")
#         i+=3
#     print()



##7.

# for i in range(1,5,1):
#     for j in range(1,5,1):
#         if(j%2==1):
#             print("$",end="  ")
#         else:
#             print("=",end="  ")
#     print()



##8.


# for i in range(1,6,1):
#     a=69
#     for j in range(1,6,1):
#         print(chr(a),end="  ")
#         a-=1
#     print()



##9.

# a=65
# for i in range(1,4,1):
#     for j in range(1,4,1):
#         if(a%2==0):
#             a+=32
#             print(chr(a),end="  ")
#             a-=32
#         else:
#             print(chr(a),end="  ")
#         a+=1
#     print()



##10.

# a=68
# for i in range(1,5,1):
#     for j in range(1,5,1):
#         print(chr(a),i,end="    ")
#         a-=1
#     a=68
#     print()


