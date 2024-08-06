import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileRecovery:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

    def recover(self):
        if not os.path.isfile(self.source_path):
            raise FileNotFoundError(f"File {self.source_path} does not exist.")
        shutil.copy(self.source_path, self.destination_path)

class FolderRecovery:
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def recover(self):
        if not os.path.isdir(self.source_folder):
            raise NotADirectoryError(f"Directory {self.source_folder} does not exist.")
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)
        self._copy_contents(self.source_folder, self.destination_folder)

    def _copy_contents(self, src, dst):
        for item in os.listdir(src):
            source_item = os.path.join(src, item)
            destination_item = os.path.join(dst, item)
            if os.path.isfile(source_item):
                shutil.copy(source_item, destination_item)
            elif os.path.isdir(source_item):
                os.makedirs(destination_item, exist_ok=True)
                self._copy_contents(source_item, destination_item)

class RecoveryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File and Folder Recovery")

        self.source_label = tk.Label(root, text="Source Path:")
        self.source_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.source_entry = tk.Entry(root, width=50)
        self.source_entry.grid(row=0, column=1, padx=10, pady=10)

        self.source_button = tk.Button(root, text="Browse", command=self.browse_source)
        self.source_button.grid(row=0, column=2, padx=10, pady=10)

        self.destination_label = tk.Label(root, text="Destination Path:")
        self.destination_label.grid(row=1, column=0, padx=10, pady=10)

        self.destination_entry = tk.Entry(root, width=50)
        self.destination_entry.grid(row=1, column=1, padx=10, pady=10)

        self.destination_button = tk.Button(root, text="Browse", command=self.browse_destination)
        self.destination_button.grid(row=1, column=2, padx=10, pady=10)

        self.recover_button = tk.Button(root, text="Recover", command=self.perform_recovery)
        self.recover_button.grid(row=2, column=1, padx=10, pady=20)

    def browse_source(self):
        filename = filedialog.askopenfilename()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, filename)

    def browse_destination(self):
        foldername = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, foldername)

    def perform_recovery(self):
        source = self.source_entry.get()
        destination = self.destination_entry.get()

        if os.path.isfile(source):
            recovery = FileRecovery(source, destination)
        elif os.path.isdir(source):
            recovery = FolderRecovery(source, destination)
        else:
            messagebox.showerror("Error", "Invalid source path.")
            return

        try:
            recovery.recover()
            messagebox.showinfo("Success", f"Recovery completed to {destination}")
        except (FileNotFoundError, NotADirectoryError) as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RecoveryApp(root)
    root.mainloop()
