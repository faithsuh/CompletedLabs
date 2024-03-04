student = int(input('Total number of students: '))
scores = input(f'Enter {student} score(s): ').split()

scores = [int(num) for num in scores]


student_count = 0
new_list = scores[0:student]

while len(new_list) < student:
    new_list = input(f'Enter {student} score(s): ').split()
new_list = [int(num) for num in new_list]

new_list = new_list[0:student]
best_score = max(new_list)


for score in new_list:
    student_count += 1
    if score >= best_score - 10:
        print(f'Student {student_count} score is {score} and grade is A')
    elif score >= best_score - 20:
        print(f'Student {student_count} score is {score} and grade is B')
    elif score >= best_score - 30:
        print(f'Student {student_count} score is {score} and grade is C')
    elif score >= best_score - 40:
        print(f'Student {student_count} score is {score} and grade is D')
    else:
        print(f'Student {student_count} score is {score} and grade is F')

