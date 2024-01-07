##1. WAP to print the first 10 Numbers in reverse order.

# i=10
# while(i>=1):
#     print(i," ",end="")
#     i-=1
# print()



##2. WAP to calculate the sum of the first 10 even numbers.

# count=1
# sum=0
# i=1
# while(count<=10):
#         if (i%2==0):
#             sum = sum + i
#             count+=1
#         i+=1
        
# print("The sum of first 10 even numbers is:",sum)



##3. WAP to find the 7th odd number (start from 1)

# count=0
# i=1
# while(count<=7):
#     if (i%2==1):
#         count+=1
#         if(count==7):
#             print("7th Odd number is:",i)
#     i+=1



##4. WAP to calculate the factorial of a given number.

# num=int(input("Enter your number:"))
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i
#     i+=1
# print("Factorial of {} is:".format(num),fact)



##5. WAP to print the first 10 negative numbers which is less than the given number.

# num=int(input("Enter any negative number:"))
# print("First 10 negative numbers less than {} are: ".format(num),end="")
# count=1
# i=num
# while(count<=10):
#     i-=1
#     print(i,end="  ")
#     count+=1
        
# print()



##6. WAP to print the table of entered number

# num=int(input("Enter the number:"))
# count=1
# i=1
# while(count<=10):
#     print(num*i,end="  ")
#     count+=1
#     i+=1
# print()



##7. WAP to find the nth even number.

# num=int(input("Enter your number:"))
# count=0
# i=1
# while(count<=num):
#     if (i%2==0):
#         count+=1
#         if (count==num):
#             print("Even number at position {} is:".format(num),i)
#     i+=1

'''ANOTHER OPTION IS '''

#print("Even number at position {} is:".format(num),2*num)



##8. WAP to print the sum numbers up to n.

# num=int(input("Enter your value:"))
# sum=0
# for i in range(0,num+1,1):
#     sum=sum+i
# print("Sum of numbers upto {} is:".format(num),sum)



##9. WAP to print squares of even numbers up to n.

# num=int(input("Enter your number:"))
# i=1
# while(i<=num):
#     if(i%2==0):
#         print(i*i,end="  ")
#     i+=1
# print()



##10. WAP to print a cube of odd numbers up to n in reverse order.
        
# num=int(input("Enter your number:"))
# i=1
# while(i<=num):
#     if (num%2==1):
#         print(num*num*num,end="  ")
#     num-=1
# print()