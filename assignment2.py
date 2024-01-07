#1. NUM DIVISIBLE BY 4 & 5
'''
num = int(input("Enter your number:"))
if(num%4==0 and num%6==0):
    print("{} is divisible by 4 and 5".format(num))
else:
    print("{} is not divisible by 4 and 5".format(num))
    '''

#2.WAP to determine whether entered angles define a right-angled triangle.Take three values of angle from the user.
'''
angle1=float(input("Enter your value for angle1:"))
angle2=float(input("Enter your value for angle2:"))
angle3=float(input("Enter your value for angle3:"))

if((angle1==90 and angle2!=90 and angle3!=90) or(angle1!=90 and angle2==90 and angle3!=90) or (angle1!=90 and angle2!=90 and angle3==90)):
    print("It is right angle triangle")
else:
    print("It is not  right angle triangle")
'''



#3. Take two numbers from users and print the sum of those numbers if the sum is even.
'''
num1 = int(input("Enter value for number1:"))
num2 = int(input("Enter value for number2:"))

if((num1 + num2)%2==0):
    print(num1+num2," is Even")
else:
    print("No Output")
'''


#4. Take a number from the user and check whether it is present in the list. If it's in the list, print "Available."

'''
list1 = [10,20,30,40,50]

num = int(input("Enter your value:"))
if(num in list1):
    print("Available")
else:
    print("No Output")
'''




#5. Print the "Core2web" string a number of times entered by the user if the number is even.
'''
num = int(input("Enter your value:"))
if(num%2==0):
    for i in range (num):
        print ("Core2web")
else:
    print("No Output")
'''



#6. Write a program that checks if a given number is odd using the "if" statement.
'''
num = int(input("Enter your value:"))

if(num%2!=0):
    print("Odd")
'''



#7. Take two numbers from the user, check if both are odd and then print the sum of the numbers.
'''
num1=int(input("Enter your value for Number1:"))
num2=int(input("Enter your value for Number2:"))

if((num1%2==0 and num2%2!=0) or (num1%2!=0 and num2%2==0)):
    print(num1 + num2)
else:
    print("No Output")
'''


#8. Take single character from user check if the ascii value of character is Even the print character.
'''
char=input("Enter your character:")

if (ord(char)%2==0):                  #"ord()" is a built in function in python to obtain the value of given character
    print(char)
else:
    print("No Output")
'''


#9. Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character
'''
char1 = input("Enter your 1st character:")
char2 = input("Enter your 2nd character:")

if (ord(char1)%2!=0 and ord(char2)%2!=0):
    print(ord(char1) + ord( char2))
else:
    print("No Output")
'''

#10. Take the number from user and modulus with 8 if the reminder of the number is 3 then print reminder.
'''
num = int(input("Enter your Number:"))

if (num%8==3):
    print("3")
else:
    print("No Output")
'''




































