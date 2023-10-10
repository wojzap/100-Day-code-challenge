# numbers = [1, 2, 3]
# new_numbers = [number + 1 for number in numbers]
# print(new_numbers)
#
# name = "Angela"
# list = [letter for letter in name]
# print(list)
#
# doubled = [number*2 for number in range(1,5)]
# print(doubled)
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)


passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)