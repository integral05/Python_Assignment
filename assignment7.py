
'''1. WAP to print the following series using a while loop 105, 98, 91, 84, 77, 70 ........7'''

# i=105
# while(i>=7):
#     print(i,end="  ")
#     i=i-7



'''2. Write a program to check whether the number is a Prime number or not. (2332)'''

# num=int(input("Enter the number:"))
# i=2
# while(i<num):
#     if(num%i==0):
#         print("{} is Not Prime number".format(num))
#         break
#     else:
#         print("{} is prime number".format(num))
#         break



'''3. Write a program to check whether the number is a Perfect number or not.'''

# num=int(input("Enter the number:"))
# i=1
# sum=0
# if (num>=0):
#     while(i<num):
#         if(num%i==0):
#             sum+=i
#         i+=1
#     if(sum==num):
#        print("{} is a perfect number".format(num))
#     else:
#         print("{} is not perfect number".format(num))
# else:
#     print("Please Enter number greater than 0")



'''4. Write a program to count the digits of the given number.'''

# num=int(input("Enter the number:"))
# count=0
# while(num>0):
#     count+=1
#     num//=10
# print(count)



'''5. Write a program to count the even digits of the given number.'''

# num=int(input("Enter the number:"))
# count=0
# while(num>0):
#     count+=1
#     num//=10
# print(count//2)



'''6. Write a program to count the Odd digits of the given number.'''

# num=int(input("Enter the number:"))
# count=0
# oddcount=0
# while(num>0):
#     count+=1
#     num//=10
#     if (count%2==1):
#         oddcount+=1
# print(oddcount)



'''7. Write a program to reverse the given number.'''
# rev=0
# num=int(input("Enter the number:"))
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# print(rev)



'''8. Write a program to check whether the number is a Palindrome number or not.'''

# num=int(input("Enter the number:"))
# onum=num
# rev=0
# rem=0
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# if(rev==onum):
#     print("{} is a Palindrome number".format(onum))
# else:
#     print("{} is not palindrome number".format(onum))



'''9. Write a program to check whether the number is Armstrong's number or not.'''

# num=int(input("Enter the number:"))
# tn1=num
# tn2=num
# count=0
# rem=0
# sum=0
# while(num>0):
#     count+=1
#     num//=10
# while(tn1>0):
#     rem=tn1%10
#     sum=sum+(rem**count)
#     tn1//=10
# if(sum==tn2):
#     print("{} is an Armstrong number".format(tn2))
# else:
#     print("{} is NOT an Armstrong number".format(tn2))



'''10. Write a program to check whether the number is a Strong number or not.'''

# num=int(input("Enter the number:"))
# tn1=num
# fact=1
# sum=0
# rem=0
# i=1
# while(num>0):
#     rem=num%10
#     num//=10

#     while(i<=rem):
#         fact*=i
#         i+=1
#     sum+=fact
#     i=1
#     fact=1

# if(sum==tn1):
#     print("{} is a Strong number".format(tn1))
# else:
#     print("{} is not Strong number".format(tn1))


    







