# Class Creations and Objects Initialization
# class User:
#     def __init__(self, user_id, username, user_role):
#         self.id = user_id
#         self.name = username
#         self.role = user_role
#         self.Competency = "High"
#         print("New user Created")
        

# user1 = User("001", "Adam Shaha", "Software Developer")
# user2 = User("002", "Faisal Dengwa", "Programmer")

# print(f"ID: {user1.id}")
# print(f"Name: {user1.name}")
# print(f"Role: {user1.role}")
# print(f"Competency: {user1.Competency}")

# print(f"ID: {user2.id}")
# print(f"Name: {user2.name}")
# print(f"Role: {user2.role}")
# print(f"Competency: {user2.Competency}")

class User:
    def __init__(self, user_id, username, user_role):
        self.id = user_id
        self.name = username
        self.role = user_role
        self.followers = 0
        self.following = 0
        print("New user Created")

    def follow(self, user):
        user.followers +=1
        self.following +=1

user1 = User("001", "Adam Shaha", "Software Developer")
user2 = User("002", "Faisal Dengwa", "Programmer")

user1.follow(user2)     
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

        


# print(f"ID: {user1.id}")
# print(f"Name: {user1.name}")
# print(f"Role: {user1.role}")

# print(f"ID: {user2.id}")
# print(f"Name: {user2.name}")
# print(f"Role: {user2.role}")
