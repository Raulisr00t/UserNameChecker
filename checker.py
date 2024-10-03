import requests
from bs4 import BeautifulSoup
import sys
from colorama import Style, Fore

apps = [
    'https://linkedin.com/in/',
    'https://instagram.com/',
    'https://github.com/',
    'https://pinterest.com/',
    'https://snapchat.com/add/',
    'https://tryhackme.com/p/',
    'https://twitch.tv/',
    'https://medium.com/@',
    'https://reddit.com/user/',
    'https://discord.com/invite/'
]

try:
    username = input("[>>] Enter a target username for searching: ")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for app in apps:
        url = app + username
        print(Fore.YELLOW + f"Checking {url}" + Style.RESET_ALL)

        response = requests.get(url, headers=headers, allow_redirects=False)

        # Special handling for Twitch
        if app == 'https://twitch.tv/':
            content = BeautifulSoup(response.content, 'html.parser')
            error_message = content.find('p', {'data-a-target': 'core-error-message'})

            if error_message and 'Sorry. Unless you\'ve got a time machine, that content is unavailable.' in error_message.text:
                print(Fore.RED + f"[-] Not Found on {app}" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + f"[+] Found on {app}" + Style.RESET_ALL)
            continue

        # Special handling for Discord
        if app == 'https://discord.com/invite/':
            content = BeautifulSoup(response.content, 'html.parser')
            error_message = content.find('h1', class_='heading-xl/semibold_dc00ef')

            if error_message and 'Invite Invalid' in error_message.text:
                print(Fore.RED + f"[-] Not Found on {app}" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + f"[+] Found on {app}" + Style.RESET_ALL)
            continue

        # General case: Check status code for all other apps
        if response.status_code < 300:
            print(Fore.BLUE + f"[+] Found on {app}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"[-] Not found on {app}" + Style.RESET_ALL)

except KeyboardInterrupt:
    print("\n[!] User stopped the tool forcibly!")
    sys.exit()
