class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # default value, not provided in the constructor
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User('001', 'angela')
user1.id = '001'
user1.username = 'angela'

print(user1.username)
print(user1.id)

user2 = User('002', 'john')


user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)


