import subprocess
import os
import sys

# Function to attempt password cracking
def crack_password(decryptor_path, session_file, wordlist_file):
    # Open the password file and try each password
    with open(wordlist_file, 'r', encoding='latin-1') as f:
        for password in f:
            password = password.strip()  # Remove any newlines or extra spaces
            print(f"Trying password: {password}")
            
            # Run the decryptor with the current password
            result = subprocess.run([decryptor_path, session_file, password], capture_output=True, text=True)
            
            # Check if the command was successful
            if result.returncode == 0:
                print(f"Correct password found: {password}\n")
                os.system(f'{decryptor_path} {session_file} {password}')
                break
            else:
                print(f"Failed with password: {password}")

    print("Process complete.")

if __name__ == "__main__":
    # Ensure the user provides the correct number of arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <decryptor_path> <session_file> <wordlist_file>")
        sys.exit(1)
    
    # Assign command-line arguments to variables
    decryptor_path = sys.argv[1]
    session_file = sys.argv[2]
    wordlist_file = sys.argv[3]
    
    # Call the crack_password function with the provided arguments
    crack_password(decryptor_path, session_file, wordlist_file)