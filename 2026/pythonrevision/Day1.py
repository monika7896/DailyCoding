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




















