from student import add_course, drop_course, list_courses
from billing import calculate_hours_and_bill, display_hours_and_bill

# Student data
student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
student_in_state = {'1001': True, '1002': False, '1003': True, '1004': False}
course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': []}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

def login(id, s_list):
    """Verify student login credentials."""
    pin = input("Enter PIN: ")
    if (id, pin) in s_list:
        print("ID and PIN verified")
        return True
    else:
        print("ID or PIN incorrect")
        return False

def main():
    """Manage course registration system."""
    s_list = dict(student_list)
    while True:
        id = input("Enter ID to log in, or 0 to quit: ")
        if id == '0':
            break
        if login(id, student_list):
            registered_courses = []
            waitlist = []
            while True:
                print("\n    Select Option: \n" + " -------- ".center(20) +
                    f"\n|{'1: Add Course':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'2: Drop Course':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'3: List Courses':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'4: Show Bill':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'0 to exit:':^20s}|\n" + " -------- ".center(20))

                choice = input()
                if choice == '0':
                    break
                elif choice == '1':
                    course = input("Enter course you want to add: ")
                    if course not in course_hours:
                        print("Course not found")
                    elif id in course_roster[course]:
                        print("You are already enrolled in that course.")
                    elif len(course_roster[course]) < course_max_size[course]:
                        add_course(id, course_roster, course_max_size, registered_courses, course, waitlist)
                        print("Course added.")
                    else:
                        print("Course already full.")
                        waitlist.append(id)
                        print(f"Added {id} to waitlist for {course}.")
                elif choice == '2':
                    course = input("Enter course you want to drop: ")
                    if course not in course_hours:
                        print("Course not found")
                    elif id not in course_roster[course]:
                        print("You are not enrolled in that course.")
                    else:
                        drop_course(id, course_roster, registered_courses, waitlist, course, course_max_size)
                        print("Course dropped.")
                        # Check if there are students on the waitlist for this course
                        if waitlist:
                            next_student = waitlist.pop(0)
                            add_course(next_student, course_roster, course_max_size, registered_courses, course)
                            print(f"{next_student} has been enrolled in {course} from the waitlist.")
                elif choice == '3':
                    list_courses(id, course_roster)
                elif choice == '4':
                    credit_hours, cost = calculate_hours_and_bill(id, student_in_state, course_roster, course_hours)
                    display_hours_and_bill(credit_hours, cost)

if __name__ == '__main__':
    main()
