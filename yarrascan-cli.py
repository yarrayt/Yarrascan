#!/usr/bin/env python3

import os
import sys
import time
from pyfiglet import Figlet

VERSION = "1.0.0"

def show_banner():
    figlet = Figlet(font='slant')
    print(figlet.renderText('YARRASCAN'))
    print("Ultimate Terminal Security Toolkit - v" + VERSION)
    print("-" * 60)

def show_help():
    help_text = """
Welcome to YarraScan - Terminal Security Toolkit

Basic Options:
  -h, --help              Show this help message and exit
  -v, --version           Show YarraScan version

Main Functions:
  --menu                  Start interactive scan menu
  --about                 Show about and credits

Scan Categories:
  [1] Recon & OSINT
  [2] Subdomain Enumeration
  [3] Vulnerability Scanning
  [4] Web Crawling & Fuzzing
  [5] SQL Injection Testing
  [6] XSS Testing
  [7] Directory Bruteforce
  [8] OSINT Analysis
  [9] LFI Finder
 [10] Web App Testing
 [11] Password Bruteforce
 [12] Exploitation

Usage:
  python3 yarrascan-cli.py --menu
  ./yarrascan-cli.py --menu
"""
    print(help_text)

def show_about():
    print("""
YarraScan Suite v1.0.0
Developed by Raghav (CyberMonarch)
For ethical cybersecurity testing only.
""")

# === TOOL MENUS (Short demo version – customize with real commands) ===

def recon_menu():
    tools = {
        "1": "recon-ng",
        "2": "reconspider",
        "3": "theHarvester",
        "4": "Maltego",
        "5": "SpiderFoot",
        "6": "gobuster",
        "7": "dnsrecon"
    }

    print("\n[ Reconnaissance & OSINT Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        target = input("Enter target (domain/IP/keyword): ")

        cmd = ""
        if tool == "recon-ng":
            cmd = "recon-ng"
        elif tool == "reconspider":
            cmd = f"reconspider -d {target}"
        elif tool == "theHarvester":
            cmd = f"theHarvester -d {target} -l 100 -b all"
        elif tool == "Maltego":
            cmd = "maltego"
        elif tool == "SpiderFoot":
            cmd = "spiderfoot -l 127.0.0.1:5001"
        elif tool == "gobuster":
            wordlist = input("Enter wordlist path: ")
            cmd = f"gobuster dir -u {target} -w {wordlist}"
        elif tool == "dnsrecon":
            cmd = f"dnsrecon -d {target}"

        os.system(cmd)

        save = input("Do you want to save the output to a text file? (y/n): ")
        if save.lower() == "y":
            filename = input("Enter filename (without extension): ")
            os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 2: SUBDOMAIN ENUM -----------------------
def subdomain_menu():
    tools = {
        "1": "Sublist3r",
        "2": "subfinder",
        "3": "Amass",
        "4": "dnsmap",
        "5": "Katana"
    }

    print("\n[ Subdomain Enumeration Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        domain = input("Enter target domain: ")

        cmd = ""
        if tool == "Sublist3r":
            cmd = f"sublist3r -d {domain}"
        elif tool == "subfinder":
            cmd = f"subfinder -d {domain}"
        elif tool == "Amass":
            cmd = f"amass enum -d {domain}"
        elif tool == "dnsmap":
            cmd = f"dnsmap {domain}"
        elif tool == "Katana":
            cmd = f"katana -u https://{domain} -silent"

        os.system(cmd)

        save = input("Do you want to save the output to a text file? (y/n): ")
        if save.lower() == "y":
            filename = input("Enter filename (without extension): ")
            os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 3: VULNERABILITY SCANNING -----------------------
def vulnscan_menu():
    tools = {
        "1": "Nikto",
        "2": "OpenVAS",
        "3": "Wapiti",
        "4": "Vega",
        "5": "Nmap"
    }

    print("\n[ Vulnerability Scanning Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        target = input("Enter target domain or IP: ")

        cmd = ""
        if tool == "Nikto":
            cmd = f"nikto -h {target}"
        elif tool == "OpenVAS":
            print("[*] Please run Greenbone/OpenVAS via web interface or daemon.")
            return
        elif tool == "Wapiti":
            cmd = f"wapiti -u http://{target}/"
        elif tool == "Vega":
            print("[*] Vega is a GUI application. Launching...")
            cmd = "vega"
        elif tool == "Nmap":
            cmd = f"nmap -sV -Pn {target}"

        os.system(cmd)

        if cmd != "":
            save = input("Do you want to save the output to a text file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename (without extension): ")
                os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 4: WEB CRAWLING & FUZZING -----------------------
def crawling_menu():
    tools = {
        "1": "wfuzz",
        "2": "ffuf",
        "3": "sfuzz",
        "4": "Photon",
        "5": "Peach Fuzzer"
    }

    print("\n[ Web Crawling & Fuzzing Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        target = input("Enter target URL: ")

        cmd = ""
        if tool == "wfuzz":
            wordlist = input("Enter wordlist path: ")
            cmd = f"wfuzz -c -w {wordlist} --hc 404 {target}/FUZZ"
        elif tool == "ffuf":
            wordlist = input("Enter wordlist path: ")
            cmd = f"ffuf -u {target}/FUZZ -w {wordlist}"
        elif tool == "sfuzz":
            cmd = f"sfuzz -f fuzzcases.txt -m GET -u {target}"
        elif tool == "Photon":
            cmd = f"python3 photon.py -u {target} -o photon_output"
        elif tool == "Peach Fuzzer":
            print("[*] Peach Fuzzer requires a custom config. Launch GUI or script manually.")
            return

        os.system(cmd)

        save = input("Do you want to save the output to a text file? (y/n): ")
        if save.lower() == "y":
            filename = input("Enter filename (without extension): ")
            os.system(f"{cmd} > reports/{filename}.txt")


def sqli_menu():
    tools = {
        "1": "sqlmap",
        "2": "sqlninja",
        "3": "jSQL Injection",
        "4": "sqlifinder",
        "5": "BBQSQL"
    }

    print("\n[ SQL Injection Testing Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        target = input("Enter vulnerable URL or target: ")

        cmd = ""
        if tool == "sqlmap":
            cmd = f"sqlmap -u \"{target}\" --batch"
        elif tool == "sqlninja":
            cmd = f"sqlninja -u \"{target}\""
        elif tool == "jSQL Injection":
            print("[*] jSQL is a Java GUI tool. Launching...")
            cmd = "java -jar jsql-injection.jar"
        elif tool == "sqlifinder":
            cmd = f"sqlifinder -u \"{target}\""
        elif tool == "BBQSQL":
            cmd = "bbqsql"

        os.system(cmd)

        if tool in ["sqlmap", "sqlninja", "sqlifinder"]:
            save = input("Do you want to save the output to a text file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename (without extension): ")
                os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 6: XSS TESTING -----------------------
def xss_menu():
    tools = {
        "1": "XSSer",
        "2": "XSS-Freak",
        "3": "DalFox",
        "4": "XSStrike",
        "5": "Burp Suite"
    }

    print("\n[ XSS Testing Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        target = input("Enter target URL: ")

        cmd = ""
        if tool == "XSSer":
            cmd = f"xsser -u \"{target}\""
        elif tool == "XSS-Freak":
            cmd = f"python3 xssfreak.py -u \"{target}\""
        elif tool == "DalFox":
            cmd = f"dalfox url \"{target}\""
        elif tool == "XSStrike":
            cmd = f"python3 xsstrike.py -u \"{target}\""
        elif tool == "Burp Suite":
            print("[*] Burp Suite is a GUI tool. Launching...")
            cmd = "burpsuite"

        os.system(cmd)

        if tool in ["XSSer", "DalFox", "XSS-Freak", "XSStrike"]:
            save = input("Do you want to save the output to a text file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename (without extension): ")
                os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 7: DIRECTORY & FILE BRUTE-FORCING -----------------------
def brute_menu():
    tools = {
        "1": "ffuf",
        "2": "gobuster",
        "3": "dirbuster",
        "4": "dirsearch",
        "5": "wfuzz"
    }

    print("\n[ Directory & File Brute-Forcing Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        target = input("Enter target URL: ")
        wordlist = input("Enter path to wordlist: ")

        cmd = ""
        if tool == "ffuf":
            cmd = f"ffuf -u {target}/FUZZ -w {wordlist}"
        elif tool == "gobuster":
            cmd = f"gobuster dir -u {target} -w {wordlist}"
        elif tool == "dirbuster":
            print("[*] dirbuster is a GUI tool. Launching...")
            cmd = "dirbuster"
        elif tool == "dirsearch":
            cmd = f"python3 dirsearch.py -u {target} -w {wordlist}"
        elif tool == "wfuzz":
            cmd = f"wfuzz -c -w {wordlist} --hc 404 {target}/FUZZ"

        os.system(cmd)

        if tool != "dirbuster":
            save = input("Do you want to save the output to a text file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename (without extension): ")
                os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 8: OSINT ANALYSIS -----------------------
def osint_menu():
    tools = {
        "1": "social-analyzer",
        "2": "Sherlock",
        "3": "Maigret",
        "4": "Holehe"
    }

    print("\n[ OSINT Analysis Tools (Social Media Profiling) ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        identifier = input("Enter username or email: ")

        cmd = ""
        if tool == "social-analyzer":
            cmd = f"social-analyzer -q {identifier} --json"
        elif tool == "Sherlock":
            cmd = f"python3 sherlock/sherlock.py {identifier}"
        elif tool == "Maigret":
            cmd = f"maigret {identifier}"
        elif tool == "Holehe":
            cmd = f"holehe {identifier}"

        os.system(cmd)

        save = input("Do you want to save the output to a text file? (y/n): ")
        if save.lower() == "y":
            filename = input("Enter filename (without extension): ")
            os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 9: LFI VULNERABILITY FINDER -----------------------
def lfi_menu():
    print("\n[ Local File Inclusion (LFI) Finder ]")
    target = input("Enter target URL (use 'FUZZ' as injection point): ")
    wordlist = input("Enter path to LFI payload wordlist: ")

    print(f"\n[+] Fuzzing {target} for LFI vulnerabilities...\n")
    cmd = f"wfuzz -c -w {wordlist} --hc 404 {target}"

    os.system(cmd)

    save = input("Do you want to save the output to a text file? (y/n): ")
    if save.lower() == "y":
        filename = input("Enter filename (without extension): ")
        os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 10: WEB APPLICATION TESTING -----------------------
def webapp_menu():
    tools = {
        "1": "Burp Suite",
        "2": "OWASP ZAP",
        "3": "Nikto",
        "4": "w3af",
        "5": "Metasploit"
    }

    print("\n[ Web Application Testing Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        target = input("Enter target (if required): ")

        cmd = ""
        if tool == "Burp Suite":
            print("[*] Launching GUI...")
            cmd = "burpsuite"
        elif tool == "OWASP ZAP":
            cmd = "owasp-zap"
        elif tool == "Nikto":
            cmd = f"nikto -h {target}"
        elif tool == "w3af":
            print("[*] Opening w3af console...")
            cmd = "w3af_console"
        elif tool == "Metasploit":
            cmd = "msfconsole"

        os.system(cmd)

        if tool == "Nikto":
            save = input("Do you want to save the output to a text file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename (without extension): ")
                os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 11: PASSWORD BRUTE-FORCE -----------------------
def password_menu():
    tools = {
        "1": "John the Ripper",
        "2": "Hydra",
        "3": "Hashcat",
        "4": "Medusa",
        "5": "Crunch"
    }

    print("\n[ Password Brute-force & Dictionary Attack Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")

        cmd = ""
        if tool == "John the Ripper":
            hashfile = input("Enter path to hash file: ")
            cmd = f"john {hashfile}"
        elif tool == "Hydra":
            ip = input("Enter target IP: ")
            protocol = input("Enter protocol (e.g., ssh, ftp): ")
            userlist = input("Enter path to username list: ")
            passlist = input("Enter path to password list: ")
            cmd = f"hydra -L {userlist} -P {passlist} {ip} {protocol}"
        elif tool == "Hashcat":
            hashfile = input("Enter path to hash file: ")
            wordlist = input("Enter path to wordlist: ")
            cmd = f"hashcat -m 0 {hashfile} {wordlist}"
        elif tool == "Medusa":
            ip = input("Enter target IP: ")
            service = input("Enter service (e.g., ssh, ftp): ")
            userlist = input("Enter path to username list: ")
            passlist = input("Enter path to password list: ")
            cmd = f"medusa -h {ip} -U {userlist} -P {passlist} -M {service}"
        elif tool == "Crunch":
            min_len = input("Enter minimum length: ")
            max_len = input("Enter maximum length: ")
            charset = input("Enter character set or leave blank for default: ")
            cmd = f"crunch {min_len} {max_len} {charset}" if charset else f"crunch {min_len} {max_len}"

        os.system(cmd)

        if tool not in ["Crunch"]:
            save = input("Do you want to save the output to a text file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename (without extension): ")
                os.system(f"{cmd} > reports/{filename}.txt")


# ----------------------- POINT 12: EXPLOITATION -----------------------
def exploitation_menu():
    tools = {
        "1": "Metasploit",
        "2": "exploit-db",
        "3": "searchsploit",
        "4": "commix",
        "5": "BeEF"
    }

    print("\n[ Exploitation Tools ]")
    for key, val in tools.items():
        print(f"  {key}. {val}")

    choice = input("\nSelect a tool to run: ")

    if choice in tools:
        tool = tools[choice]
        print(f"\n[+] You selected {tool}")
        cmd = ""

        if tool == "Metasploit":
            cmd = "msfconsole"
        elif tool == "exploit-db":
            print("[*] Visit: https://www.exploit-db.com/")
            return
        elif tool == "searchsploit":
            keyword = input("Enter search keyword: ")
            cmd = f"searchsploit {keyword}"
        elif tool == "commix":
            url = input("Enter target URL: ")
            cmd = f"commix --url \"{url}\" --batch"
        elif tool == "BeEF":
            cmd = "beef-xss"

        os.system(cmd)

        if tool == "searchsploit" or tool == "commix":
            save = input("Do you want to save the output to a text file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename (without extension): ")
                os.system(f"{cmd} > reports/{filename}.txt")


# === MAIN MENU ===

def main_menu():
    while True:
        show_banner()
        print("""
[ Main Menu ]
1. Reconnaissance & OSINT
2. Subdomain Enumeration
3. Vulnerability Scanning
4. Web Crawling & Fuzzing
5. SQL Injection Testing
6. Cross-Site Scripting (XSS)
7. Directory & File Bruteforce
8. OSINT Analysis
9. LFI Finder
10. Web Application Testing
11. Password Brute-force
12. Exploitation
A. About
99. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1": recon_menu()
        elif choice == "2": subdomain_menu()
        elif choice == "3": vulnscan_menu()
        elif choice == "4": crawling_menu()
        elif choice == "5": sqli_menu()
        elif choice == "6": xss_menu()
        elif choice == "7": brute_menu()
        elif choice == "8": osint_menu()
        elif choice == "9": lfi_menu()
        elif choice == "10": webapp_menu()
        elif choice == "11": password_menu()
        elif choice == "12": exploitation_menu()
        elif choice.lower() == "a": show_about(); input("Press Enter to return...")
        elif choice == "99":
            print("Exiting YarraScan... Stay safe!")
            break
        else:
            print("Invalid input."); time.sleep(1)

# === ENTRY POINT ===

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()
    elif "--version" in sys.argv or "-v" in sys.argv:
        print("YarraScan CLI Version:", VERSION)
    elif "--menu" in sys.argv:
        main_menu()
    elif "--about" in sys.argv:
        show_about()
    else:
        print("Use -h or --help for usage information.")
