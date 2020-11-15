import re

pattern = r"color"

if re.match(pattern,"Red is a color , I love red color"):
    print("Matched")
else:
    print("Not matched")    