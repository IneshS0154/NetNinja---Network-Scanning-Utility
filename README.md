<h1 align="center">🥷 NetNinja</h1>

<p align="center">
  <b>An open-source, terminal-based network scanning utility written in Python.</b><br/>
  Scan a subnet or a list of your own domains and IPs for open ports, from one clean interactive menu.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/UI-Rich-red?style=flat-square" alt="Rich"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square" alt="Platforms"/>
  <img src="https://img.shields.io/badge/Status-In%20development-orange?style=flat-square" alt="Status"/>
</p>

---

## 📖 About

NetNinja is a lightweight command-line tool for quick network reconnaissance on networks you own or manage. It checks hosts for **14 common service ports** (FTP, SSH, HTTP/HTTPS, SMB, RDP, MySQL and more) using multithreaded TCP connect scans, and shows live progress in the terminal with [Rich](https://github.com/Textualize/rich). Everything runs from an interactive menu, so there are no command-line flags to remember.

> **🚧 Project status:** NetNinja is under active development. Core scanning works; see the roadmap below for what's next.

## ✨ Features

- **🌐 Subnet scan**: enter any network in CIDR notation (e.g. `192.168.1.0/24`) or press Enter for the default `192.168.1.0/24`. Scans up to the first 50 hosts.
- **🎯 Custom target scan**: enter domains and/or IP addresses separated by commas; hostnames are resolved automatically and unreachable targets are reported.
- **⚡ Multithreaded port checks**: each host's ports are probed in parallel (20 worker threads, 0.8 s timeout).
- **📊 Live progress bar** with elapsed and remaining time.
- **🎨 Animated ASCII banner** and colour-coded results (open ports in green).
- **🖥️ Cross-platform**: works on Windows, Linux and macOS.

#### Ports checked

| Port | Service | Port | Service |
|---|---|---|---|
| 21 | FTP | 143 | IMAP |
| 22 | SSH | 443 | HTTPS |
| 23 | Telnet | 445 | SMB |
| 25 | SMTP | 3306 | MySQL |
| 53 | DNS | 3389 | RDP |
| 80 | HTTP | 8080 | HTTP (alt) |
| 110 | POP3 | 139 | NetBIOS |

## 🖥️ Preview

```
▐██████ ▐██████ ▐██████ ▐██████ ▐██ ▐██████ ▐██████ ▐██████
▐██ ▐██ ▐██       ▐██   ▐██ ▐██ ▐██ ▐██ ▐██     ▐██ ▐██ ▐██
▐██ ▐██ ▐████     ▐██   ▐██ ▐██ ▐██ ▐██ ▐██     ▐██ ▐██████
▐██ ▐██ ▐██       ▐██   ▐██ ▐██ ▐██ ▐██ ▐██ ▐██ ▐██ ▐██ ▐██
▐██ ▐██ ▐██████   ▐██   ▐██ ▐██ ▐██ ▐██ ▐██ ▐██████ ▐██ ▐██
Open Source Network Scanning Utility - IneshS

---Choose an Option---
[1] Scan current network
[2] Scan custom domains/IPs
[3] Exit

Response: 2
Enter domains or IPs separated by commas: 127.0.0.1, localhost
Scanning 2 target(s) for common open ports...

127.0.0.1: open ports -> 8080
localhost: open ports -> 8080
```

## 🚀 Getting started

### Prerequisites

- Python 3.8 or newer
- `pip`

### Installation

```bash
git clone https://github.com/IneshS0154/NetNinja---Network-Scanning-Utility.git
cd NetNinja---Network-Scanning-Utility

# optional: create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

Pick an option by typing its number and pressing **Enter**:

| Option | What it does |
|---|---|
| `1` Scan current network | Asks for a CIDR range (default `192.168.1.0/24`) and scans up to 50 hosts |
| `2` Scan custom domains/IPs | Asks for a comma-separated list, e.g. `192.168.1.1, myserver.local` |
| `3` Exit | Quits NetNinja |

After each scan, press **Enter** to return to the menu.

## 📁 Project structure

```
NetNinja/
├── main.py            # Entry point: menu loop that dispatches to the scanners
├── menu.py            # Animated ASCII banner, interactive menu and input validation
├── scanner.py         # Port-scanning logic, subnet/target scans and progress display
├── requirements.txt   # Python dependencies
└── .gitignore
```

## 🛠️ Built with

- **Python 3**: `socket`, `ipaddress` and `concurrent.futures` from the standard library
- **[Rich](https://github.com/Textualize/rich)**: coloured output and progress bars

## 🗺️ Roadmap

- [x] Interactive menu with animated banner
- [x] Multithreaded TCP port scanning of common ports
- [x] Subnet (CIDR) scanning
- [x] Custom domain/IP scanning with hostname resolution
- [ ] Auto-detect the local subnet for option 1
- [ ] Scan whole subnets quickly by scanning hosts in parallel
- [ ] Custom port lists and port ranges
- [ ] Display results in Rich tables with service names
- [ ] Export scan results to CSV / JSON
- [ ] Command-line flags for non-interactive use

## ⚠️ Responsible use

Only scan networks and hosts that you own or have explicit permission to test. Scanning systems without authorisation may be illegal where you live and may break the terms of service of your network provider. The author is not responsible for misuse of this tool.

## 🤝 Contributing

Contributions, issues and feature requests are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push the branch: `git push origin feature/my-feature`
5. Open a pull request

## 👤 Author

**Inesh Sandiv**: [GitHub](https://github.com/IneshS0154) · [LinkedIn](https://linkedin.com/in/inesh-sandiv-2aa742199)
