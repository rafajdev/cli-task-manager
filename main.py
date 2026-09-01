
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
            print("Add task")
         case "2":
            print("List tasks")
         case "3":
            print("Complete task")
         case "4":
            print("Delete task")
         case "5":
            break
         case _:
            print("\nInvalid option. Try again.")

start()