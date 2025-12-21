n=5
for i in range(n,0,-1):
    # print(i ,end=" ")
    for j in range(1,i+1):
        print(j ,end=" ")
    print()


for i in range(n ,1,-1):
    for j in range(1,i+1):
        print( "*", end=" ")
    print()
    

for i in range(1, n + 1):
    # print spaces
    print(" " * (n - i), end="")
    
    # print stars
    print("*" * (2 * i - 1))


for i in range(n ,1,-1):
    
    # print stars
    print("*" * (2 * i - 1))


print("------------------------------")

for i in range(1, n + 1):

    
    # print stars
    print("*" * (2 * i - 1))


for i in range(n, 0, -1):
    # print leading spaces
    print(" " * (n - i), end="")
    
    # print stars
    print("*" * (2 * i - 1))

    
for i in range(n, 0, -1):
    # print leading spaces
    print(" " * (n - i), end="")
    
    # print stars
    print("*" * (2 * i - 1))

n = 9
for i in range (1,n+1):
    print(" " * (n - i) +  "*" * (2*i - 1))

for i in range( n-1,0,-1):
    print( " " * (n-i) +  "*" * (2 * i -1) )
    


n = 9
for i in range (1,n+1):
    print("" * (n - i) +  "*" * (2*i - 1))

for i in range( n-1,0,-1):
    print( "" * (n-i) +  "*" * (2 * i -1) )
    

# 01 pyramid
for i in range (n):
    if i%2 == 0:
        start = 1
    else:
        start=0
    for j in range(i+1):
        print(start , end="")
        start= 1 - start
    print()



for i in range (n):
    if i%2 == 0:
        start = 1
    else:
        start=0
    for j in range(i+1):
        print(start , end=" ")
        start= 1 - start
    print()