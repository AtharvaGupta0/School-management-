import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="pyuser",
    password="",
    database="test"
)
def add_student():
    name = input("Name: ")
    student_class = input("Class: ")
    marks = int(input("Marks: "))
    username = input("Username: ")
    password = input("Password: ")

    query = """
    INSERT INTO students (name, class, marks, username, password)
    VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(query, (name, student_class, marks, username, password))
    conn.commit()
    print("Student added")

def view_students():
    cur.execute("SELECT id, name, class, marks FROM students")
    for s in cur.fetchall():
        print(s)

def update_marks():
    sid = int(input("Student ID: "))
    marks = int(input("New marks: "))
    cur.execute("UPDATE students SET marks=%s WHERE id=%s", (marks, sid))
    conn.commit()
    print("Marks updated")

def delete_student():
    sid = int(input("Student ID: "))
    cur.execute("DELETE FROM students WHERE id=%s", (sid,))
    conn.commit()
    print("Student deleted")

# ---------- TEACHER FUNCTIONS ----------
def add_teacher():
    name = input("Teacher name: ")
    subject = input("Subject: ")
    cur.execute(
        "INSERT INTO teachers (name, subject) VALUES (%s, %s)",
        (name, subject)
    )
    conn.commit()
    print("Teacher added")

def view_teachers():
    cur.execute("SELECT * FROM teachers")
    for t in cur.fetchall():
        print(t)

# ---------- STUDENT LOGIN ----------
def student_login():
    uname = input("Username: ")
    pwd = input("Password: ")

    cur.execute(
        "SELECT id, name, class, marks FROM students WHERE username=%s AND password=%s",
        (uname, pwd)
    )
    s = cur.fetchone()

    if s:
        print("\n--- STUDENT PROFILE ---")
        print("ID:", s[0])
        print("Name:", s[1])
        print("Class:", s[2])
        print("Marks:", s[3])
    else:
        print("Invalid login")

# ---------- MENUS ----------
def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Add Teacher")
        print("6. View Teachers")
        print("7. Back")

        ch = input("Choice: ")

        if ch == "1":
            add_student()
        elif ch == "2":
            view_students()
        elif ch == "3":
            update_marks()
        elif ch == "4":
            delete_student()
        elif ch == "5":
            add_teacher()
        elif ch == "6":
            view_teachers()
        elif ch == "7":
            break

# ---------- MAIN ----------
while True:
    print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
    print("1. Admin Login")
    print("2. Student Login")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        admin_menu()      # Admin adds students first
    elif choice == "2":
        student_login()   # Works only after students exist
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

