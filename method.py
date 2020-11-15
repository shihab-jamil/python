class student:
    roll =  ""
    gpa = ""

    def setValue(self , roll , gpa):
        self.roll = roll
        self.gpa = gpa
    
    def display(self):
         print(f"Roll : {self.roll}  Gpa : {self.gpa}") 


karim = student()
karim.setValue(101, 3.75)
karim.display()
   