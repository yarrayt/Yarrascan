## Yarrascan:

"Brahmastra" is a powerful security analysis tool inspired by the ancient Indian mythology of Lord Brahma. Just as Lord Brahma was known for his divine wisdom and knowledge, this tool embodies those qualities by offering a comprehensive range of security assessment functionalities. With its Python-based script, Brahmastra combines network scanning, web crawling, vulnerability scanning, and CMS detection capabilities. By utilizing external tools and modules, it enables users to discover social media profiles, gather information, perform SSL analysis, identify subdomains, detect vulnerabilities such as SQL injection and XSS, and much more. The tool's intuitive menu system provides an easy-to-use interface, empowering security professionals to conduct thorough security assessments and uncover potential vulnerabilities and weaknesses in target systems. Embracing the name of an ancient divine weapon, Brahmastra aims to provide security practitioners with a potent tool to safeguard modern digital environments.

## 🛠️ Installation:

* Simply execute the following command

```bash
git clone https://github.com/yarrayt/Yarrascan.git
```

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python libraries requirements.

```bash
sudo apt install python3-pip -y
```

```bash
cd Yarrascan
chmod +x *
sudo pip3 install -r requirements.txt
```

* Then install the other requirements.

```bash
sudo ./install_tools.sh
```

## 🎯 Features:

📊 Reconnaissance & OSINT Integration – Easily run tools like recon-ng, theHarvester, SpiderFoot, and more for detailed target information gathering.

🌐 Subdomain Enumeration – Automates discovery using tools like sublist3r, amass, subfinder, and Katana.

🛡️ Vulnerability Scanning – Leverages tools like nikto, nmap, and wapiti to find known weaknesses in web servers and applications.

📂 Web Crawling & Fuzzing – Supports ffuf, wfuzz, Photon, and dirsearch for fast discovery of hidden files, URLs, and parameters.

💉 SQL Injection Testing – Automates detection and exploitation using sqlmap, sqlninja, and sqlifinder.

⚠️ Cross-Site Scripting (XSS) Testing – Find XSS vulnerabilities using advanced scanners like DalFox, XSStrike, and XSSer.

🔎 Directory & File Brute-forcing – Use gobuster, dirbuster, and wfuzz to uncover hidden directories and sensitive files.

🧠 OSINT & Social Profiling – Tools like Sherlock, Holehe, and social-analyzer help identify online identities and footprints.

📁 LFI Vulnerability Scanning – Detect local file inclusion vulnerabilities through custom wordlists and fuzzing tools.

🔍 Web Application Analysis – Launch Burp Suite, OWASP ZAP, and w3af for in-depth app security testing.

🔐 Password Brute-force Attacks – Perform dictionary attacks using Hydra, John the Ripper, Medusa, and Hashcat.

💣 Exploitation Tools Launcher – Directly access Metasploit, commix, BeEF, and searchsploit from the menu for post-recon attacks.

These are the main features of the Brahmastra tool, offering a range of functionalities for reconnaissance, vulnerability assessment, and security testing.


## ⁉️ Usage:

```bash
python3 yarrascan-cli.py
```

## 📸 Screenshot:

![alt text](https://github.com/yarrayt/Yarrascan/blob/main/assets/img/Main-Menu.png)


## 💚 Contributing:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## 🔑 License:

Distributed under the GNU V3.0 License. See [LICENSE](https://github.com/yarrayt/Yarrascan/blob/main/LICENSE) for more information.

-----
Project Maintainer: [Raghav Dixit](https://github.com/yarrayt/) 



[<img src="https://img.icons8.com/color/48/000000/linkedin.png"/>](https://www.linkedin.com/in/raghav-dixit-ba8265247/)
<img src="C:\Users\ragha\Yarrascan\assets\img\TryHackMe" alt="TryHackMe">
<img src="C:\Users\ragha\Yarrascan\assets\img\Portswiger" alt="Portswiger">