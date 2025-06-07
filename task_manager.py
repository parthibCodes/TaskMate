class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        task['done'] = False
        self.tasks.append(task)
        print(f"✅ Task added: {task['title']}")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks yet.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "✅" if task.get("done") else "❌"
            print(f"{i}. {task['title']} (Priority: {task.get('priority', 'N/A')}, Due: {task.get('due_date', 'N/A')}) [{status}]")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
            print(f"🎉 Task '{self.tasks[index - 1]['title']}' marked as complete!")
        else:
            print("❌ Invalid task number.")
