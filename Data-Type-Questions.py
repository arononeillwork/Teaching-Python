# Use this list of grades throughout these questions
grades = [85, 78, 92, 73, 88, 95, 68, 90]

# 1. Calculate the lowest grade
lowest_grade = min(grades)
print(f"\nHighest grade: {highest_grade}")


# 3. Calculate the highest grade from the list
highest_grade = max(grades)


# 4. Calculate the number of grades
number_of_grades = len(grades)

# 4. Calculate the total of grades
total_grade = sum(grades)


# 4. Calculate the average grade.
# First, how do you do that in english?
# total / number of grades
average_grade = sum(grades) / len(grades)

# OR by reusing a variable - easier to read
average_grade = total_grade / number_of_grades



# 5. Count the number of grades which are 70 and above. 

number_of_passing_grades = 0 
for grade in grades:
    if grade >= 70:
        number_of_passing_grades = number_of_passing_grades + 1

print(f"\nThe number of grades above 70 were: {number_of_passing_grades}")



# 5. Count the number of grades which are 70 and above. 

number_of_passing_grades = 0 
for grade in grades:
    if grade <= 70:
        number_of_passing_grades = number_of_passing_grades + 1

print(f"\nThe number of grades below 70 were: {number_of_passing_grades}")






# 7. Sort the grades in ascending order.
# Question: Write a Python function to return the grades sorted in ascending order.
sorted_grades = sorted(grades)
# Explanation: The 'sorted' function returns a new list of grades sorted in ascending order.
print(f"Sorted grades (ascending): {sorted_grades}") 



# 8. Sort the grades in descending order.
# Question: Write a Python function to return the grades sorted in descending order.
sorted_grades_desc = sorted(grades, reverse=True)
# Explanation: The 'sorted' function with 'reverse=True' returns the list sorted in descending order.
print(f"Sorted grades (descending): {sorted_grades_desc}")