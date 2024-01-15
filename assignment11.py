##1.

# for i in range(1,5,1):
#     for j in range(1,i+1,1):
#         print(i,end="  ")
#     print()



##2.

# for i in range(0,5):
#     num=5
#     for j in range(0,i+1):
#         print(num,end="  ")
#         num-=1
#     print()



##3.

num=1
for i in range(0,5):
    if(num%2==1):
        for j in range(0,i+1):
            print(num,end="  ")
    num+=1
    print()
    





















# for i in range(1,5,1):
#     for j in range(5,i,-1):
#         print(i,end="  ")
#     print()