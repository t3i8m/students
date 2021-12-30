import string

# datas
students_grade_report = {
    'Jhon Watson': {'math': [10, 8, 9], 'chemistry': [10, 6, 4]}, 
    'Sherlok Holmes': {'math': [10, 10, 10]}, 
    'James Bond': {'chemistry': [10, 3, 6]}, 
    'James Lebron': {'math': [10, 5, 9], 'physic': [10, 8, 9], 'sport': [10, 10, 10]}, 
    'Santa Claus': {'math': [10, 10, 10], 'chemistry': [10, 10, 10], 'physic': [10, 10, 10], 'sport': [3, 7, 5]}, 
    'Marry Popins': {'math': [10, 9, 10], 'chemistry': [10, 8, 10], 'sport': [9, 8, 7]}, 
    'Carlson': {'math': [10, 4, 7], 'chemistry': [7, 6, 8], 'sport': [4, 5, 4]}, 
    'Leonardo da Vinci': {'math': [10, 10, 10], 'chemistry': [10, 10, 10]}}

all_subjects = ["math", "chemistry", "physic", "sport"]
symbols = list(string.ascii_lowercase)+list(string.punctuation)

def find_opertaion(user_input):
    print("\nLoading...")
    if user_input.lower() in symbols:
        print("You have to pick number of the current operation")
        # action()
    elif int(user_input) == 1:
        name = input("Enter student`s Name and Surname: ")
        subject = input("Enter subject: ")
        grades = converting(list(input("Enter grades: ")))
        append_datas(name, subject, grades)
    elif int(user_input) == 2:
        name = input("Enter student`s Name and Surname: ")
        find_student(name,students_grade_report)
    elif int(user_input) == 3:
        current_subject(input("Enter subject: "), students_grade_report)
    elif int(user_input) == 4:
        print(students_grade_report)
    elif int(user_input) == 5:
        removing(input("Enter student`s Name and Surname: "))
    elif int(user_input) == 6:
        rating()
    else:
        print("You have to pick number of the current operation")

        

def converting(grades):
    grades_converted = []
    if len(grades) <= 2:
        grades_converted.append(int(str(grades[0])))
        return grades_converted
    if int(str(grades[-2])+str(grades[-1])) in range(1, 11):
        for index, n in enumerate(grades):
            if n != " ":
                if index+1 < len(grades):
                        if int(str(n)+grades[index+1]) in range(0,11):
                            if int(n) not in [1,0] and grades[index+1] != 0:
                                grades_converted.append(int(n))
                            elif int(n) == 1:
                                grades_converted.append(10)
                            elif int(n) == 1 and int(grades[index+1]) == 0:
                                grades_converted.append(1)
                        else:
                            print("Grade cannot be more than 10, or equal,less than zero")
                            action()
                elif int(n) != 0:
                    grades_converted.append(int(n))
        return grades_converted
    else:
        print("Grade cannot be more than 10, or equal,less than zero")
        action()

def append_datas(name, subject, grades):
    if name not in students_grade_report:
        students_grade_report[name] = {subject:grades}
        print("Successfully added!")
    else:
        students_grade_report[name].update({subject:grades})
        print("Successfully updated!")
    return students_grade_report

def find_student(name, students):
    if name in students:
        print(f"{name} grade report: ",students[name])
    else:
        print("Student not found")

def current_subject(subject, students):
    names = [name for name, value in students.items() if subject in value]
    all_marks = [n for mark in students.values() if subject in mark for n in mark[subject]]
    average_mark = round(sum(all_marks)/len(all_marks),2)
    average_by_person = [[round(sum(value[subject])/len(value[subject]),2), key]for key, value in students.items() if subject in value]
    average_by_person.sort(reverse = True)
    print(f"""
    Students: {names}
    Average mark: {average_mark}
    Best student: {average_by_person[0][1]} - average mark: {average_by_person[0][0]}
    Worst student: {average_by_person[-1][1]} - cverage mark: {average_by_person[-1][0]}\n""")

def removing(student_datas):
    if student_datas in students_grade_report:
        del(students_grade_report[student_datas])
        print("Student removed successfully!")
    else:
        print("Student not found in the list")

def rating():
    # uploading datas from dictionary into lists
    all_students = [[students_grade_report[name][n], name] for name in students_grade_report.keys() for n in all_subjects if n in students_grade_report[name]]
    average_students = [[all_students[index][1],round((sum(all_students[index][0]))/(len(all_students[index][0])), 2)] for index in range(len(all_students))]
    count_indexes = list()
    all_students = [[first[1]+second[1], first[0]] for first, second in zip(average_students, average_students) if first[0] == second[0]]
    # sorting algorithm
    # 1 part - count element in the list
    for index,n in enumerate(all_students):
        if len(all_students) > index+1:
                if all_students[index][1] != all_students[index+1][1]:
                    count_indexes.append([item for sublist in all_students for item in sublist].count(n[1]))
        else:
            count_indexes.append([item for sublist in all_students for item in sublist].count(n[1]))
    # 2 part - sorting all_students list
    for k in range(len(all_students)):
        for index, n in enumerate(all_students):
            if len(all_students) > index+1:
                if all_students[index][1] == all_students[index+1][1]:
                    all_students[index][0] += all_students[index+1][0]
                    all_students.pop(index+1)
    average_by_student = sorted([[round(n[0]/(index*2),2), n[1]] for n, index in zip(all_students, count_indexes)], reverse = True)
    average_mark_all = round(sum([n[0] for n in average_by_student])/len(average_by_student),2)
    # printing graphic
    print(f"\nAverage mark in all subjects is {average_mark_all}")
    print("Average raiting:\n")
    for index, n in enumerate(average_by_student):
        row = int(index)*" "
        if len(average_by_student) > index+1:
            if average_by_student[index][0] == average_by_student[index+1][0]:
                print(f"{row} {index+1} {n[1]} {n[0]}")
                print(f"{row} {index+2} {average_by_student[index+1][1]} {average_by_student[index+1][0]}")
            elif average_by_student[index][0] != average_by_student[index+1][0] and average_by_student[index][0] != average_by_student[index-1][0]:
                print(f"{row} {index+1} {n[1]} {n[0]}")
        else:
            print(f"{row} {index+1} {n[1]} {n[0]}")
             

def action():
    find_opertaion(input("""\nChoose operation (enter number):\n
    1 add new student
    2 find student
    3 information about current subject
    4 view all students
    5 remove student
    6 rating by average mark\n
    Action: """))


while True:
    action()
    request = input("\nDo you want to continue? ")
    if request.title() != "Yes":
        print("Exiting...")
        exit()

        
