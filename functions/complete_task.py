from data.tasks import tasks
from functions.clear_terminal import clear_terminal

def aux(task_id):
   if tasks:
      for task in tasks:
         current_task_id = task["id"]
         
         if task_id == current_task_id:
            task["completed"] = True
            
            clear_terminal()
            print(f"\nTask '{task["task_title"]}' completed")
            
            return
      
      clear_terminal()
      print("\nTask not found")
   else:
      clear_terminal()
      print("\nThere's no tasks created")

def complete_task():
   clear_terminal()
   print("\n=== Complete Task ===")
      
   print("\nEnter task id: ")
   task_id = input("> ")
   
   aux(int(task_id))