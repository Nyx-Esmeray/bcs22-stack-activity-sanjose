#Create a task manager in python using stack with basic functionalities:
 #(classes, methods, lists, loops, input-handling in python )
 #- add tasks with a title and descriptiom
 #- mark tasks as completed
 #- display the list of tasks along with status
 #- exit option to exit the task manager
 #push in your gitHub account and paste the URL in our SB- lab

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        
class TaskManager:
    def __init__(self):
        self.Tasks = []

    def task(self, title, description):
        t = Task(title, description)
        self.Tasks.append(t)
        print(f"Task '{title}' added successfully")  

    def completed(self, title):
        for task in self.Tasks:
            if task.title == title:
                task.completed = True
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def delete(self, title):
        for task in self.Tasks:
            if task.title == title:
                self.Tasks.remove(task)
                print(f"Task '{title}' has been deleted.")
                return
        print(f"Task '{title}' not found.")

    def display_tasks(self):
        if not self.Tasks:
            print("No tasks to display.")
        else:
            print("Tasks: ")
            for task in self.Tasks:
                status = "Completed" if task.completed else "Not Completed"
                print(f" * Title: {task.title}, Description: {task.description}, Status: {status}")

    def display(self):
        while True:
            print("\n\t\t\t\t\tTask Manager")
            print(f"{'=' * 50}")
            print("1. Add Task")
            print("2. Mark Task as Completed")
            print("3. Delete Task")
            print("4. Display Tasks")
            print("E. Exit")
            option = input("Select an Option (1-4) or (E) to exit: ")

            if option == "1":
                title = input("\nEnter Task Title: ")
                des = input("Enter Task Description: ")
                self.task(title, des)

            elif option == "2":
                com = input("\nEnter task title to mark as completed: ")
                self.completed(com)

            elif option == "3":
                dele = input("\nEnter task title to delete: ")
                d = input("Are you sure you want to delete the task? (Yes or No): ")
                if d == "Yes":
                    self.delete(dele)
                    print("Task Deleted")
                elif d == "No":
                    continue
                else:
                    print("Invalid Option. Please enter 'Yes' or 'No'")

            elif option == "4":
                self.display_tasks()

            elif option == "E":
                exit = input("\nAre you sure you want to exit? (Yes or No): ")
                if exit == "Yes":
                    print("Exiting Task Manager...")
                    break
                elif exit == "No":
                    continue
                else:
                    print("Invalid Option. Please enter 'Yes' or 'No'")
            else:
                print("Invalid Option!")
                print("Please select a valid option (1-4) or (E) to exit")

manager = TaskManager()
manager.display()

