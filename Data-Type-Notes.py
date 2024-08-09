"""
What we learned before:

Data types - the type of data stored (int, float, string)

Variables - Are used to store data values
          - their value is assigned by = 
          - their value can change over time

Examples of data types:
Integer 
Float
String


"""

# Integer
age = 30
print(f"\nInteger example: {age} - must be a whole number")

# Float
height = 130.4
print(f"\nFloat example: {height} - can have a decimal point")

# String
name = "aron4"
print(f"\nString example: " + name + " - can store any character")










"""
We have a new one to add called list

"""

grades = [85, 78, 92, 73, 88, 95, 68, 90]

print(f"\nGrades example: {grades} - multiple values of any data type")


"""
In Programming, the elements within a list are viewed as this:

list = [key: value, key: value]


key - number used to retrieve the N listed number from the list

value - a variable with any data type

"""

list_example = ["string1", "string2", "string3", "string4"]

               [    0,         1,         2,         3    ]



# So, the 1st element in programming, is retrieved by using the key 0.
# Print the 1st grade from the list
first_grade = grades[0]
print(f"\nFirst grade: {first_grade}")


# Print the 5th grade from the list
fifth_grade = grades[4]
print(f"\nFifth grade: {fifth_grade}")



# Print the last grade in the list.
# To access the last value from a list, we use -1
last_grade = grades[-1]
print(f"\nLast grade: {last_grade}")
















"""
EXTRA NOTES

You can have a list of any type
"""



# List of Integers
int_list = [1, 2, 3, 4, 5]

# List of Float values
float_list = [1.1, 2.2, 3.3, 4.4, 5.5]

# List of Strings
string_list = ["apple", "banana", "cherry"]



















# Boolean example

# A boolean is simply a true or false result

# List of Mixed Data Types
mixed_list = [25, "hello", 3.14, True]
# Explanation: A list containing different data types (int, string, float, boolean).