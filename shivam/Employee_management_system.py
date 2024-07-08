import random

class Employee:
    """This class represents an employee with attributes like ID,name etc
    """
    def __init__(self, emp_id, name, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")
    """
        Initializes an Employee object with the given attributes.
        """

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def display_all_employees(self):
        for emp in self.employees:
            emp.display_info()
            print("*"*50)

    def calculate_average_salary(self):
        return sum(emp.salary for emp in self.employees) / len(self.employees)

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            for emp in self.employees:
                f.write(f"{emp.emp_id},{emp.name},{emp.designation},{emp.salary}\n")

    def read_from_file(self, filename):
        self.employees = []
        with open(filename, "r") as f:
            for line in f:
                emp_id, name, designation, salary = line.strip().split(",")
                emp = Employee(int(emp_id), name, designation, int(salary))
                self.employees.append(emp)

ems = EmployeeManagementSystem()
ems.read_from_file("employee1.txt")
#Main program loop
while True:
    print("*"*50)
    print("1. Add New Employee")
    print("2. Display All Employees")
    print("3. Calculate Average Salary")
    print("4. Update Employee Info")
    print("5. Exit")
    print("*"*50)

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        emp_id = random.randint(1111, 9999)
        name = input("Enter Employee Name: ")
        designation = input("Enter Employee Designation: ")
        salary = int(input("Enter Employee Salary: "))
        emp = Employee(emp_id, name, designation, salary)
        ems.add_employee(emp)
        print("Employee added successfully!")

    elif choice == 2:
        ems.display_all_employees()

    elif choice == 3:
        print(f"Average Salary: {ems.calculate_average_salary()}")

    elif choice == 4:
        emp_id = int(input("Enter Employee ID: "))
        for emp in ems.employees:
            if emp.emp_id == emp_id:
                update_choice = int(input("Enter 1 to update salary or 2 to update designation: "))
                if update_choice == 1:
                    new_salary = int(input("Enter New Salary: "))
                    emp.salary = new_salary
                    print("Salary updated successfully!")
                elif update_choice == 2:
                    new_designation = input("Enter New Designation: ")
                    emp.designation = new_designation
                    print("Designation updated successfully!")
                else:
                    print("Invalid choice. Please try again.")
                break
        else:
            print("Employee not found.")

    elif choice == 5:
        ems.write_to_file("employee1.txt")
        print("Thank you for using the Employee Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
