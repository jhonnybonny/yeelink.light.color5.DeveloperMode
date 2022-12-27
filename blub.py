import subprocess
login = input("Username (email or user ID): ")
password = input("Password: ")
# Set the input for the script
input_str = f"{login}\n{password}\nde\n"

# Encode the input string to bytes
input_bytes = input_str.encode()

# Run the token_extractor.py script and provide the input
output = subprocess.run(["python3", "token_extractor.py"], 
input=input_bytes, capture_output=True).stdout.decode()

# Parse the output to extract the TOKEN and IP values for the specified 
device
device_name = "Mi Smart LED Bulb Essential (White and Color)"
for line in output.splitlines():
    if "NAME" in line and device_name in line:
        # We are at the correct device, extract the TOKEN and IP values
        for line in output.splitlines()[1:]:
            if "TOKEN" in line:
                _, token = line.split(": ")
                token = token.strip()
            elif "IP" in line:
                _, ip = line.split(": ")
                # Remove leading whitespace characters from the IP value
                ip = ip.strip()

# Use the TOKEN and IP values in the miiocli command
subprocess.run(["miiocli", "yeelight", "--ip", ip, "--token", token, 
"set_developer_mode", "1"])


