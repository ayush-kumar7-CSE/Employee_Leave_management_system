from datetime import datetime

# Employee leave balances
employees = {
    "E101": {
        "Casual": 12,
        "Sick": 10,
        "Earned": 15
    }
}


def apply_leave(employee_id, leave_type, from_date, to_date):
    if employee_id not in employees:
        print("Invalid employee ID.")
        return

    if leave_type not in employees[employee_id]:
        print("Invalid leave type.")
        return

    try:
        start = datetime.strptime(from_date, "%Y-%m-%d")
        end = datetime.strptime(to_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    if end < start:
        print("Invalid dates. To-date cannot be before from-date.")
        return

    days = (end - start).days + 1
    balance = employees[employee_id][leave_type]

    if days <= balance:
        employees[employee_id][leave_type] = balance - days

        print(
            f"Leave approved: {days} days {leave_type} | "
            f"Balance {leave_type}: "
            f"{employees[employee_id][leave_type]}"
        )
    else:
        print(
            f"Leave rejected. Requested: {days} days "
            f"| Available: {balance}"
        )


def view_balance(employee_id):
    if employee_id not in employees:
        print("Invalid employee ID.")
        return

    print(f"Balance: {employee_id}")

    for leave_type, balance in employees[employee_id].items():
        print(f"{leave_type}: {balance}")


def main():
    while True:
        print("\n1. Apply for leave")
        print("2. View balance")
        print("3. Exit")

        choice = input("Enter menu option: ")

        if choice == "1":
            employee_id = input("Employee ID: ")
            leave_type = input("Leave type (Casual/Sick/Earned): ")
            from_date = input("From date (YYYY-MM-DD): ")
            to_date = input("To date (YYYY-MM-DD): ")

            apply_leave(
                employee_id,
                leave_type,
                from_date,
                to_date
            )

        elif choice == "2":
            employee_id = input("Employee ID: ")
            view_balance(employee_id)

        elif choice == "3":
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()