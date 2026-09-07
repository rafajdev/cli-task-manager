from functions.add_task import add_task
from functions.list_tasks import list_tasks
from functions.complete_task import complete_task
from functions.delete_task import delete_task
from functions.clear_terminal import clear_terminal

def start():
   while True:
      print("\n=== Task Manager ===")
      print("\n1. Add task")
      print("2. List tasks")
      print("3. Complete task")
      print("4. Delete task")
      print("5. Exit")
      
      user_input = input("\n> ")
      
      match user_input:
         case "1":
            add_task()
         case "2":
            list_tasks()
         case "3":
            complete_task()
         case "4":
            delete_task()
         case "5":
            break
         case _:
            clear_terminal()
            print("\nInvalid option. Try again.")

if __name__ == "__main__":
   start()