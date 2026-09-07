from data.tasks import tasks

def aux(task_id):
   if tasks:
      for task in tasks:
         current_task_id = task["id"]
         
         if task_id == current_task_id:
            task["completed"] = True
            
            print(f"\nTask '{task["task_title"]}' completed")
         else:
            print("\nTask not found")
   else:
      print("\nThere's no tasks created")

def complete_task():
   print("\n=== Complete Task ===")
      
   print("\nEnter task id: ")
   task_id = input("> ")
   
   aux(int(task_id))