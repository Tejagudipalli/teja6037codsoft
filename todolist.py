tasks = []
def show_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"{index+1}. {task}")
def add_task():
  new_task = input("Enter a new task: ")
  tasks.append(new_task)
  print("Task added successfully!")
def mark_complete():
  if not tasks:
    print("There are no tasks to mark complete.")
    return
  
  show_tasks()
  try:
    task_number = int(input("Enter the number of the task to mark complete: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
      print("Invalid task number.")
      return
    tasks.pop(task_number)
    print("Task marked complete!")
  except ValueError:
    print("Invalid input. Please enter a number.")
while True:
  print("\nTo-Do List App")
  print("1. Show Tasks")
  print("2. Add Task")
  print("3. Mark Task Complete")
  print("4. Exit")
  
  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    show_tasks()
  elif choice == '2':
    add_task()
  elif choice == '3':
    mark_complete()
  elif choice == '4':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")


