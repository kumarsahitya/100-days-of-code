class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def __str__(self):
        return f"User(username={self.username}, id={self.id})"

    def follow(self, user):
        if user != self:
            self.following += 1
            user.followers += 1
            print(f"{self.username} is now following {user.username}.")
        else:
            print("You cannot follow yourself.")

user1 = User("001", "Alice")
user2 = User("002", "Bob")
user1.follow(user2)
user2.follow(user1)

print(user1)
print(user2)