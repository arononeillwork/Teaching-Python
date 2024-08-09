"""
LIST Questions
"""





# Use this list of grades throughout these questions
grades = [85, 78, 92, 73, 88, 95, 68, 90]




# Print the 1st grade from the list
first_grade = grades[0]
print(f"\nFirst grade: {first_grade}")

# Find the last grade in the list.
last_grade = grades[-1]
print(f"\nLast grade: {last_grade}")




# Calculate the lowest grade
lowest_grade = min(grades)
print(f"\nHighest grade: {highest_grade}")


# Calculate the highest grade from the list
highest_grade = max(grades)


# Calculate the number of grades
number_of_grades = len(grades)

# Calculate the total of grades
total_grade = sum(grades)


# Calculate the average grade.
# First, how do you do that in english?
# total / number of grades
average_grade = sum(grades) / len(grades)

# OR by reusing a variable - easier to read
average_grade = total_grade / number_of_grades



# Count the number of grades which are 70 and above. 

number_of_passing_grades = 0 
for grade in grades:
    if grade >= 70:
        number_of_passing_grades = number_of_passing_grades + 1

print(f"\nThe number of grades above 70 were: {number_of_passing_grades}")



# Count the number of grades which are 70 and above. 

number_of_passing_grades = 0 
for grade in grades:
    if grade <= 70:
        number_of_passing_grades = number_of_passing_grades + 1

print(f"\nThe number of grades below 70 were: {number_of_passing_grades}")






# Sort the grades in ascending order.
sorted_grades = sorted(grades)
print(f"Sorted grades (ascending): {sorted_grades}") 



# Sort the grades in descending order.
sorted_grades_desc = sorted(grades, reverse=True)
print(f"Sorted grades (descending): {sorted_grades_desc}")