TASKS = [
    {"name": "Server Connectivity Check", "priority": "High", "is_completed": False},
    {"name": "Database Backup", "priority": "High", "is_completed": True},
    {"name": "CPU Usage Monitor", "priority": "Medium", "is_completed": False},
    {"name": "Clear Temp Files", "priority": "Low", "is_completed": True},
    {"name": "Security Patch Update", "priority": "High", "is_completed": False}
]



def get_completed_tasks(task_list):
    return [task for task in task_list if task["is_completed"]] 


def get_incomplete_tasks(task_list):
    return [task for task in task_list if not task["is_completed"]] 



def get_urgent_tasks(task_list):
    return [task for task in task_list if task["priority"] == "High"]



def format_status(is_completed):
    return "completed" if is_completed else "not completed"



def display_task_list(task_list):
    for task in task_list:
        status_text = format_status(task["is_completed"])
        print(f"Task: {task['name']} | Priority: {task['priority']} | Status: {status_text}") 


def display_summary(task_list):
    total = len(task_list) 
    open_count = len(get_incomplete_tasks(task_list)) 
    done_count = len(get_completed_tasks(task_list)) 
    urgent_count = len(get_urgent_tasks(task_list)) 

    print("\n" + "="*20)
    print("DAILY SUMMARY")
    print(f"Total Tasks: {total}")
    print(f"Open: {open_count}")
    print(f"Completed: {done_count}")
    print(f"Urgent: {urgent_count}")
    print("="*20)


def show_menu():
    print("--- Task Management System ---")
    print("1. Show all tasks")
    print("2. Show completed tasks")
    print("3. Show incomplete tasks")
    print("4. Show urgent tasks")
    print("5. Show daily summary")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Please enter your choice (1-6): ")

        if choice == "1":
            display_task_list(TASKS)
        elif choice == "2":
            display_task_list(get_completed_tasks(TASKS))
        elif choice == "3":
            display_task_list(get_incomplete_tasks(TASKS))
        elif choice == "4":
            display_task_list(get_urgent_tasks(TASKS))
        elif choice == "5":
            display_summary(TASKS)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
