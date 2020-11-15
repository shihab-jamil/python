def vote(age):
    if age < 18:
        raise ValueError("Invalid voter")
    else:
        return "You are allowed to vote"


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

try:
    result = num1/num2
    print(result)
    print(vote(17))

except (ValueError , ZeroDivisionError) as e:
    print(e)

finally:
    print("Successfull")