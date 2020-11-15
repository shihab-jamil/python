studentDetails = {
    "Name" : "Shihab Jamil",
    "Id" : "011 181 180",
    "Dept" : "CSE",
    "CGPA" : "3.83"
}

# print(studentDetails.get("Name", "Not a valid key"))
# print(studentDetails.get("Id", "Not a valid key"))
# print(studentDetails.get("Dept", "Not a valid key"))
# print(studentDetails.get("CGPA", "Not a valid key"))

# for x in studentDetails.values():
#     print(x)

for x, y in studentDetails.items():
    print(x+" : "+y)