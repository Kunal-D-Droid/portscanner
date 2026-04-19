# 🚀 Multi-Threaded Port Scanner

A fast, lightweight, and modern TCP port scanner written in Python. It uses multi-threading to quickly identify open ports on a target host.

---

## ✨ Features

- **⚡ Multi-Threaded**: Built with `ThreadPoolExecutor` for high-performance scanning.
- **🎨 Modern UI**: Beautiful, colorized terminal output using ANSI escape codes.
- **🛠️ Configurable**: Scan the top 1024 ports by default or specify a custom range.
- **⏳ Low Latency**: Optimized socket timeouts for faster results.
- **🛡️ Error Handling**: Robust handling of host resolution and connection errors.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kunal-D-Droid/portscanner.git
   cd portscanner
   ```

2. No external dependencies are required! (Uses standard libraries).

---

## 🛠️ Usage

### Default Scan (Ports 1-1024)
```bash
python portscanner.py <target_ip_or_hostname>
```

### Custom Range Scan
```bash
python portscanner.py <target_ip_or_hostname> <start_port> <end_port>
```
*Example:* `python portscanner.py 127.0.0.1 20 80`

---

## ⚠️ Disclaimer
This tool is for **educational and ethical testing purposes only**. Scanning networks without explicit permission is illegal in many jurisdictions and may violate your ISP's terms of service. The author is not responsible for any misuse of this tool.

---

## 👤 Author
**Kunal-D-Droid**
- GitHub: [@Kunal-D-Droid](https://github.com/Kunal-D-Droid)
