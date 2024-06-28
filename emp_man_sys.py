import os
class Employee:
    # class level list 
    employees = [] 
    # counter
    id_counter = 1  

    def __init__(self, name, salary):
        self.id = Employee.id_counter
        self.name = name
        self.salary = salary
        Employee.id_counter += 1

    @classmethod
    def add_employee(cls, name, salary):
        """This function is used for creating employee instance and takes 
        name and salary as arguments"""
        new_employee = cls(name, salary)
        cls.employees.append(new_employee)
        return new_employee

    @staticmethod
    def average_salary():
        """This function is used to calculate average salary of employees"""
        if not Employee.employees:
            return 0
        total_salary = sum(emp.salary for emp in Employee.employees)
        return total_salary / len(Employee.employees)

    def display_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: ${self.salary}")

emp1 = Employee.add_employee("John Doe", 50000)
emp2 = Employee.add_employee("Jane Smith", 60000)
emp3 = Employee.add_employee("Alice Johnson", 55000)
emp4 = Employee.add_employee("Taylor Swift", 100000)

should_continue = True

while should_continue:
    continue_executing = input("Which action would you like to perform?\n1. Add Employee\n2. Show Average Salary\n3. Display All Employee Details\n4. Exit\nType (1/2/3/4): ")
    if continue_executing == "1":
        # Adding new employees
        emp_name = input("Enter Employee's name: ")
        emp_salary = int(input("Enter Employee's salary: "))
        print("Employee info added.")
        emp4 = Employee.add_employee(emp_name, emp_salary)
    elif continue_executing == "2":
        # Calculating and printing the average salary
        avg_salary = Employee.average_salary()
        print(f"Average Salary: ${avg_salary:.2f}")
    elif continue_executing == "3":
        # Displaying details of all employees
        for emp in Employee.employees:
            emp.display_details()
    elif continue_executing == "4":
        # User Quits
        should_continue = False
        os.system('cls')
    else: 
        print("!!!!!!!!!Invalid input! Please enter valid input.!!!!!!!!!")