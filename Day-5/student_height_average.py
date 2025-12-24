# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_of_heights = 0

for student_height in student_heights:
    sum_of_heights += student_height

print(f"total height = {sum_of_heights}")

count = 0

for student in student_heights:
    count += 1

print(f"number of students = {count}")
print(f"average height = {round(sum_of_heights / count)}")
