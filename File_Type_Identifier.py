import os

def check_file_type(file_path):
    file_name, extension = os.path.splitext(file_path)
    extension = extension.lower()

    with open(file_path, 'rb') as file:
        header_bytes = file.read(4)
        hex_signature = header_bytes.hex().upper()
        
        print(f"\n[+] Scanning: {file_path}")
        print(f"[+] File Signature Found: {hex_signature}")

        detected_type = "Unknown"

        if hex_signature.startswith("FFD8FF"):
            detected_type = ".jpg"
        elif hex_signature.startswith("89504E47"):
            detected_type = ".png"
        elif hex_signature.startswith("25504446"):
            detected_type = ".pdf"
        elif hex_signature.startswith("47494638"):
            detected_type = ".gif"

        print(f"[+] Detected actual format: {detected_type}")
        
        if detected_type == "Unknown":
            print("[-] WARNING: Could not identify this file type.")
        
        elif extension == detected_type or (extension == ".jpeg" and detected_type == ".jpg"):
            print("✅ SUCCESS: File extension matches the internal data.")
        
        else:
            print("🚨 ALERT! SECURITY RISK DETECTED! 🚨")
            print(f"--> The file claims to be {extension}")
            print(f"--> But the internal data says it is a {detected_type} file!")
            print("--> This file might be trying to trick you.")

try:
    user_file = input("Enter the name of the file to scan: ")
    check_file_type(user_file)
except FileNotFoundError:
    print("Error: I couldn't find that file!")
