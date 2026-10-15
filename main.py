from menu import menuOptions
from scanner import scan_current_network, scan_custom_targets

if __name__ == "__main__":
    while True:
        choice = menuOptions()
        if choice == 1:
            scan_current_network()
        elif choice == 2:
            scan_custom_targets()
        else:
            break
    print("Goodbye!")
