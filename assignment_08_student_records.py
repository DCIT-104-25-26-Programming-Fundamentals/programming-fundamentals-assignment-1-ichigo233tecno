def display_menu():
    """Print the menu options."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Prompt for student details and add a new record to the list."""
    name = input("Student name: ")
    student_id = input("Student ID: ")

    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(num_scores):
        score = int(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimals."""
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)


def display_all_students(students):
    """Print a formatted table of every student's name, ID, scores, average."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(str(s) for s in student["scores"])
        avg = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{avg:<10}")

    print("-" * 50)


def find_student_average(students):
    """Ask for a student ID, then display that student's average score."""
    search_id = input("Enter student ID: ")

    for student in students:
        if str(student["id"]) == search_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg}")
            return

    print("Error: No student found with that ID.")


if __name__ == "__main__":
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            find_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a number between 1 and 4.")