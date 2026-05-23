from soldier_manager import add_soldier,remove_soldier,get_all_soldiers
from duty_manager import add_duty_to_soldier,update_duty_status,get_soldier_duties



def show_menu():
    print("=" * 10 + " Soldier Duty Management System " + "=" * 10)
    print("1: Exit")
    print("2: Add new soldier")
    print("3: Remove soldier")
    print("4: Show list of all soldiers")
    print("5: Add duty to a soldier")
    print("6: Update duty status")
    print("7: Show duties of a soldier")
    print("=" * 52)




def handle_add_soldier():
    try:
        raw_id = input("Enter soldier ID (7 digits): ")
        if not raw_id.isdigit():
            raise ValueError("ID must contain digits only.")
            
        soldier_id = int(raw_id)
        name = input("Enter soldier name: ")
        
        add_soldier(soldier_id, name)
        print("Soldier added successfully!")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")



def handle_remove_soldier():
    try:
        raw_id = input("Enter soldier ID to remove: ")
        if not raw_id.isdigit():
            raise ValueError("ID must contain digits only.")
            
        soldier_id = int(raw_id)
        remove_soldier(soldier_id)
        print("Soldier removed successfully!")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")




def handle_show_list_of_soldiers():
    soldiers = get_all_soldiers()
    if not soldiers:
        print("The system is currently empty of soldiers.")
        return
        
    print("\n--- Soldiers List ---")
    for s in soldiers:
        print(f"ID: {s['id']} | Name: {s['name']} | Duties Count: {len(s['duties'])}")




def handle_add_duty():
    try:
        raw_id = input("Enter soldier ID for duty assignment: ")
        if not raw_id.isdigit():
            raise ValueError("ID must contain digits only.")
            
        soldier_id = int(raw_id)
        duty_name = input("Enter duty name: ")
        day = input("Enter day of the week: ")
        
        add_duty_to_soldier(soldier_id, duty_name, day)
        print("Duty assigned successfully!")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")




def handle_update_duty_status():
    try:
        raw_id = input("Enter soldier ID: ")
        if not raw_id.isdigit():
            raise ValueError("ID must contain digits only.")
            
        soldier_id = int(raw_id)
        duty_name = input("Enter duty name to update: ")
        new_status = input("Enter new status (pending/completed/missed): ")
        
        update_duty_status(soldier_id, duty_name, new_status)
        print("Success: Duty status updated successfully!")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")



def handle_show_soldier_duties():
    try:
        raw_id = input("Enter soldier ID to view duties: ")
        if not raw_id.isdigit():
            raise ValueError("ID must contain digits only.")
            
        soldier_id = int(raw_id)
        duties = get_soldier_duties(soldier_id)
        
        if not duties:
            print("This soldier has no duties assigned.")
            return
            
        print(f"\n--- Duties for Soldier ID {soldier_id} ---")
        for d in duties:
            print(f"Duty: {d['name']} | Day: {d['day']} | Status: {d['status']}")
            
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")



def main():
    while True:
        show_menu()
        user_choice = input("Please choose an option (1-7): ").strip()
        
        if user_choice == "1":
            print("Exiting the system. Goodbye!")
            break
        elif user_choice == "2":
            handle_add_soldier()
        elif user_choice == "3":
            handle_remove_soldier()
        elif user_choice == "4":
            handle_show_list_of_soldiers()
        elif user_choice == "5":
            handle_add_duty()
        elif user_choice == "6":
            handle_update_duty_status()
        elif user_choice == "7":
            handle_show_soldier_duties()
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")



if __name__ == "__main__":
    main()