class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.is_completed = False

    # Getters
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.is_completed

    # Setters
    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def mark_completed(self):
        self.is_completed = True
        

class TaskView:
    def display_tasks(self, tasks):
        if not tasks:
            print("No tasks available.")
            return
        
        print("Tasks:")
        for task in tasks:
            status = "✓" if task.is_completed else "✗"
            print(f"[{status}] {task.get_id()}: {task.get_title()} - {task.get_description()}")

    def prompt_for_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        return title, description

    def prompt_for_task_completion(self):
        task_id = int(input("Enter the task ID to mark as completed: "))
        return task_id
    
    
class TaskController:
    def __init__(self):
        self.tasks = []
        self.next_id = 1  # Start IDs from 1

    def add_task(self, title, description):
        new_task = Task(self.next_id, title, description)
        self.tasks.append(new_task)
        self.next_id += 1

    def get_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.get_id() == task_id:
                task.mark_completed()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")
        
        
class Main:
    def __init__(self):
        self.controller = TaskController()
        self.view = TaskView()

    def run(self):
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                title, description = self.view.prompt_for_task()
                self.controller.add_task(title, description)
            elif choice == '2':
                tasks = self.controller.get_tasks()
                self.view.display_tasks(tasks)
            elif choice == '3':
                task_id = self.view.prompt_for_task_completion()
                self.controller.mark_task_completed(task_id)
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = Main()
    app.run()