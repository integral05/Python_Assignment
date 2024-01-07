#1.WAP to print numbers from a given range.
'''
start = int(input("Enter your starting value:"))
end = int(input("Enter your ending value:"))

for i in range (start,end):
    print(i,end=" ")
print()
'''



#2.Write a Program to print all Even numbers from a given range.
'''
start = int(input("Enter your starting value:"))
end = int(input("Enter your ending value:"))

for i in range (start,end):
    if(i%2==0):
        print(i,end=" ")
print()
'''
    

#3.WAP to print the sum of all numbers from a given range.
'''
start = int(input("Enter your starting value:"))
end = int(input("Enter your ending value:"))
sum=0
for i in range(start,end):
    sum+=i
    if(i==end-1):
        print(sum)
    #sum+=i
'''
#4.WAP to print all the character values of the given ASCII value range from the user

'''
start = int(input("Enter your starting range:"))
end = int(input("Enter your ending range:"))

if((start>=65 and end<=90) or (start>=97 and end<=122)):
    for i in range(start,end+1):
        
        print("The character ASCII value {} is".format(i),chr(i))

else:
    print("Wrong Input")
'''


#5.WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100


'''
start=int(input("Enter your starting value:"))
end=int(input("Enter your ending value:"))

for i in range(start,end):
    if(i%7==0 and i%3!=0):
        print(i,end="  ")
print()
'''


#6.WAP to print all the ASCII values from a given character range.

'''
start=(input("Enter the start range:"))
end=(input("Enter the end range:"))
for i in range(ord(start),ord(end)):
#for i in range(ord(start),ord(end)+1):-------------> #TO PRINT FROM A TO Z
    print("ASCII value of",chr(i),"is",(i))
'''


#7.WAP that prints all Positive numbers from a given range.
'''
start=int(input("Enter starting value:"))
end= int(input("Enter ending value:"))
for i in range (start,end):
    if (i>0):
        print(i,end=" ")
print()
'''

#8.WAP to prints numbers which are divisible by 3 and 5 both in a given range.

'''
start=int(input("Enter starting value:"))
end= int(input("Enter ending value:"))

for i in range (start, end):
    if(i%3==0 and i%5==0):
        print(i,end=" ")
print()
'''

#9.WAP to print the count of all negative numbers from a given range
'''
start=int(input("Enter starting value:"))
end= int(input("Enter ending value:"))

count=0
for i in range(start,end):
    if(i<0):
        count+=1
print(count)
'''

#10.WAP program to calculate and print the product of the count of odd numbers within a given range.


start=int(input("Enter starting value:"))
end= int(input("Enter ending value:"))
prod=1
count=0
for i in range(start,end):
    if(i%2!=0):
        count+=1
        prod=prod*i
print(prod)






















