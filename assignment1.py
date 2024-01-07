
#1.MAXIMUM BETWEEN TWO NUMBERS
'''
a= int(input("Enter 1st number:"))
b= int(input("Enter 2nd number:"))

if(a>b):
    print(a,"is max between",a, "&", b)
else:
    print(b,"is max between" ,a, "&", b)
'''



#2.+ve,-ve or =0 number
'''
a2= int(input("Enter your number:"))

if(a2>0):
    print("{} is positive number" .format(a2))
elif(a2<0):
    print("{} is negative number" .format(a2))
else:
    print("{} is equal to zero" .format(a2))
'''



#3.EVEN OR ODD NUMBER

'''
a3= int(input("Enter your number:"))
if(a3%2==0):
    print("{} is even number".format(a3))
else:
    print("{} is odd number".format(a3))
'''





#4.DIVISIBLE BY 5 OR NOT

'''
a4=int(input("Enter your number:"))
if(a4%5==0):
    print("{} is divisible by 5".format(a4))
else:
    print("{} is not divisible by 5" .format(a4))
'''



#5. WEEKDAYS

'''
a5= int(input("Enter number from 0 to 6 :"))
if(a5==0):
    print("MONDAY")
elif(a5==1):
    print("TUESDAY")
elif(a5==2):
    print("WEDNESDAY")
elif(a5==3):
    print("THURSDAY")
elif(a5==4):
    print("FRIDAY")
elif(a5==5):
    print("SATURDAY")
elif(a5==6):
    print("SUNDAY")
else:
    print("INVALID NUMBER")
'''

#6.CHECK GIVEN VALUE IS ALPHABET
'''
char=input("Enter your value:")
if((ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122)):
    print(char, "is an alphabet")
else:
    pass
'''

#7.NO. OF DAYS IN MONTH
'''
a7=int(input("Enter Month number:"))
if(a7==1):
    print("January is a 31 day month")
elif(a7==2):
    print("February is a 27 or 28  day month")
elif(a7==3):
    print("March is a 31  day month")
elif(a7==4):
    print("April is a 30  day month")
elif(a7==5):
    print("May is a 31  day month")
elif(a7==6):
    print("June is a 30  day month")
elif(a7==7):
    print("July is a 31 day month")
elif(a7==8):
    print("August is a 31  day month")
elif(a7==9):
    print("September is a 30  day month")
elif(a7==10):
    print("October is a 31 day month")
elif(a7==11):
    print("November is a 30  day month")
elif(a7==12):
    print("December is a 31  day month")
else:
    print("Enter valid detail")
'''




#8.GREATER THAN 10
'''
a8=int(input("Enter your number:"))
if(a8>10):
    print("{} is greater than 10" .format(a8))
elif(a8<10):
    print("{} is smaller than 10" .format(a8))
else:
     print("{} is equals to 10" .format(a8))
'''


#9. VOWELS OR CONSONANT
'''
v=['a','e','i','o','u']
a9=input("Enter your alphabet:")
if(a9 in v):
    print("{} is vowel" .format(a9))
else:
    print("{} is consonant" .format(a9))
'''


#10. LEAP YEAR

'''
year = int(input("Enter your year:"))

if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("{} Is Leap Year" .format(year))
        else:
            print("{} Is NOT Leap Year" .format(year))
    else:
        print("{} Is Leap Year" .format(year))
else:
    print("{} Is NOT Leap Year" .format(year))
'''
