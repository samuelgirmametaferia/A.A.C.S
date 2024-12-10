from random import choice

def start_story():
  print("You wake up in a dark forest. You can hear the rustling of leaves and the distant call of a bird. ")
  choice = input("Do you go left or right? ")
  if choice.lower() == "left":
    left_path()
  elif choice.lower() == "right":
    right_path()
  else:
    print("Invalid choice. Please enter 'left' or 'right'.")
    start_story()

def left_path():
  print("You follow the path to the left, and soon come across a small stream. ")
  choice = input("Do you cross the stream or continue along the path? ")
  if choice.lower() == "cross":
    cross_stream()
  elif choice.lower() == "continue":
    continue_path()
  else:
    print("Invalid choice. Please enter 'cross' or 'continue'.")
    left_path()

def right_path():
  print("You follow the path to the right, and come to a clearing. ")
  choice = input("Do you explore the clearing or continue along the path? ")
  if choice.lower() == "explore":
    explore_clearing()
  elif choice.lower() == "continue":
    continue_path()
  else:
    print("Invalid choice. Please enter 'explore' or 'continue'.")
    right_path()

def cross_stream():
  print("You carefully cross the stream and find a small cottage on the other side. ")
  choice = input("Do you knock on the door or continue exploring? ")
  if choice.lower() == "knock":
    knock_on_door()
  elif choice.lower() == "continue":
    continue_exploring()
  else:
    print("Invalid choice. Please enter 'knock' or 'continue'.")
    cross_stream()

def continue_path():
  print("You continue along the path, and eventually come to a fork in the road. ")
  choice = input("Do you take the upper path or the lower path? ")
  if choice.lower() == "upper":
    upper_path()
  elif choice.lower() == "lower":
    lower_path()
  else:
    print("Invalid choice. Please enter 'upper' or 'lower'.")
    continue_path()

# ... (Add more functions for different paths and choices)

start_story()