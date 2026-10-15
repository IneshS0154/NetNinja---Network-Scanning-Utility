import os
import socket
import ipaddress
import platform
import time
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389, 3306, 8080]


def is_port_open(host: str, port: int, timeout: float = 0.8) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))
        return True
    except Exception:
        return False


def scan_host_ports(host: str, ports=None):
    if ports is None:
        ports = COMMON_PORTS
    open_ports = []
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        return host, []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(is_port_open, ip, port): port for port in ports}
        for future in futures:
            port = futures[future]
            if future.result():
                open_ports.append(port)

    return host, open_ports


def scan_hosts(hosts, ports=None):
    results = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total} hosts"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("Scanning hosts", total=len(hosts))
        for host in hosts:
            host = host.strip()
            if not host:
                progress.advance(task)
                continue
            target, open_ports = scan_host_ports(host, ports)
            results.append((target, open_ports))
            progress.advance(task)
    return results


def scan_current_network():
    console = Console()
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    console.print("\n---Scan Current Network---", style="bold yellow")
    network_input = input("Enter CIDR network (example 192.168.1.0/24), or leave blank for 192.168.1.0/24: ").strip()
    if not network_input:
        network_input = "192.168.1.0/24"

    try:
        network = ipaddress.ip_network(network_input, strict=False)
    except ValueError:
        console.print("Invalid network format. Use a value like 192.168.1.0/24.", style="red")
        time.sleep(2)
        return

    hosts = [str(ip) for ip in network.hosts()]
    if len(hosts) > 50:
        console.print(f"Network contains {len(hosts)} hosts. Scanning the first 50 hosts only.", style="yellow")
        hosts = hosts[:50]

    console.print(f"Scanning {len(hosts)} hosts for common open ports...\n", style="green")
    results = scan_hosts(hosts)

    for host, open_ports in results:
        if open_ports:
            console.print(f"{host}: open ports -> {', '.join(str(p) for p in open_ports)}", style="bright_green")
        else:
            console.print(f"{host}: no common open ports found", style="cyan")

    input("\nScan complete. Press Enter to return to the menu.")


def scan_custom_targets():
    console = Console()
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    console.print("\n---Scan Custom Domains/IPs---", style="bold yellow")
    raw = input("Enter domains or IPs separated by commas: ").strip()
    hosts = [item.strip() for item in raw.split(",") if item.strip()]
    if not hosts:
        console.print("No targets entered.", style="red")
        time.sleep(2)
        return

    console.print(f"Scanning {len(hosts)} target(s) for common open ports...\n", style="green")
    results = scan_hosts(hosts)

    for host, open_ports in results:
        if open_ports:
            console.print(f"{host}: open ports -> {', '.join(str(p) for p in open_ports)}", style="bright_green")
        else:
            console.print(f"{host}: no common open ports found or host unreachable", style="cyan")

    input("\nScan complete. Press Enter to return to the menu.")
