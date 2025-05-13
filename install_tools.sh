#!/bin/bash

echo "===================================="
echo "     YARRASCAN TOOL INSTALLER       "
echo "===================================="

# Step 1: Install Python dependencies
echo "[*] Installing Python packages..."
pip3 install -r requirements.txt

# Step 2: Install system tools (Kali Linux)
echo "[*] Installing required Kali tools..."
sudo apt update
sudo apt install -y \
  nmap sqlmap ffuf wfuzz gobuster dirsearch dirbuster \
  nikto zaproxy burpsuite john hydra hashcat metasploit-framework \
  theharvester recon-ng sublist3r amass dnsrecon dnsenum dnsmap \
  sherlock holehe xsstrike dalfox jsql spiderfoot \
  social-analyzer beef-xss commix

echo "[✓] All tools installed successfully!"
echo "You can now run the tool using: python3 yarrascan-cli.py --menu"
