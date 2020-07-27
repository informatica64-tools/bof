#! /bin/bash

# Upgrade repositories
sudo apt-get update

# Install tools for my pentests
sudo apt-get install curl nikto hydra padbuster smbclient nmap hashcat netcat john yersinia aircrack-ng ssh vsftpd wireshark snort cadaver atftpd -y

# Some tools neccesaries
sudo apt-get install -y postgresql apache2 php -y

# Spoofing tools
sudo apt-get install dsniff exiftool net-tools ettercap-graphical steghide binwalk -y

# Metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod +x msfinstall
sudo ./msfinstall

# Kali Linux repositories
sudo sh -c "echo 'deb https://http.kali.org/kali kali-rolling main non-free contrib' > /etc/apt/sources.list.d/kali.list"
sudo apt-get update -y
sudo apt-get install gnupg -y
wget 'https://archive.kali.org/archive-key.asc'
sudo apt-key add archive-key.asc
sudo apt-get update -y
sudo sh -c "echo 'Package: *'>/etc/apt/preferences.d/kali.pref; echo 'Pin: release a=kali-rolling'>>/etc/apt/preferences.d/kali.pref; echo 'Pin-Priority: 50'>>/etc/apt/preferences.d/kali.pref"
sudo apt-get update -y

sudo apt-get install exploitdb -y

sudo apt autoremove && sudo apt-get update -y
