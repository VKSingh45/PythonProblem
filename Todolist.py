class TodoList:
    def __init__():
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
    def show_tasks(self):
        print("Todo List:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}.{task}")
    def clear_tasks(self):
        self.tasks = []

todo_list = TodoList()
todo_list.add_task("Task 1")
todo_list.add_task("Task 2")
todo_list.show_tasks()
todo_list.remove_task("Task 2")
