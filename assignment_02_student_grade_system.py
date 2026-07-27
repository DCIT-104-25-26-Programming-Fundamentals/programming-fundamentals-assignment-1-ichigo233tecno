def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

    if __name__ == "__main__":
        score = float(input("Enter the student's score: "))
        grade = get_grade(score)
        print(f"The student's grade is: {grade}")

