'''
_Assignment: Classes, Objects, and Python Data Types
This script demonstrates the use of classes, objects, and various Python data types.
It includes a Student class with methods to add grades, calculate averages, and display information.
It also shows how to work with dictionaries and sets in the context of Student objects.
'''

# Importing 're' (regular expressions) for the bonus email validation section
import re
import sys
sys.stdout.reconfigure(encoding='utf-8') # to make special characters display w/o error


# PART 1: Class Definition
# ─────────────────────────────────────────────────

class Student:
    """
    A class representing a student with name, email, and grades.
        Provides methods to add grades, calculate averages, and display student information.
    """
    def __init__(self, name, email, grades):
        self.name = name        # Store the name string on this object
        self.email = email      # Store the email string on this object
        self.grades = grades    # Store the grades list on this object

    def add_grade(self, grade):
        """
        Add a grade to the student's grades list.
                Args:
            grade: An integer grade value to append.
        """
        self.grades.append(grade)   # .append() adds the item to the end of the list

    def average_grade(self):
        """
        Calculate the average of the student's grades.
                Returns:
            The average grade as a float, or 0 if no grades exist.
        """
        if len(self.grades) == 0:   # Guard against dividing by zero if no grades exist
            return 0
        return sum(self.grades) / len(self.grades)  # Average = total / count

    def display_info(self):
        """
        Display the student's information including name, email, grades, and average.
        """
        print(f"Name:    {self.name}")
        print(f"Email:   {self.email}")
        print(f"Grades:  {self.grades}")
        print(f"Average: {self.average_grade():.2f}")  # :.2f formats to 2 decimal places
        print()  # Blank line for readability


    def grades_tuple(self):
        """
        Convert the student's grades list to a tuple.
                Returns:
            A tuple containing all the student's grades.
        """
        return tuple(self.grades)



# PART 2: Working with Objects
# ─────────────────────────────────────────────────

print("=" * 40)
print("PART 2: Student Objects")
print("=" * 40)

# Create 3 Student objects by calling Student(name, email, grades).
# Each call runs __init__ and gives us back a fully built object.
student1 = Student("Kathy Booth",  "kathy@school.com",  [99, 92, 95])
student2 = Student("Andrea Heffernan",   "andrea@school.com",  [91, 85, 97])
student3 = Student("NaYoung Song",  "nayoungatschool.com",  [75, 68, 80])

# Add 2 new grades to each student using the add_grade method.
# This calls .append() internally and modifies each student's grades list in place.
student1.add_grade(94)
student1.add_grade(98)

student2.add_grade(88)
student2.add_grade(93)

student3.add_grade(60)
student3.add_grade(78)

# Print info for each student.
# display_info() prints name, email, grades, and average — all in one method call.
student1.display_info()
student2.display_info()
student3.display_info()



# PART 3: Dictionary & Set Integration
# ─────────────────────────────────────────────────

print("=" * 40)
print("PART 3: Dictionary & Set")
print("=" * 40)

# A dictionary maps keys -> values. Here each key is an email string,
# and each value is the corresponding Student object.
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3,
}

# Print the dictionary to show all email -> student mappings.
# We loop with .items() because printing the raw dict would show ugly memory addresses
# for the Student objects instead of their actual names.
print("Student Dictionary (email -> student name):")
for student_email, student in student_dict.items():
    print(f"  {student_email} -> {student.name}")
print()

# --- Function: get_student_by_email ---
# .get(email) returns the Student object if the email exists, or None if it doesn't.
# This is "safe" because it won't crash with a KeyError like student_dict[email] would.
def get_student_by_email(email):
    """
    Retrieve a Student object by email address.
        Args:
        email: The email address to look up in the student dictionary.
    Returns:
        The Student object if found, or None if the email does not exist.
    """
    return student_dict.get(email)  # Returns None automatically if key is missing

# Demonstrate the lookup function with an email that EXISTS and one that DOESN'T
found = get_student_by_email("kathy@school.com")
if found:                    # 'if found' is True when the object is not None
    print(f"Found student: {found.name}")

not_found = get_student_by_email("unknown@nowhere.com")
print(f"Unknown email lookup result: {not_found}")   # Should print None
print()

# Build a SET of all unique grades across every student.
# A set automatically removes duplicate values — no grade appears twice.
# We use a set comprehension: for each student, for each grade in their list, add it.
all_grades_set = {grade for student in student_dict.values() for grade in student.grades}
print(f"All unique grades across all students: {sorted(all_grades_set)}")
# sorted() just makes the output easier to read; sets themselves have no order
print()



# PART 4: Tuple Practice
# ─────────────────────────────────────────────────

print("=" * 40)
print("PART 4: Tuples & Immutability")
print("=" * 40)

# Call grades_tuple() on student1 — this returns a tuple version of her grades list.
s1_tuple = student1.grades_tuple()
print(f"{student1.name}'s grades as a tuple: {s1_tuple}")

# Tuples are IMMUTABLE — you cannot change their values after creation.
# We try to assign to index 0 inside a try/except block.
# If Python raises a TypeError, we catch it and print a friendly message.
try:
    s1_tuple[0] = 99    # Intentionally showing that this line WILL raise a TypeError
except TypeError as e:
    print(f"Cannot modify tuple — tuples are immutable! Error: {e}")
print()



# PART 5: List Operations
# ─────────────────────────────────────────────────

print("=" * 40)
print("PART 5: List Operations")
print("=" * 40)

# Put all three students in a plain list so we can loop over them easily
all_students = [student1, student2, student3]

for student in all_students:
    # .pop() with no argument removes AND returns the LAST item in the list.
    # This changes the list permanently — the grade is gone after this line.
    removed = student.grades.pop()
    print(f"{student.name}: removed last grade -> {removed}")

    # Index [0] accesses the very first item in the list (Python lists start at 0).
    first_grade = student.grades[0]

    # Index [-1] is a Python shortcut that always means the LAST item, no matter the length.
    last_grade = student.grades[-1]

    print(f"  First grade: {first_grade}  |  Last grade: {last_grade}")

    # len() returns the number of items currently in the list.
    print(f"  Number of grades recorded: {len(student.grades)}")
    print()



# PART 6: Bonus — Email Validation & Grade Count
# ─────────────────────────────────────────────────

print("=" * 40)
print("PART 6: Bonus")
print("=" * 40)

# re.match() checks whether a string matches a pattern starting from the beginning.
# Pattern breakdown:
#   ^         — start of the string
#   [^@\s]+   — one or more characters that are NOT '@' or whitespace (the local part)
#   @         — literal '@' symbol
#   [^@\s]+   — one or more characters (the domain name)
#   \.        — literal dot (backslash escapes the dot so it's not "any character")
#   [^@\s]+   — one or more characters (the TLD, e.g. "com")
#   $         — end of the string
EMAIL_PATTERN = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'

print("Email validation:")
for student in all_students:
    # re.match returns a Match object if valid, or None if it doesn't match
    is_valid = re.match(EMAIL_PATTERN, student.email) is not None
    status = "✅ valid" if is_valid else "❌ invalid"
    print(f"  {student.email} — {status}")
print()

# Count how many grades are above 90 across ALL students.
# We use a generator expression inside sum():
# For every student, for every grade in their list, add 1 if grade > 90.
grades_above_90 = sum(1 for student in all_students for grade in student.grades if grade > 90)
print(f"Total grades above 90 across all students: {grades_above_90}")
