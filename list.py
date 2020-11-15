
n = int(input("How many elements: "))

list = []
for i in range(0,n,1):
    elmnt = int(input())
    list.append(elmnt)


list.reverse()

print(list)
