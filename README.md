# UserNameChecker
UserNameChecker is a Python-based script that searches for a specific username across multiple popular websites. It automates the process of checking if a given username exists on social media platforms and other services.

## Features
Checks for a username on platforms like LinkedIn, Instagram, GitHub, Pinterest, Snapchat, and more.
Provides detailed feedback on whether the username exists on the specified platforms.
Special handling for platforms like Twitch and Discord with additional parsing for their unique error messages.
User-friendly output with color coding for easy reading (using colorama).

## Prerequisites
Python 3.x
The following Python packages:
requests
BeautifulSoup4
colorama
You can install the required packages using:

```powershell
pip install requests beautifulsoup4 colorama
```

## Usage
`.Clone the repository or download the script.
```powershell
git clone https://github.com/Raulisr00t/UserNameChecker.git
```
2.Run the script in your terminal and enter the target username when prompted:
```powershell
python3 checker.py
```
3.The script will check if the username is available across multiple platforms and will display the results in color:

Yellow: Checking the platform.
Blue: Username found on the platform.
Red: Username not found on the platform.

Example Output
```powershell
[>>] Enter a target username for searching: exampleUser
Checking https://linkedin.com/in/exampleUser
[-] Not found on https://linkedin.com/in/
Checking https://instagram.com/exampleUser
[+] Found on https://instagram.com/
...
```
### Platforms Supported
The script checks the username on the following platforms:

LinkedIn
Instagram
GitHub
Pinterest
Snapchat
TryHackMe
Twitch
Medium
Reddit
Discord

### Error Handling
Twitch: The script checks the specific error message returned by Twitch if the username doesn't exist.
Discord: The script handles the invalid invite error message and informs the user if the username is not associated with an invite.

### Customization
To add or remove platforms, simply modify the apps list within the script by adding or removing URLs with the appropriate format.

## Notes
The script simulates a browser request by using a User-Agent header. This helps avoid being blocked by some platforms.
It checks the username by making GET requests and verifies the presence of the username based on the platform’s HTTP response or error messages.

## License
This project is licensed under the MIT License. You are free to modify and distribute the code.
