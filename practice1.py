def studentinputfunction(studentlist):
    print("---")
    nb = int(input("Number of student : "))
    for _ in range(nb):
        print("---")
        name = input("Student name : ")
        dob = input("date of birth of student : ")
        stdid = input("Student id : ")
        studentlist.append([name,dob,stdid])

def outofliststudent(studentlist):
    print("+++")
    print(f"number of student in list : {len(studentlist)}")
    for student in studentlist:
        print(f"student name is : {student[0]}")
        print(f"date of birth of student is : {student[1]}")
        print(f"id of student is : {student[2]}")

def courseinput(courselist):
    print("###")
    nc = int(input("Number of course : "))
    for _ in range(nc):
        nameofcourse = input("course name : ")
        idofcourse = input("id of course : ")
        courselist.append([nameofcourse,idofcourse,{}])

def outofcourse(courselist):
    print("###")
    for course in courselist:
        print(f"course name is :{course[0]}")
        print(f"course id is :{course[1]}")

def markinput(courselist,studentlist):
    csid = input("your course id you want to input for student : ")
    cs = None
    for course in courselist:
        if course[1] == csid:
            cs = course
            break
    print(f"course you choose is {cs[0]}")
    for student in studentlist:
        print(f"enter mark for student {student[0]} with id {student[2]} :")
        mark = float(input())
        cs[2][student[2]] = mark

def outofmark(courselist,studentlist):
    print("###")
    courseid = input("enter courseid you want to see : ")
    for course in courselist:
        if course[1]==courseid:
            for student in studentlist:
                mark = course[2].get(student[2],"no information")
                print(f"{student[0]}:{mark}")
            break

def main():
    t = []
    z = []
    while True:
        print("*******")
        print("MENU TOOL")
        print("1.input student information")
        print("2.output student information")
        print("3.input course information")
        print("4.output course information")
        print("5.Input mark ")
        print("6.Output mark ")
        print("7.exit tool")
        choice = int(input("enter your choices : "))
        if choice == 1:
            studentinputfunction(t)
        if choice == 2:
            outofliststudent(t)
        if choice == 3:
            courseinput(z)
        if choice == 4:
            outofcourse(z)
        if choice == 5:
            markinput(z,t)  # Fixed parameter order
        if choice == 6:
            outofmark(z,t)  # Fixed parameter order
        if choice == 7:
            print("EXIT SUCCESSFULL")
            break

main()