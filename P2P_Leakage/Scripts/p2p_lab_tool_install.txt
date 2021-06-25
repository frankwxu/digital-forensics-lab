#!/bin/bash

echo "*******************************"
echo "*                             *"
echo "*    Installation Script      *"
echo "*                             *"
echo "*                             *"
echo "*   University of Baltimore   *"
echo "*                             *"
echo "*******************************"


echo -e "Installing necessary tools...\n"

# Installing tools

sudo apt update -y

sudo apt install git hashdeep libreoffice mutt python2 python3 python3-evtx sleuthkit sqlite3 sqlitebrowser xmlstarlet wine64 -y
sudo apt install vinetto tree libhivex-bin python3-hivex libesedb-utils pasco pff-tools libnl-utils libvshadow-utils ewf-tools -y
sudo apt install python-setuptools python3-setuptools python3-plaso pip foremost pst-utils bulk_extractor libimage-exiftool-perl -y
pip3 install time-decode
sudo apt install npm -y
sudo npm install -g imgclip 

cd ~/Downloads
wget https://raw.githubusercontent.com/dfir-scripts/installers/main/RegRipper30-apt-git-Install.sh
sudo bash RegRipper30-apt-git-Install.sh
rm RegRipper30-apt-git-Install.sh
wget https://github.com/torrent-file-editor/torrent-file-editor/releases/download/v0.3.17/torrent-file-editor-0.3.17-x64.exe
wget https://f001.backblazeb2.com/file/EricZimmermanTools/JLECmd.zip
unzip JLECmd.zip && rm JLECmd.zip

# Installing other tools

mkdir ~/Forensic_Tools
mv torrent-file-editor-0.3.17-x64.exe ~/Forensic_Tools
cd ~/Forensic_Tools
git clone https://github.com/volatilityfoundation/volatility.git
git clone https://github.com/volatilityfoundation/volatility3.git
git clone https://github.com/PoorBillionaire/USN-Journal-Parser.git
git clone https://github.com/PoorBillionaire/USN-Record-Carver.git
git clone https://github.com/PoorBillionaire/Windows-Prefetch-Parser.git
git clone https://github.com/prolsen/recentfilecache-parser.git
git clone https://github.com/dkovar/analyzeMFT.git
mkdir JLECmd && mv ~/Downloads/JLECmd.exe ./JLECmd
mkdir Torrent_File_Editor && mv ~/Downloads/torrent-file-editor-0.3.17-x64.exe ./Torrent_File_Editor
cd

# Installing terminal emulator

sudo apt install terminator -y

# Ending
echo -e "\nFinished!\n"