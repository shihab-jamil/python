class student:
    roll =  ""
    gpa = ""

    def __init__(self , roll , gpa):
        self.roll = roll
        self.gpa = gpa
    
    def display(self):
         print(f"Roll : {self.roll}  Gpa : {self.gpa}") 


karim = student(101, 3.75)
karim.display()
   