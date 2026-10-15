from rich.console import Console
import os
import time
import platform
import random

console = Console()
animated_menu_shown = False
last_art_variant = None

ASCII_ARTS = [
    r"""
▐██████ ▐██████ ▐██████ ▐██████ ▐██ ▐██████ ▐██████ ▐██████
▐██ ▐██ ▐██       ▐██   ▐██ ▐██ ▐██ ▐██ ▐██     ▐██ ▐██ ▐██
▐██ ▐██ ▐████     ▐██   ▐██ ▐██ ▐██ ▐██ ▐██     ▐██ ▐██████
▐██ ▐██ ▐██       ▐██   ▐██ ▐██ ▐██ ▐██ ▐██ ▐██ ▐██ ▐██ ▐██
▐██ ▐██ ▐██████   ▐██   ▐██ ▐██ ▐██ ▐██ ▐██ ▐██████ ▐██ ▐██
    """,
]


def menuArt(animated=False, variant=0):
    ascii_art = ASCII_ARTS[variant]
    if animated:
        for line in ascii_art.splitlines():
            console.print(line, style="red")
            time.sleep(0.03)
    else:
        console.print(ascii_art, style="red")
    console.print("Open Source Network Scanning Utility - IneshS", style="bold red")


def menuOptions():
    global animated_menu_shown, last_art_variant
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        variant = random.randrange(len(ASCII_ARTS))
        if len(ASCII_ARTS) > 1 and variant == last_art_variant:
            variant = (variant + 1) % len(ASCII_ARTS)
        menuArt(animated=not animated_menu_shown, variant=variant)
        last_art_variant = variant
        animated_menu_shown = True
        console.print("\n---Choose an Option---")
        console.print("[1] Scan current network", style="green")
        console.print("[2] Scan custom domains/IPs", style="green")
        console.print("[3] Exit\n", style="green")

        try:
            usrInp = int(input("Response: "))
            if 1 <= usrInp <= 3:
                return usrInp
            else:
                console.print("Invalid option! Please enter 1, 2, or 3.", style="red")
                time.sleep(2)

        except ValueError:
            console.print("Invalid input! Please enter a number.", style="red")
            time.sleep(2)
