import os

def list_all_files(directory, current_path=""):
  """
  This function lists all files and folders with structure indicators and avoids repetition.

  Args:
      directory: The path to the starting directory.
      current_path: The current path accumulated during recursion (defaults to "").

  Returns:
      None
  """
  for item in os.listdir(directory):
    full_path = os.path.join(directory, item)
    if os.path.isdir(full_path):
      print(f"{current_path}{item}  - ")
      list_all_files(full_path, f"{current_path}{item}   |   ")
    else:
      print(f"{current_path}{item}")

# Example usage
starting_dir = "./"
list_all_files(starting_dir)
