class bike:
    
    def __init__(self , name , color):
        self.name = name
        self.color = color

    def __str__(self):
        return (f"Name = {self.name}  Color = {self.color}")

    

bike1 = bike("Yamaha R15","Blue")        
bike2 = bike("Yamaha R15","Blue")        
print(bike1)