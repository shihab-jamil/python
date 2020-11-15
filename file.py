file = open("student.txt","a")



file.write("\nThasin       ----- 011 181 150")

file.close()

file = open("student.txt","r")

text = file.read()

print(text)