# Ways to create a dictionary of Lists - Python
di ={}
di["0"]=[1,2]
di[1]=["name",'mon']

print(di)

# Using the zip() Function

k = ["Fruits", "Vegetables", "Drinks"]
val = [["Apple", "Banana"], ["Carrot", "Spinach"], ["Water", "Juice"]]

dis = dict(zip(k,val))
print(dis)

# using for loop and  setdefault()

li = [("Fruits", "Apple"), ("Fruits", "Banana"), ("Vegetables", "Carrot")]

d = {}
for k , item in li:
    d.setdefault(k , []).append(item)

print(d)

# Using Dictionary Comprehension
dicom = {k: [i for _, i in filter(lambda x: x[0] == k, li)] for k in set(k for k, _ in li)}

print(dicom)
