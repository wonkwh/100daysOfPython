# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
print(max(student_scores))

max_score = 0
for score in student_scores:
    if max_score < score:
        max_score = score

print(f"The highest score in the class is: {max_score}")

# for loop with range
for number in range(1, 11):
    print(number)

# 5-3 adding evens
sum_of_evens = 0
for num in range(1, 101):
    if num % 2 == 0:
        sum_of_evens += num

sum_of_evens = 0
for num in range(2, 101, 2):
    sum_of_evens += num
print(f"{sum_of_evens}")
