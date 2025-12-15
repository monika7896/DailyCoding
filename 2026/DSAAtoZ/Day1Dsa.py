# all type of patters

n = int(input("Enter N: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()



for i in range(n+1):
    print("*" * i)

class Sol:
    def star_pattern(self,n):
        for i in range(1, n+1):
            # print(i)
            for j in range(1, i+1):
                print(j , end=" ")
            print()

sol = Sol()
N = 5
# Call pattern function
sol.star_pattern(N)


class Sol:
    def star_pattern4(self,n):
        for i in range(1, n+1):
            # print(i)
            for j in range( 1,i+1):
                print(i , end=" ")
            print()

sol = Sol()
N = 5
# Call pattern function
sol.star_pattern4(N)
    