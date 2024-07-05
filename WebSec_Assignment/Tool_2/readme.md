# Network Security Scanner Tool

## Overview
The Network Security Scanner tool is designed to help users identify open ports on a given IP address, enhancing network security by identifying potential vulnerabilities. The tool consists of three main files:
1. **ip_add.py**: This script outputs the IP address corresponding to a given domain name.
2. **port_scanner.py**: This script scans the common ports 22, 443, and 80 of a provided target IP address to determine their status (open/closed).
3. **net_scan.py**: This is the main script that takes an IP address as input from the user and scans it to check the status of the ports within a specified time frame.

## Libraries Used
- **socket**: Provides low-level networking interface.
- **subprocess**: Allows spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.
- **datetime**: Supplies classes for manipulating dates and times.

## Working of the Main Code (net_scan.py)
The `net_scan.py` script uses the imported libraries as follows:
1. **User Input**: The script prompts the user to input an IP address and the desired time frame for the scan.
2. **Socket Module**: Utilizes the `socket` library to create connections to the target IP address on the specified ports (22, 443, 80) to determine their status.
3. **Subprocess Module**: Can be used to run auxiliary commands or scripts if needed for advanced network operations or data processing.
4. **Datetime Module**: Records the start and end times of the scan to ensure it completes within the provided time frame and for logging purposes.

### Workflow
1. **Input Handling**: The user is prompted to enter the IP address they want to scan.
2. **Port Scanning**: The script iterates over the predefined ports (22, 443, 80), attempting to establish a connection using the `socket` library. If a connection is successful, the port is marked as open; otherwise, it is marked as closed.
3. **Time Management**: The `datetime` library is used to track the scan duration, ensuring that the process completes within the user-specified time limit.
4. **Output**: The results of the scan (whether each port is open or closed) are displayed to the user.

This tool provides a straightforward and efficient method to check the status of critical ports on a target IP address, helping users identify potential security issues quickly.

---

Thank you for using the Network Security Scanner tool. Your feedback and contributions are welcome to improve and extend the functionality of this tool.
