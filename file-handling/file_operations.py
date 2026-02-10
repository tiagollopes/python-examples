# New commands: open(), with, write(), read()
# This example shows how to create, write, and read text files

file_name = "my_data.txt"

# 1. Writing to a file (using 'w' for write)
# The 'with' statement automatically closes the file for us
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python is great for file handling!\n")
    file.write("This line was written automatically.\n")
    print(f"File '{file_name}' created and written successfully.")

# 2. Reading from the file (using 'r' for read)
print("\nReading the content of the file:")
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 3. Appending data (using 'a' for append)
with open(file_name, "a", encoding="utf-8") as file:
    file.write("Adding a new line without deleting the old ones.\n")

print("New line appended.")
