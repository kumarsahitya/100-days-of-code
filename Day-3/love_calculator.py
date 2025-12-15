print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine_names = (name1 + name2).lower()

t = combine_names.count('t')
r = combine_names.count('r')
u = combine_names.count('u')
e  = combine_names.count('e')

true_count = t + r + u + e

l = combine_names.count('l')
o = combine_names.count('o')
v = combine_names.count('v')
e = combine_names.count('e')

love_count = l + o + v + e

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
  print(f'Your score is ' + score + ', you go together like coke and mentos.')
elif score >= 40 and score <= 50:
  print(f'Your score is ' + score + ', you are alright together.')
else:
  print(f'Your score is ' + score + '.')