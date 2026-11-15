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
            f"Balance {leave_type}: {employees[employee_id][leave_type]}"
        )
    else:
        print(
            f"Leave rejected. Requested: {days} days "
            f"| Available: {balance} days"
        )


def view_balance(employee_id):
    if employee_id not in employees:
        print("Invalid employee ID.")
        return

    bal = employees[employee_id]
    print(f"Casual: {bal['Casual']} | Sick: {bal['Sick']} | Earned: {bal['Earned']}")


def main():
    while True:
        print("\n1. Apply for leave")
        print("2. View balance")
        print("3. Exit")

        choice = input("Enter menu option: ").strip()

        if choice == "1":
            employee_id = input("Employee ID: ").strip().upper()
            leave_type = input("Leave type (Casual/Sick/Earned): ").strip().capitalize()
            from_date = input("From date (YYYY-MM-DD): ").strip()
            to_date = input("To date (YYYY-MM-DD): ").strip()

            apply_leave(employee_id, leave_type, from_date, to_date)

        elif choice == "2":
            employee_id = input("Employee ID: ").strip().upper()
            view_balance(employee_id)

        elif choice == "3":
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()
