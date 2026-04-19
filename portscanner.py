#!/usr/bin/env python3

import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ANSI Color Codes
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def print_banner(target, start_port, end_port):
    print(BLUE + "-" * 50 + RESET)
    print(f"{YELLOW}Scanning target:{RESET} {target}")
    print(f"{YELLOW}Port Range:{RESET} {start_port} - {end_port}")
    print(f"{YELLOW}Time started:{RESET} {datetime.now()}")
    print(BLUE + "-" * 50 + RESET)

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{GREEN}[+] Port {port} is open{RESET}")
        s.close()
    except Exception:
        pass

def main():
    if len(sys.argv) < 2:
        print(RED + "Error: Target not specified." + RESET)
        print(f"Syntax: python {sys.argv[0]} <target> [start_port] [end_port]")
        print("Example: python portscanner.py 127.0.0.1 1 100")
        sys.exit(1)

    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print(RED + "Error: Hostname could not be resolved." + RESET)
        sys.exit(1)

    start_port = 1
    end_port = 1024

    if len(sys.argv) >= 3:
        start_port = int(sys.argv[2])
    if len(sys.argv) >= 4:
        end_port = int(sys.argv[3])

    print_banner(target, start_port, end_port)

    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, target, port)
    except KeyboardInterrupt:
        print(RED + "\nExiting program..." + RESET)
        sys.exit()
    except socket.error:
        print(RED + "Error: Could not connect to server." + RESET)
        sys.exit()

if __name__ == "__main__":
    main()
