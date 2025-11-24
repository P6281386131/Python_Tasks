
students = {} # Dictionary to hold student data
unique_courses = set() # Set to hold unique courses

while True:
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Show All Students")
    print("5. Show All Unique Courses (Set Methods)")
    print("6. Dictionary Methods Demo")
    print("7. Exit")

    choice = input("Enter choice: ")

    # ------------------------------
    # 1. ADD STUDENT
    # ------------------------------
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        courses = input("Enter Courses (comma separated): ").split(",")

        courses = [c.strip() for c in courses]

        students[roll] = {
            "name": name,
            "age": age,
            "courses": courses
        }

        # Adding courses to set (update)
        unique_courses.update(courses)

        print("Student Added")

    # ------------------------------
    # 2. REMOVE STUDENT
    # ------------------------------
    elif choice == "2":
        roll = input("Enter roll number to remove: ")

        if roll in students:
            students.pop(roll)
            print("Student Removed")
        else:
            print("Student Not Found")

    # ------------------------------
    # 3. SEARCH STUDENT
    # ------------------------------
    elif choice == "3":
        roll = input("Enter roll number: ")

        # using dictionary get()
        student = students.get(roll)
        if student:
            print("Student Found:", student)
        else:
            print("Not Found")

    # ------------------------------
    # 4. SHOW ALL STUDENTS
    # ------------------------------
    elif choice == "4":
        if not students:
            print("No students available.")
        else:
            for r, details in students.items():
                print(r, "→", details)

    # ------------------------------
    # 5. SHOW SET METHODS
    # ------------------------------
    elif choice == "5":
        print("\nCurrent Courses:", unique_courses)

        set= {"Python", "Java", "C" , "JavaScript" , "HTML"}

        print("\n--- SET METHODS DEMO ---")
        print("Union:", unique_courses.union(set))
        print("Intersection:", unique_courses.intersection(set))
        print("Difference:", unique_courses.difference(set))
        print("Symmetric Difference:", unique_courses.symmetric_difference(set))
        print("Is Disjoint?", unique_courses.isdisjoint({"Ruby"}))
        print("Is Subset?", set.issubset(unique_courses))
        print("Is Superset?", unique_courses.issuperset(set))

        # Demonstrate add(), discard(), remove(), pop()
        print("\n--- MODIFYING SET ---")
        unique_courses.add("NewCourse")    # add
        print("After add():", unique_courses)

        unique_courses.discard("Java")     # discard (no error)
        print("After discard():", unique_courses)

        # remove() gives error if item not found
        if "C" in unique_courses:
            unique_courses.remove("C")
            print("After remove():", unique_courses)

        popped = unique_courses.pop()      # removes random element
        print("pop() removed:", popped)
        print("After pop():", unique_courses)

    # ------------------------------
    # 6. DICTIONARY METHODS DEMO
    # ------------------------------
    elif choice == "6":
        print("\n--- DICTIONARY METHODS DEMO ---")

        print("Keys:", students.keys())         # keys()
        print("Values:", students.values())     # values()
        print("Copy of dictionary:", students.copy())  # copy()

        # clear() example (not actually clearing main dictionary)
        temp = students.copy()
        temp.clear()
        print("Temporary cleared dict:", temp)

    # ------------------------------
    # 7. EXIT
    # ------------------------------
    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
