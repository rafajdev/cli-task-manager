from functions.add_task import add_task
from functions.list_tasks import list_tasks
from functions.complete_task import complete_task
from functions.delete_task import delete_task
from functions.clear_terminal import clear_terminal
from version import __version__

def start():
   while True:
      print(f"\n=== Task Manager {__version__} ===")
      print("\n1. Add task")
      print("2. List tasks")
      print("3. Complete task")
      print("4. Delete task")
      print("5. Exit")
      
      try:
         user_input = int(input("\n> "))
      
         match user_input:
            case 1:
               add_task()
            case 2:
               list_tasks()
            case 3:
               complete_task()
            case 4:
               delete_task()
            case 5:
               print("Exiting...")
               break
            case _:
               clear_terminal()
               print("\nInvalid option. Try again.")
      except ValueError:
         clear_terminal()
         print("\nInvalid option. Try again.")
      except KeyboardInterrupt:
         print("\nExiting...")
         break
         

if __name__ == "__main__":
   start()