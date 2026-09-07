from data.tasks import tasks
from functions.clear_terminal import clear_terminal

def generate_task_id():
   if tasks:
      all_ids = []
      
      for task in tasks:
         current_task_id = task["id"]
         all_ids.append(current_task_id)
         
      return max(all_ids) + 1
   else:
      return 1
   
def add_task():
   clear_terminal()
   print("\n=== Add Task ===")
   
   print("\nEnter task title: ")
   task_title = input("> ")

   task_id = generate_task_id()
   
   tasks.append({
      "id": task_id,
      "task_title": task_title,
      "completed": False
   })
   
   clear_terminal()
   print(f"Task '{task_title}' created")