import random 
from datetime import datetime

#Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def main():
    print("==== Student Report Card Generator ====")
    #Random unique report ID
    report_id = random.randint(1000, 9999)

    student_name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    #if user leaves roll number blank, assign a random one
    if roll_number.strip() == "":
        roll_number = f"RN{random.randint(100,999)}"

    #Current date
    current_date = datetime.now().strftime("%Y-%m-%d / %H:%M:%S")

    subjects = {}
    n = int(input("Enter number of subjects: "))


    for i in range(n):
        subject = input(f"Enter name of subject {i+1}: ")
        marks = int(input(f"Enter marks obtained in {subject}: "))
        subjects[subject] = marks

    #prepare report card
    report_lines = []
    report_lines.append("==== Student Report Card ====")
    report_lines.append(f"Report ID: {report_id}")
    report_lines.append(f"Date: {current_date}")
    report_lines.append(f"Student Name: {student_name}")
    report_lines.append(f"Roll Number: {roll_number}")
    report_lines.append("------------------------------")
    total = 0
    for subject, marks in subjects.items():
        grade = calculate_grade(marks)
        report_lines.append(f"{subject}: {marks} ({grade})")
        total += marks

    average = total / n if n > 0 else 0
    overall_grade = calculate_grade(average)

    report_lines.append("------------------------------")
    report_lines.append(f"Total Marks: {total}/{n*100}")
    report_lines.append(f"Average Marks: {average:.2f}")
    report_lines.append(f"Overall Grade: {overall_grade}")
    if overall_grade == "F":
        report_lines.append("Status: Fail")
    else:
        report_lines.append("Status: Pass") 
       #print to console
        print("\n".join(report_lines))
    report_lines.append("==============================")

    # Save report card to a text file 
    filename = f"reportcard_{report_id}.txt"
    with open(filename, "w") as f:
        f.write("\n".join(report_lines))

    print("Report card generated successfully!")

if __name__ == "__main__":
    main()