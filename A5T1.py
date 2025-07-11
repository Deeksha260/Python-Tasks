students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Eve": 95
}


student_name = input("Enter the student's name to retrieve their marks: ")


if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")
else:
    print(f"Student not found .")