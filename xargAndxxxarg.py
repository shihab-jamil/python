#xarg
def add(*numbers):
    sum = 0
    for i in numbers:
        sum += i

    return sum    


#xxargs
def addition(**details):
    print(details["id"])

print(add(10,20,30) )
addition(id="180",name="Shihab Jamil")  