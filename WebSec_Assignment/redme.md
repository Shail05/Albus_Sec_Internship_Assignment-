# Web Security Assignment

## Overview
This assignment focuses on enhancing web security through the development of two essential tools:

1. **Password Manager Tool**
2. **Network Security Scanner Tool**

Each tool addresses specific aspects of web security, providing users with powerful features to protect and manage their digital assets. The development of these tools not only strengthened my understanding of web security principles but also significantly improved my Python coding skills through hands-on practice and problem-solving.

## Tools Description

### Password Manager Tool

The **Password Manager Tool** is designed to securely store and retrieve passwords. It includes the following features:

- **Secure Storage and Retrieval**: Allows users to securely store and retrieve their passwords.
- **Password Generation**: Generates strong, random passwords to enhance security.
- **Encryption**: Encrypts stored passwords to protect them from unauthorized access.

#### Code Structure

- **pass_manager(main).py**: Main script for integrating functionalities from other files.
- **pass_manager.py**: Handles core functionality for storing and retrieving passwords.
- **password_generator.py**: Generates strong passwords using cryptographic techniques.
- **encod_decod.py**: Encodes and decodes passwords using Base64 and Fernet symmetric encryption.

#### Libraries Used

- **hashlib**: Provides a common interface to many secure hash and message digest algorithms.
- **getpass**: Facilitates secure handling of passwords and other sensitive input.
- **os**: Provides a way of using operating system-dependent functionality like reading or writing to the file system.
- **base64**: Provides functions for encoding binary data to Base64 and decoding Base64 back to binary data.
- **secrets**: Provides functions for generating secure random numbers suitable for cryptographic use.
- **string**: Contains a collection of string constants and utility functions.
- **cryptography.fernet**: Implements the Fernet symmetric encryption standard.
- **cryptography.hazmat.primitives.hashes**: Provides a variety of cryptographic hash functions.
- **cryptography.hazmat.primitives.kdf.pbkdf2**: Implements the PBKDF2 key derivation function.

#### Working of the Main Code

The `pass_manager(main).py` script serves as the entry point of the application. It interprets the user's choices and executes the corresponding functions:

1. **User Interaction**: Presents options to the user and collects input.
2. **Password Generation**: Utilizes the secure random generation functions and encrypts the generated password.
3. **Adding Passwords**: Stores new passwords securely in a file.
4. **Retrieving Passwords**: Retrieves and securely handles stored passwords.

The Password Manager Tool ensures secure encryption, easy retrieval, and safe storage of passwords, enabling users to manage their passwords efficiently and securely.

### Network Security Scanner Tool

The **Network Security Scanner Tool** is designed to help users identify open ports on a given IP address, enhancing network security by identifying potential vulnerabilities. It includes the following features:

- **IP Address Identifier**: Provides the IPv4 address of a domain name.
- **Port Scanning**: Scans common ports (22, 443, 80) on a target IP to determine their status (open/closed).
- **Network Traffic Analysis**: Provides insights into network traffic patterns, protocols, and potential security vulnerabilities.

#### Code Structure

- **ip_add.py**: Outputs the IP address corresponding to a given domain name.
- **port_scanner.py**: Scans specified ports on a target IP to check their status.
- **net_scan.py**: Main script for analyzing network traffic and identifying security vulnerabilities.

#### Libraries Used

- **socket**: Provides low-level networking interface.
- **subprocess**: Allows spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.
- **datetime**: Supplies classes for manipulating dates and times.

#### Working of the Main Code

The `net_scan.py` script uses the imported libraries as follows:

1. **User Input**: Prompts the user to input an IP address and the desired time frame for the scan.
2. **Socket Module**: Creates connections to the target IP address on the specified ports (22, 443, 80) to determine their status.
3. **Subprocess Module**: Runs auxiliary commands or scripts if needed for advanced network operations or data processing.
4. **Datetime Module**: Tracks the scan duration to ensure completion within the user-specified time limit and logs the start and end times.

#### Workflow

1. **Input Handling**: Prompts the user to enter the IP address they want to scan.
2. **Port Scanning**: Iterates over the predefined ports, attempting to establish connections and marking their status.
3. **Time Management**: Uses the `datetime` library to monitor and limit scan duration.
4. **Output**: Displays the results of the scan (whether each port is open or closed) to the user.

The Network Security Scanner Tool provides a straightforward and efficient method to check the status of critical ports on a target IP address, helping users identify potential security issues quickly.

## Conclusion

This Web Security Assignment was a valuable experience that enhanced my web security knowledge and significantly improved my Python programming skills. The development of the **Password Manager Tool** and the **Network Security Scanner Tool** equipped me with practical skills and a deeper understanding of cybersecurity concepts.

Thank you for using these tools. Your feedback and contributions are welcome to improve and extend their functionality. For any queries or further assistance, please refer to the documentation.
