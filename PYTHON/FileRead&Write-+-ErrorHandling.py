File Read & Write + Error Handling

def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the file for reading
        with open(filename, 'r') as file:
            content = file.read()

        # Example modification: convert text to uppercase
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Success! Modified content has been saved in '{new_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    read_and_modify_file()
