import os

file_name = "tasks.txt"
with open(file_name,"w",encoding="utf-8")as file:
    file.write("1|PENDING|Learn Python Files\n")
    file.write("2|DONE|Write Exercies\n")
    file.write("3|PENDING|Finish The Project\n")




def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    task = []
    with open(filename,"r",encoding="utf-8")as file:
        for i in file:
            dic = {}
            line = i.strip().split("|")
            task.append({"id":line[0],
                         "status":line[1],
                         "description":line[2]
                         })
        
    return task
    

def save_tasks(filename, tasks):
    with open(filename,"w",encoding="utf-8")as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['status']}|{task['description']}\n")



    
def add_task(filename, description):
    task = load_tasks(filename)
    total = len(task) + 1
    new_task = {"id":str(total),"status":"PENDING","description":description}
    task.append(new_task)
    save_tasks(filename,task)






def complete_task(filename, task_id):
    tasks = load_tasks(filename)
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "DONE"
            found = True
            break
    if found:
        save_tasks(filename,tasks)
    else:
        return "the id does not exists"
    
    



def list_tasks(filename):
    tasks = load_tasks(filename)
    for i in tasks:
        status_icon = "[✓]" if i["status"] == "DONE" else "[ ]"
        print(f"{i['id']}. {status_icon} {i['description']}")   
        


def main():
    FILENAME = "tasks.txt"
    while True:
        print('\n=== To-Do List Manager ===')
        print("1. Show tasks ")
        print("2. Add task")
        print("3. Mark as completed")
        print("4. Exit")
        choice = input("choice option:")
        if choice == '1':
            print()
            list_tasks(FILENAME)
        elif choice == '2':
            desc = input("Please enter the description: ")
            add_task(FILENAME, desc)
            print("The task added")
        elif choice == '3':
            task_id = input("Please enter the number of the task:")
            complete_task(FILENAME, task_id)
            print("The task complete")
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Wrong chice! try again")



if __name__ == '__main__':
    main()


