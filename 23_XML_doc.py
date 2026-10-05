import xml.etree.ElementTree as ET
from pathlib import Path

XML_FILE = Path("students.xml")


def create_xml():
    """Create the XML file if it does not exist."""
    if not XML_FILE.exists():
        root = ET.Element("students")
        tree = ET.ElementTree(root)
        tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)
        print("XML file created.")


def save_xml(root):
    """Save the XML tree with indentation."""
    ET.indent(root, space="    ")
    tree = ET.ElementTree(root)
    tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)


def load_xml():
    """Load and return the XML root element."""
    create_xml()
    tree = ET.parse(XML_FILE)
    return tree.getroot()


def add_student(student_id, name, cgpa, department, email):
    root = load_xml()

    # Check whether ID already exists
    if root.find(f"./student[@id='{student_id}']") is not None:
        print("Student ID already exists.")
        return

    student = ET.SubElement(root, "student", id=str(student_id))

    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "cgpa").text = str(cgpa)
    ET.SubElement(student, "department").text = department
    ET.SubElement(student, "email").text = email

    save_xml(root)
    print("Student added successfully.")


def display_students():
    root = load_xml()

    students = root.findall("student")

    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 60)

    for student in students:
        print(f"ID     : {student.get('id')}")
        print(f"Name   : {student.findtext('name')}")
        print(f"Department : {student.findtext('department')}")
        print(f"Cgpa    : {student.findtext('cgpa')}")
        print(f"Email  : {student.findtext('email')}")
        print("-" * 60)


def search_student(student_id):
    root = load_xml()

    student = root.find(f"./student[@id='{student_id}']")

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Found")
    print(f"ID     : {student.get('id')}")
    print(f"Name   : {student.findtext('name')}")
    print(f"cgpa    : {student.findtext('cgpa')}")
    print(f"department : {student.findtext('department')}")
    print(f"Email  : {student.findtext('email')}")


def update_student(student_id):
    root = load_xml()

    student = root.find(f"./student[@id='{student_id}']")

    if student is None:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{student.findtext('name')}]: ")
    department = input(f"Department [{student.findtext('department')}]: ")
    cgpa = input(f"CGPA [{student.findtext('cgpa')}]: ")
    email = input(f"Email [{student.findtext('email')}]: ")

    if name:
        student.find("name").text = name

    if cgpa:
        student.find("cgpa").text = cgpa

    if department:
        student.find("department").text = department

    if email:
        student.find("email").text = email

    save_xml(root)
    print("Student information updated successfully.")


def delete_student(student_id):
    root = load_xml()

    student = root.find(f"./student[@id='{student_id}']")

    if student is None:
        print("Student not found.")
        return

    root.remove(student)
    save_xml(root)

    print("Student deleted successfully.")


def main():
    create_xml()

    while True:
        print("\n===== Student Information Mancgpament =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            cgpa = input("Enter cgpa: ")
            department = input("Enter department: ")
            email = input("Enter email: ")

            add_student(student_id, name, cgpa, department, email)

        elif choice == "2":
            display_students()

        elif choice == "3":
            student_id = input("Enter student ID to search: ")
            search_student(student_id)

        elif choice == "4":
            student_id = input("Enter student ID to update: ")
            update_student(student_id)

        elif choice == "5":
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)

        elif choice == "6":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
