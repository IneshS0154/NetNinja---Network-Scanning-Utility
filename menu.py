from rich.console import Console
import os
import time
import platform

console = Console()

def menuArt():
    ascii_art = r"""
    _    _      _   _   _ _        _       
    | \ | | ___| |_| \ | (_)_ __  (_) __ _ 
    |  \| |/ _ \ __|  \| | | '_ \ | |/ _` |
    | |\  |  __/ |_| |\  | | | | || | (_| |
    |_| \_|\___|\__|_| \_|_|_| |_|/ |\__,_|
                                |__/       
    """
    console.print(ascii_art, style="red")
    console.print("Open Source Network Scanning Utility - IneshS", style="bold red")

def menuOptions():
    
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        menuArt()
        console.print("\n---Choose an Option---")
        console.print("[1]Scan current Network", style="green")
        console.print("[2]Scan Custom domains/IPs", style="green")
        console.print("[3]Exit\n", style="green")
        
        try:
            usrInp = int(input("Response: "))
            if 1 <= usrInp <= 3:
                return usrInp
            else:
                console.print("Invalid option! Please enter 1, 2, or 3.", style="red")
                time.sleep(3)
                os.system('cls' if platform.system() == 'Windows' else 'clear')
                
        except ValueError:
            console.print("Invalid input! Please enter a number.", style="red") 
            time.sleep(3)
            os.system('cls' if platform.system() == 'Windows' else 'clear')