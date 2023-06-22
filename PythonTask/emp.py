def add_employee(database):
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")
    salary = input("Enter employee salary: ")

    # Validate input
    if not age.isdigit():
        print("Invalid input for age. Age should be a numeric value.")
        return
    if not salary.isdigit():
        print("Invalid input for salary. Salary should be a numeric value.")
        return

    # Add employee to the database
    database[name] = {
        'age': int(age),
        'position': position,
        'salary': int(salary)
    }
    print("Employee added successfully!")


def update_employee(database):
    name = input("Enter employee name: ")
    if name not in database:
        print("Employee not found!")
        return

    field = input("Enter field to update (age/position/salary): ")
    if field not in ['age', 'position', 'salary']:
        print("Invalid field!")
        return

    new_value = input("Enter new value: ")

    # Validate input
    if field == 'age' and not new_value.isdigit():
        print("Invalid input for age. Age should be a numeric value.")
        return
    if field == 'salary' and not new_value.isdigit():
        print("Invalid input for salary. Salary should be a numeric value.")
        return

    # Update employee information
    database[name][field] = new_value
    print("Employee information updated successfully!")


def delete_employee(database):
    name = input("Enter employee name: ")
    if name not in database:
        print("Employee not found!")
        return

    # Delete employee from the database
    del database[name]
    print("Employee deleted successfully!")


def view_employee_list(database):
    if not database:
        print("No employees found!")
        return

    print("+----------+-----+----------+---------+")
    print("|   Name   | Age | Position |  Salary |")
    print("+----------+-----+----------+---------+")
    for name, info in database.items():
        print("| {:<8} | {:<3} | {:<8} | {:<7} |".format(
            name, info['age'], info['position'], info['salary']))
    print("+----------+-----+----------+---------+")


def search_employee(database):
    query = input("Enter search query: ")
    results = {}
    for name, info in database.items():
        if query.lower() in name.lower() or query.lower() in info['position'].lower():
            results[name] = info

    if not results:
        print("No employees found!")
        return

    print("+----------+-----+----------+---------+")
    print("|   Name   | Age | Position |  Salary |")
    print("+----------+-----+----------+---------+")
    for name, info in results.items():
        print("| {:<8} | {:<3} | {:<8} | {:<7} |".format(
            name, info['age'], info['position'], info['salary']))
    print("+----------+-----+----------+---------+")


def sort_employee_list(database):
    sort_by = input("Sort by (name/age/position/salary): ")
    if sort_by not in ['name', 'age', 'position', 'salary']:
        print("Invalid sort option!")
        return

    sorted_employees = sorted(database.items(), key=lambda x: x[1][sort_by] if sort_by != 'name' else x[0])

    print("+----------+-----+----------+---------+")
    print("|   Name   | Age | Position |  Salary |")
    print("+----------+-----+----------+---------+")
    for name, info in sorted_employees:
        print("| {:<8} | {:<3} | {:<8} | {:<7} |".format(
            name, info['age'], info['position'], info['salary']))
    print("+----------+-----+----------+---------+")



def main():
    employee_database = {}

    while True:
        print("\nEmployee Database Management System\n")
        print("1. Add new employee")
        print("2. Update employee information")
        print("3. Delete employee")
        print("4. View employee list")
        print("5. Search employee")
        print("6. Sort employee list")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_employee(employee_database)
        elif choice == '2':
            update_employee(employee_database)
        elif choice == '3':
            delete_employee(employee_database)
        elif choice == '4':
            view_employee_list(employee_database)
        elif choice == '5':
            search_employee(employee_database)
        elif choice == '6':
            sort_employee_list(employee_database)
        elif choice == '7':
            break
        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
