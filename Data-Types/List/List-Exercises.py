# Use this list of grades throughout these questions
grades = [85, 78, 92, 73, 88, 95, 68, 90]




# 7. Find the third grade in the list.
third_grade = grades[2]
print(f"\nThird grade: {third_grade}")


# 2. Find & print the range of the grades.


# 3. Count the number of failing grades (below 50).
number_of_failing_grades = sum(1 for grade in grades if grade < 60)
print(f"\nNumber of failing grades: {number_of_failing_grades}")


# 3. Find the difference between the first and last grade in the list.
grades = sorted(grades)
difference_first_last = grades[-1] - grades[0]
print(f"\nDifference between first and last grade: {difference_first_last}")


# 7. Store the grades above the average.
grades_above_average = [grade for grade in grades if grade > average_grade]
print(f"\nGrades above average: {grades_above_average}")

