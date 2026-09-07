from data.tasks import tasks

def aux(task_id):
   if tasks:
      for task in tasks:
         current_task_id = task["id"]
         
         if task_id == current_task_id:
            tasks.remove(task)
            
            print(f"\nTask '{task["task_title"]}' deleted")
            return
         
      print("\nTask not found")
   else:
      print("\nThere's no tasks created")

def delete_task():
   print("\n=== Delete Task ===")
      
   print("\nEnter task id: ")
   task_id = input("> ")
   
   aux(int(task_id))