class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employee_table(employee_list, choice):
    if choice == 1:
        sorted_list = sorted(employee_list, key=lambda emp: emp.age)
    elif choice == 2:
        sorted_list = sorted(employee_list, key=lambda emp: emp.name)
    elif choice == 3:
        sorted_list = sorted(employee_list, key=lambda emp: emp.salary)
    else:
        print("Invalid choice!")
        return sorted_list

    return sorted_list

def main():
    employees = [
        Employee("Employee ID", "Name", "Age", "Salary (PM)"),
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table:")
    for employee in employees:
        print(employee)

    print("\nSort Employee Table by:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice (1/2/3): "))

    sorted_employees = sort_employee_table(employees[1:], choice)

    print("\nSorted Employee Table:")
    print(employees[0])  
    for employee in sorted_employees:
        print(employee)

if __name__ == "__main__":
    main()
