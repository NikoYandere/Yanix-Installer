import subprocess
import os
import tkinter as tk
from tkinter import messagebox

YANIX_PATH = os.path.expanduser("~/yanix-launcher")
GITHUB_REPO = "https://github.com/NikoYandere/Yanix-Launcher"

# Função para encontrar a pasta "yanix-installer" em qualquer local
def find_installer_path():
    for root, dirs, _ in os.walk("/"):
        if "yanix-installer" in dirs:
            return os.path.join(root, "yanix-installer")
    return None

INSTALLER_PATH = find_installer_path()
BG_PATH = os.path.join(INSTALLER_PATH, "data/background.png") if INSTALLER_PATH else None

def install():
    if not os.path.exists(YANIX_PATH):
        subprocess.run(["git", "clone", GITHUB_REPO, YANIX_PATH], check=True)
        messagebox.showinfo("Success", "Yanix Launcher installed successfully!")
    else:
        messagebox.showinfo("Info", "Yanix Launcher is already installed.")

def uninstall():
    if os.path.exists(YANIX_PATH):
        subprocess.run(["rm", "-rf", YANIX_PATH], check=True)
        messagebox.showinfo("Success", "Yanix Launcher uninstalled successfully!")
    else:
        messagebox.showinfo("Info", "Yanix Launcher is not installed.")

top = tk.Tk()
top.title("Yanix Launcher Installer")
top.geometry("800x600")
top.resizable(False, False)

if BG_PATH and os.path.exists(BG_PATH):
    bg_image = tk.PhotoImage(file=BG_PATH)
    bg_label = tk.Label(top, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

tk.Button(top, text="Install", font=("Arial", 14), command=install).place(relx=0.5, rely=0.4, anchor=tk.N)
tk.Button(top, text="Uninstall", font=("Arial", 14), command=uninstall).place(relx=0.5, rely=0.5, anchor=tk.N)

top.mainloop()
