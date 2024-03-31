# QUESTION 1: As a senior backend engineer at Jovian, 
# you are tasked with developing a fast in-memory data 
# structure to manage profile information (username, name and email) for 
# 100 million users. It should allow the following operations
# to be performed efficiently:

# Insert the profile information for a new user.
# Find the profile information of a user, given their username
# Update the profile information of a user, given their usrname
# List all the users of the platform, sorted by username
# You can assume that usernames are unique.
    
class UesrDatabase:
    def __init__(self) -> None:
        self.users = []
    def insert(self,user):
        self.users.append(user)  
    def find(self,username):
        i = 0
        while i < len(self.users):
            if username == self.users[i][0]:
                
                return self.users[i]
            i += 1
        
    def update(self,user, new_name):
        x = self.find(user)
        x[0] = new_name
        return x
    def list_all(self):
        for user in self.users:
            print(user)


user = [['aakash', 'Aakash Rai', 'aakash@example.com'],
        ['biraj', 'Biraj Das', 'biraj@example.com'],
        ['hemanth', 'Hemanth Jain', 'hemanth@example.com'],
        ['jadhesh', 'Jadhesh Verma', 'jadhesh@example.com'],
        ['siddhant', 'Siddhant Sinha', 'siddhant@example.com'],
        ['vishal', 'Vishal Goel', 'vishal@example.com']]

data = UesrDatabase()
for i in user:
    data.insert(i)
print("===============================")
print(data.find('biraj'))
print("===============================")
print(data.update("aakash", "akash"))
print("===============================")
data.list_all()
print("===============================")