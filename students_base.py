from time import sleep

# Transfering user to the current function
def transfer():
    if action == 1:
        print(count_all_students())
    elif action == 2:
        print(count_average_by_subject())
    elif action == 3:
       rating()
    return

# First action
def count_all_students():
    with open("files/student_performance.csv") as f:
        all_students = len([line.split(",")[0][1:-1] for index, line in enumerate(f) if index != 0])
    return f"Currently students amount is {all_students}"

# Second action
def count_average_by_subject():

    print("""\nChoose subject:\n
    1 math
    2 reading
    3 writing\n""")
    subject = input("Enter subject number: ")

    # Checking input
    if subject.isdigit() == True:
        subject = int(subject)
    else:
        return f"Enter number, not string, your input is {subject}"
    if subject > 3 or subject < 1:
        return f"Enter only numbers in interval from 1 to 3, your number is {subject}"

    # Algoritnm starts
    with open("files/student_performance.csv") as f:

        if subject == 1:
            index_subject = subject+4
            subject = "math"
        elif subject == 2:
            index_subject = subject+4
            subject = "reading"
        elif subject == 3:
            index_subject = subject+4
            subject = "reading"
        
        filtering_by_subject = [int(line.strip().split(",")[index_subject][1:-1]) for index, line in enumerate(f) if index != 0]
        mean_by_subject = round(sum(filtering_by_subject)/len(filtering_by_subject), 2)

    return f"Mean by {subject} is {mean_by_subject} points"

def rating():
    with open("files/student_performance.csv") as f:
        # Data searching
        mean_by_each = [[index, round((int(line.split(",")[5][1:-1])+int(line.split(",")[6][1:-1])+int(line.strip().split(",")[7][1:-1])) / 3, 3)] for index, line in enumerate(f) if index != 0]
        filtered_mean = sorted(mean_by_each, key = lambda x: x[1], reverse = True)
        only_results = list(map(lambda x: x[1], mean_by_each))

        
        # Max result operations
        max_result = max(filtered_mean, key = lambda x: x[1])[1]
        count_max_result = only_results.count(max_result)
        print(f"\nMax result is {max_result}, number of students got max result is {count_max_result}")

        # Min result operations
        min_result = min(only_results)
        count_min_result = only_results.count(min_result)
        print(f"Min result is {min_result}, number of students got min result is {count_min_result}\n")

        # Best 10
        print("Best 10 students:")
        for index, n in enumerate(filtered_mean[:10]):
            place_space = " "*index
            print(place_space,f"{index+1} place: Student`s id: {n[0]} Points: {n[1]}")
    return

while True:
    # Action chosen by user
    print("""Actions:\n
    1 Count all students
    2 Count mean by subject
    3 Rating by subject\n""")

    action = input("Enter number: ")
    if action.isdigit() == True:
        print("Loading...")
        sleep(0.5)
        action = int(action)
        transfer()
    else:
        print(f"Enter number, not string, your input is {action}")

    # Continue asking
    continue_request = input("\nDo you want continue?(y/n)")
    if continue_request == "n":
        exit()
    print("Loading...")
    sleep(1)
