def even(x):
    if x%2 == 0:
        return x

num = [1 , 2 ,3 , 4 , 5 , 6, 7 , 8 , 9 ,10]

result = list(filter(lambda x: x%2==0,num))
print(result)
