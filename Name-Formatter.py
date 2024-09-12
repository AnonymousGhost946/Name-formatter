import tkinter as tk
from tkinter import messagebox
import os

def create_folders():
    # Retrieve user inputs
    dir_path = dir_path_entry.get()
    try:
        folder_length = int(folder_length_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the number of folders.")
        return
    foldernames = foldernames_entry.get()

    # Change directory
    if not os.path.isdir(dir_path):
        messagebox.showerror("Error", f"No directory or folder found at {dir_path}")
        return
    try:
        os.chdir(dir_path)
    except PermissionError:
        messagebox.showerror("Error", f"Permission denied to access {dir_path}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Sorry, unable to locate error: {e}")
        return

    # Create folders
    errors = []
    for folder_number in range(folder_length):
        folder_name = f"{folder_number}_{foldernames}"
        try:
            os.makedirs(folder_name, exist_ok=True)
        except FileExistsError:
            errors.append(f"Folder '{folder_name}' already exists.")
        except PermissionError:
            errors.append(f"Permission denied to create folder '{folder_name}'.")
        except Exception as e:
            errors.append(f"An error occurred while creating '{folder_name}': {e}")

    if errors:
        messagebox.showwarning("Warnings", "\n".join(errors))
    else:
        messagebox.showinfo("Success", "All folders created successfully.")

# Create the main window
root = tk.Tk()
root.title("Folder Creator")

# Create and place widgets
tk.Label(root, text="Directory Path:").grid(row=0, column=0, padx=10, pady=10)
dir_path_entry = tk.Entry(root, width=50)
dir_path_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Folders:").grid(row=1, column=0, padx=10, pady=10)
folder_length_entry = tk.Entry(root, width=50)
folder_length_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Folder Name Format:").grid(row=2, column=0, padx=10, pady=10)
foldernames_entry = tk.Entry(root, width=50)
foldernames_entry.grid(row=2, column=1, padx=10, pady=10)

create_button = tk.Button(root, text="Create Folders", command=create_folders)
create_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
