class User:
    def __init__(self,username, name, email) -> None:
        self.username=username
        self.name=name
        self.email=email
        print("user craeated")
    def into_(self,g_name):
        print(f"hi {g_name} i am {self.name} contact me {self.email}")
    def __repr__(self) -> str:
        return f"[print from reper] ==== usdrname {self.username} contact {self.email}"
    def __str__(self) -> str:
        return self.__repr__()
    # repr and str are used for string representation 
user1 = User('jhon','jhon D','jhon.com') 
print(user1)
print(user1.username)
print(user1.name)
print(user1.email)
user1.into_("kali")

# aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
# biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
# hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
# jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
# siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
# sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
# vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
# users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
# print(aakash.username)
# print(aakash.name)