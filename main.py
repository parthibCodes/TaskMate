from task_manager import TaskManager
from gpt_handler import GPTHandler

print("\n🤖 Welcome to GPT TaskMate! Your AI-powered task manager.")

manager = TaskManager()
gpt = GPTHandler()

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        desc = input("📝 Enter task description: ")

        # Manual inputs
        priority = input("⭐ Set priority (low / medium / high): ").strip().lower()
        due_date = input("📅 Set due date (YYYY-MM-DD or N/A): ").strip()

        # Let GPT only generate steps
        steps_only = gpt.parse_task(desc).get("steps", [])

        task = {
            "title": desc,
            "priority": priority if priority in ["low", "medium", "high"] else "medium",
            "due_date": due_date if due_date else "N/A",
            "steps": steps_only
        }

        manager.add_task(task)

    elif choice == '2':
        manager.view_tasks()
    elif choice == '3':
        manager.view_tasks()
        idx = int(input("Enter task number to mark complete: "))
        manager.complete_task(idx)
        print(gpt.get_motivation())
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
