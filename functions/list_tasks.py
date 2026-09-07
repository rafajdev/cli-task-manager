from data.tasks import tasks

def list_tasks():
   if tasks:
      print(tasks)
   else:
      print("There's no tasks created")