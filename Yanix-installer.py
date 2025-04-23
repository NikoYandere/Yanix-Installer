import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import os
import time

class InstallWizard:
    def __init__(self, root):
        self.root = root
        self.root.title("Yanix-Launcher Setup")
        self.root.geometry("665x546")
        
        self.step = 0

        self.root.configure(bg="white")

        self.content_frame = tk.Frame(self.root, bg="white", bd=5)
        self.content_frame.pack(padx=20, pady=20, expand=True, fill="both")

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.content_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=10, fill='x')

        self.status_label = tk.Label(self.content_frame, text="Welcome to the Yanix-Launcher installer.", wraplength=350, bg="white")
        self.status_label.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_step)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel_install)
        self.cancel_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.show_welcome()

    def show_welcome(self):
        self.status_label.config(text="Welcome to the Yanix-Launcher installer.\nClick 'Next' to continue.")
        self.next_button.config(state=tk.NORMAL)

    def next_step(self):
        if self.step == 0:
            self.prepare_install()
        elif self.step == 1:
            self.clone_repository()
        elif self.step == 2:
            self.complete_install()
        elif self.step == 3:
            self.finish_install()

    def prepare_install(self):
        self.step = 1
        self.update_progress(10)
        self.status_label.config(text="Checking Git installation...")
        self.next_button.config(state=tk.DISABLED)
        self.root.after(1000, self.check_git)

    def check_git(self):
        try:
            subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.update_progress(30)
            self.status_label.config(text="Git found. Starting repository cloning.")
            self.root.after(500, self.clone_repository)
        except subprocess.CalledProcessError:
            self.update_progress(0)
            messagebox.showerror("Error", "Git is not installed. Please install Git before continuing.")
            self.root.quit()

    def clone_repository(self):
        self.step = 2
        self.update_progress(50)
        self.status_label.config(text="Cloning the Yanix-Launcher repository...")
        self.next_button.config(state=tk.DISABLED)
        self.root.after(500, self.run_git_clone)

    def run_git_clone(self):
        repo_dir = os.path.expanduser("~") + "/yanix-launcher"
        try:
            subprocess.run(["git", "clone", "https://github.com/NikoYandere/yanix-launcher", repo_dir], check=True)
            self.update_progress(80)
            self.status_label.config(text="Cloning completed successfully.")
            self.root.after(500, self.complete_install)
        except subprocess.CalledProcessError as e:
            self.update_progress(0)
            messagebox.showerror("Error", f"An error occurred while cloning the repository:\n{e}")
            self.root.quit()

    def complete_install(self):
        self.step = 3
        self.update_progress(100)
        self.status_label.config(text="Installation completed. Preparing to finalize...")
        self.root.after(500, self.finish_install)

    def finish_install(self):
        messagebox.showinfo("Installation Complete", "Yanix-Launcher has been installed successfully!")
        self.root.quit()

    def cancel_install(self):
        if messagebox.askyesno("Cancel Installation", "Are you sure you want to cancel the installation?"):
            self.root.quit()

    def update_progress(self, progress):
        self.progress_var.set(progress)

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallWizard(root)
    root.mainloop()
