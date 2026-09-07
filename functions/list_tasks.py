from data.tasks import tasks

def list_tasks():
   if tasks:
      print(tasks)
   else:
      print("\nThere's no tasks created")