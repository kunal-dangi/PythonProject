class User:
    def __init__(self , user_id , username):
        self.id = user_id
        self.name = username
        self.follower = 0
        self.following = 0


    def Follow(self , user):
        user.follower += 1
        self.following += 1





user_1 = User("001" , "Mia")
user_2 = User("002" , "Lucy")
user_1.Follow(user_2)

print(user_1.id , user_1.name)
print(user_2.id , user_2.name)


print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)