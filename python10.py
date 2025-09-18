"""numbers=[1,2,3,4,5,6,7,8,9,10]
dl=[number *2 for number in numbers]
print(dl)"""

l= [ i for i in range(1,11)]
print(l)
dl=[i**2  if i%2==0 else i for i in l]

print(dl)