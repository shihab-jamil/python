num1 = {1,2,3,4,4,4}
num2 = set([5,6,7,7])

num1.add(7)
num1.remove(4)

print(num1 | num2)  #union
print(num1 & num2)  #intersection
print(num1 - num2)  #set difference
