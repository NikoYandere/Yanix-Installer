import os
import subprocess

def install():
    repo_url = "https://github.com/NikoYandere/Yanix-Launcher"
    if os.path.exists("yanix-launcher"):
        print("O Yanix-Launcher já está instalado.")
    else:
        print("Clonando o repositório...")
        subprocess.run(["git", "clone", repo_url])
        print("Instalação concluída!")

def uninstall():
    if os.path.exists("yanix-launcher"):
        print("Removendo o Yanix-Launcher...")
        subprocess.run(["rm", "-rf", "yanix-launcher"])
        print("Desinstalação concluída!")
    else:
        print("O Yanix-Launcher não está instalado.")

def main():
    print("select an option")
    print("1 - Install Yanix")
    print("2 - Uninstall Yanix")
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == "1":
        install()
    elif escolha == "2":
        uninstall()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()

