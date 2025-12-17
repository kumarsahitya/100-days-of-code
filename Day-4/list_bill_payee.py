names_string = "user1, user2, user3, user4, user5"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

payeeIndex = random.randint(0, len(names) -1);

print(f'{names[payeeIndex]} is going to buy the meal today!')