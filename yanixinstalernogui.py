import os
import subprocess

def install():
    repo_url = "https://github.com/NikoYandere/yanix-launcher"
    if os.path.exists("yanix-launcher"):
        print("Yanix-Launcher is already installed.")
    else:
        print("Cloning the repository...")
        subprocess.run(["git", "clone", repo_url])
        print("Installation complete!")

def uninstall():
    if os.path.exists("yanix-launcher"):
        print("Removing Yanix-Launcher...")
        subprocess.run(["rm", "-rf", "yanix-launcher"])
        print("Uninstallation complete!")
    else:
        print("Yanix-Launcher is not installed.")

def main():
    print("Select an option")
    print("1 - Install Yanix")
    print("2 - Uninstall Yanix")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        install()
    elif choice == "2":
        uninstall()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
