
print("Mishra Ji's Notepad")
def main():
  file_name = "notepad.txt"
  while True:
      print("\n1. Read\n2. Write\n3. Edit\n4. Save\n5. Exit")
      choice = input("Select an option: ")

      if choice == "1":
          read_notepad(file_name)
      elif choice == "2":
          write_notepad(file_name)
      elif choice == "3":
          edit_notepad(file_name)
      elif choice == "4":
          save_notepad(file_name)
      elif choice == "5":
          print("Exiting notepad...")
          break
      else:
          print("Invalid choice. Please try again.")

def read_notepad(file_name):
  try:
      with open(file_name, 'r') as file:
          content = file.read()
          print("\n--- Notepad Content ---\n")
          print(content)
  except FileNotFoundError:
      print("File not found. Please write something first.")

def write_notepad(file_name):
  content = input("Enter text to write: ")
  with open(file_name, 'w') as file:
      file.write(content)
  print("Text written successfully.")

def edit_notepad(file_name):
  content = input("Enter text to append: ")
  with open(file_name, 'a') as file:
      file.write("\n" + content)
  print("Text appended successfully.")

def save_notepad(file_name):
  print("Notepad saved as", file_name)

if __name__ == "__main__":
  main()




# 1. Read
# 2. Write
# 3. Edit
# 4. Save
# 5. Exit
# Select an option: 2
# Enter text to write: Aditya mishra ji
# Text written successfully.

# 1. Read
# 2. Write
# 3. Edit
# 4. Save
# 5. Exit
# Select an option: 1

# --- Notepad Content ---

# Aditya mishra ji

# 1. Read
# 2. Write
# 3. Edit
# 4. Save
# 5. Exit
# Select an option: 4
# Notepad saved as notepad.txt

# 1. Read
# 2. Write
# 3. Edit
# 4. Save
# 5. Exit
# Select an option: 
# Invalid choice. Please try again.

# 1. Read
# 2. Write
# 3. Edit
# 4. Save
# 5. Exit
# Select an option: 3
# Enter text to append: GOAT 
# Text appended successfully.

# 1. Read
# 2. Write
# 3. Edit
# 4. Save
# 5. Exit
# Select an option: 1

# --- Notepad Content ---

# Aditya mishra ji
# GOAT 

# 1. Read
# 2. Write
# 3. Edit
# 4. Save
# 5. Exit
# Select an option: 5
# Exiting notepad...

