class phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class samsunng(phone):
    def photo(self):
        print("You can take photo")            


s = samsunng()
s.call()
s.message()
s.photo()        