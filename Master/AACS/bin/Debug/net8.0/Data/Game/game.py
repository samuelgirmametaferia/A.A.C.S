
def start_game():
  print("Welcome to the Adventure!")
  print("You find yourself in a dark forest.")
  print("What do you do?")
  print("1. Go north")
  print("2. Go south")
  choice = input("> ")

  if choice == "1":
    north_path()
  elif choice == "2":
    south_path()
  else:
    print("Invalid choice. Please try again.")
    start_game()

def north_path():
  print("You walk north and encounter a fork in the path.")
  print("1. Take the left path")
  print("2. Take the right path")
  choice = input("> ")

  if choice == "1":
    left_path()
  elif choice == "2":
    right_path()
  else:
    print("Invalid choice. Please try again.")
    north_path()

def south_path():
  print("You walk south and come across a small stream.")
  print("1. Try to cross the stream")
  print("2. Look for another way around")
  choice = input("> ")

  if choice == "1":
    print("You attempt to cross the stream but slip and fall in!")
    print("Game Over")
  elif choice == "2":
    print("You carefully find a way around the stream.")
    print("You continue south and...")
    # Add more story elements here
  else:
    print("Invalid choice. Please try again.")
    south_path()

def left_path():
  print("You take the left path and...")
  # Add more story elements here

def right_path():
  print("You take the right path and...")
  # Add more story elements here

start_game()
```
