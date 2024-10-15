# # SolarPuttyDecrypt Password Cracker

## Usage

This script attempts to crack the password for SolarPutty sessions using a wordlist.

### Prerequisites

- Download the SolarPuttyDecrypt tool from [here](https://github.com/VoidSec/SolarPuttyDecrypt/releases).
- Make sure you have your own wordlists ready for use.

### Running the Script

Run the script using the following command:

python script.py <decryptor_path> <session_file> <wordlist_file>

**Arguments:**
- `<decryptor_path>`: The full path to the SolarPuttyDecrypt executable.
- `<session_file>`: The path to your SolarPutty sessions file (`sessions.dat`).
- `<wordlist_file>`: The path to your wordlist file (e.g., `rockyou.txt`).

### Example Command

For Windows:
python script.py C:\SolarPuttyDecrypt\SolarPuttyDecrypt.exe C:\sessions.dat C:\rockyou.txt

For Linux or macOS (with Wine installed):
python script.py /path/to/SolarPuttyDecrypt.exe /path/to/sessions.dat /path/to/rockyou.txt

**Note:** If you are having problems with Wine like I was, just run this on a Windows machine.

### Credits

Credits to VoidSec for reverse engineering SolarPutty, so we don't have to. Learn more about the tool and how it works [here](https://voidsec.com/solarputtydecrypt/).

### Disclaimer

Use this script responsibly. The author is not responsible for any misuse of this tool or its consequences.