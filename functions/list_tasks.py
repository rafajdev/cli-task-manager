from data.tasks import tasks
from functions.clear_terminal import clear_terminal

def list_tasks():
   clear_terminal()
   
   if tasks:
      print("\nTasks:")
      
      all_tasks_text = ""
      
      for task in tasks:
         task_text = f"(Id: {task["id"]} | Title: {task["task_title"]} | Completed: {"Yes" if task["completed"] == True else "No"})\n"
         
         all_tasks_text += task_text
      
      print(all_tasks_text)
   else:
      print("\nThere's no tasks created")