from data.tasks import tasks
from functions.clear_terminal import clear_terminal

def list_tasks():
   clear_terminal()
   
   if tasks:
      print("Tasks:")
      print(tasks)
   else:
      print("\nThere's no tasks created")