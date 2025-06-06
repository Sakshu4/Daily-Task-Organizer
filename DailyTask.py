
tasks = [
    ("Finish Python project", "Work", "High"),
    ("Buy groceries", "Personal", "Medium"),
    ("Read book", "Personal", "Low")
]

def add_task():
    print("\nAdd New Task")
    task_name = input("Task name: ")
    category = input("Category (Work, Personal, etc.): ")
    priority = input("Priority (High, Medium, Low): ").capitalize()
    
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority! Please enter High, Medium, or Low.\n")
        return
    tasks.append((task_name, category, priority))
    print("Task added!\n")

def view_tasks():
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks yet!\n")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task[0]} | Category: {task[1]} | Priority: {task[2]}")
    print()

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed[0]}\n")
        else:
            print("Wrong number!\n")
    except ValueError:
        print("Please enter a number!\n")

def show_high_priority():
    print("\nHigh Priority Tasks:")
    high_tasks = [t for t in tasks if t[2] == "High"]
    if not high_tasks:
        print("No high priority tasks found.\n")
        return
    for i, task in enumerate(high_tasks, start=1):
        print(f"{i}. {task[0]} | Category: {task[1]} | Priority: {task[2]}")
    print()

def count_tasks_by_category():
    print("\nCount Tasks by Category:")
    if not tasks:
        print("No tasks to count.\n")
        return
    count = {}
    for task in tasks:
        category = task[1]
        count[category] = count.get(category, 0) + 1
    for category, number in count.items():
        print(f"{category}: {number}")
    print()

def menu():
    while True:
        print("=== Daily Task Organizer ===")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Show High Priority Tasks")
        print("5. Count Tasks by Category")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            show_high_priority()
        elif choice == "5":
            count_tasks_by_category()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()
