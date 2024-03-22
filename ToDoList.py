class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid index")
    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task Update successfully")
        else:
            print("Invalid index, Please Try again!")
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task Delete Successfully")
        else:
            print("Invalid Index, Please Try Again!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = " [X] " if task["completed"] else " [ ] "
                print(f"{i + 1}.{status}{task['task']}")
def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display my To Do List")
        print("4. Delete task")
        print("5. Update task")
        print("6. Quit/Exit")
        choice = input("Enter the number of option you want to execute: ")
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            index = int(input("Enter index you want to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "5":
            task = input("Enter new task: ")
            todo_list.add_task(task)
        elif choice == "6":
            print("Exiting Program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()
