print("Hi , I'm monika")
msg = "good morinig"
# stripping
lstr = "    monika"
rstr = "yadav         "
st = "          MY           "
print(lstr.lstrip() ,rstr.rstrip()  , st.strip() )
# data types
# numbers
print(5+4)
age=23
print( "my age is " + str(age))
nums="27"
print( "my age is " + nums)
teams = ["mon" ,"nidhi" ,26 ,22 , 24]
print(teams)
# change , add  remove list elements
teams[0]="riya" 
print(teams)
# add elemen at last
teams.append("sneha")
print(teams)
# add elemen at particaluar idex
teams.insert(1 , 24)
print(teams)
# removing element
# permanent delte so can not use this value
del teams[0]
print(teams)
# use pop if you want to resue the var
c = teams.pop(1)
print(c, teams)
# remove it by value
teams.remove(24)
print(teams)
# sort list it is permamane sort
cars =["BMW","Audi","Thar"]
cars.sort(reverse=True)
print(cars)
# sort a list temporary
cars2 =["BMW","Audi","Thar" , "Maruti","i10"]
print(sorted(cars2))
print(cars2.reverse())
print( len(cars2))
# for loop
for i in range(1,6):
    print(i)
    
num = list(range(4,11,2))
print(num)

square = []
for i in range(1,11 ):
    sq=i**2
    square.append(sq)
print(square)
print(min(square))
print(max(square))
print(sum(square))
# list compransion
sqare_c = [ i**2  for i in range(11)]
print(sqare_c)
# slicing
print(square_c[0:6])
print(square_c[:6])
print(square_c[2:6])
# loop to subset only
for i in square_c[0:3]:
    print(i)
    
# copy entire list using slicing
square_copy= square_c[:]
square_copy.append(12121)
print(square_copy)
print(square_c)


import array as arr

# 'i' specifies signed integer type
my_array = arr.array('i', [1, 2, 3, 4, 5])
print(my_array)


day = int(input("Enter a number (1-7): "))

# Match-case (Python 3.10+ feature) to act like a switch
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        # Default case if no match
        print("Invalid")












































