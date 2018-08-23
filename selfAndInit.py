class User1:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False

    def displayInfo(self):
        print(self.name)
        print(self.email)
    
user1 = User1("Anna Propas", "anna@anna.com")
print(user1.name)
print(user1.logged)
print(user1.email)
user1.displayInfo()

""" 
class User2:
    name="Anna"
anna = User2()
print("anna's name:", anna.name)                            
User2.name = "Bob"
print("anna's name after change:", anna.name)               
bob = User2()
print("bob's name:", bob.name)  """