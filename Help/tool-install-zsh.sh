#!/bin/bash

echo 'This might take a while. Please wait...'


# Update apt first
sudo apt update -y 


# Install Python-related tools first
# Note: -y means the install will go through without user input
sudo apt install python-setuptools python3-pip -y


# Install software that can be installed from the repository
sudo apt install vinetto tree python3-evtx xmlstarlet libhivex-bin python3-hivex libesedb-utils pasco pff-tools libnl-utils libvshadow-utils -y
pip3 install time-decode 
sudo apt install npm -y
sudo npm install -g imgclip


# Installing Regripper
cd ~/Downloads
wget https://raw.githubusercontent.com/siftgrab/siftgrab/master/regripper.conf/RegRipper30-apt-git-Install.sh 
sudo bash RegRipper30-apt-git-Install.sh


# Git clone other tools
mkdir ~/UB-730-Tools
cd ~/UB-730-Tools
git clone https://github.com/PoorBillionaire/USN-Record-Carver.git
git clone https://github.com/dkovar/analyzeMFT.git
git clone https://github.com/PoorBillionaire/USN-Journal-Parser.git
git clone https://github.com/PoorBillionaire/Windows-Prefetch-Parser.git
git clone https://github.com/prolsen/recentfilecache-parser.git

# Installing JLEC 
cd ~/Downloads
wget https://f001.backblazeb2.com/file/EricZimmermanTools/JLECmd.zip
unzip JLECmd.zip && mkdir ~/UB-730-Tools/JLEC && mv JLECmd.exe ~/UB-730-Tools/JLEC 


# Installing wine
sudo apt install wine wine64 -y
cd ~/Downloads
wget https://dl.winehq.org/wine/wine-mono/5.0.0/wine-mono-5.0.0-x86.msi


# Create .zsh_aliases file. .bashrc is set to run this file by default.
# This will allow you to call the git cloned programs anywhere in the terminal. Current solution anyway.
touch ~/.zsh_aliases
echo "alias prefetch.py='python2 ~/UB-730-Tools/Windows-Prefetch-Parser/windowsprefetch/prefetch.py'" >> ~/.zsh_aliases
echo "alias rfcparse.py='python2 ~/UB-730-Tools/recentfilecache-parser/rfcparse.py'" >> ~/.zsh_aliases
echo "alias usn.py='python2 ~/UB-730-Tools/USN-Journal-Parser/usnparser/usn.py'">> ~/.zsh_aliases
echo "alias usncarve.py='python2 ~/UB-730-Tools/USN-Record-Carver/usncarve.py'" >> ~/.zsh_aliases
echo "alias analyzeMFT.py='python2 ~/UB-730-Tools/analyzeMFT/analyzeMFT.py'" >> ~/.zsh_aliases
echo "alias JLECmd.exe='wine64 ~/UB-730-Tools/JLEC/JLECmd.exe'" >> ~/.zsh_aliases 


# Allow .zshrc to run .zshaliases
echo "" >> ~/.zshrc
echo '# Alias definitions' >> ~/.zshrc
echo 'if [ -f ~/.zsh_aliases ]; then' >> ~/.zshrc
echo '    . ~/.zsh_aliases' >> ~/.zshrc
echo 'fi' >> ~/.zshrc

 
# Creating reference file in case user doesn't know how to call these commands 
touch ~/UB-730-Tools/Tools-Reference.txt
echo 'This is a reference for all of the programs installed via the script.' >> ~/UB-730-Tools/Tools-Reference.txt
echo "" >> ~/UB-730-Tools/Tools-Reference.txt
echo "" >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Key: Program --> Command' >> ~/UB-730-Tools/Tools-Reference.txt
echo '-------------------------' >> ~/UB-730-Tools/Tools-Reference.txt
echo '' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'AnalyzeMFT --> analyzeMFT.py' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Hivex --> hivexsh' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'libesedb --> esedbinfo, esedbexport' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'libpff --> pffinfo, pffexport' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'libvshadow --> vshadowdebug, vshadowinfo, vshadowmount' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'libnl --> nl, nl-* (There are many different commands; type in nl- and press TAB key twice to see)' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Pasco --> pasco' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Python-evtx --> evtx_info.py, evtx_dump.py (There are other commands; type in evtx_ and press TAB key twice to see)' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Regripper --> rip.pl' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'RecentFileCacheParser --> rfcparse.py' >>~/UB-730-Tools/Tools-Reference.txt
echo 'Tree --> tree' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Time-Decode --> time_decode.py' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'USNJournalParser --> usn.py' >> ~/UB-730-Tools/Tools-Reference.txt
echo  'USNRecordCarver --> usncarve.py'>> ~/UB-730-Tools/Tools-Reference.txt
echo 'Vinetto --> vinetto' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'WindowsPrefetchParser --> prefetch.py' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Xmlstarlet --> xmlstarlet' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'JLECmd --> JLECmd.exe' >> ~/UB-730-Tools/Tools-Reference.txt
echo 'Imgclip --> imgclip' >> ~/UB-730-Tools/Tools-Reference.txt


# Creating README.txt
touch ~/UB-730-Tools/README.txt
echo "Warning: If you move any of the tools' folders, the settings I put may/will break. If you know everything I did, great, if not, be careful." >> ~/UB-730-Tools/README.txt
echo "" >> ~/UB-730-Tools/README.txt
echo "As of now, you do not have to type in the full path to use any of these programs. I took care of that for you. See Tools-Reference.txt." >> ~/UB-730-Tools/README.txt
echo "" >> ~/UB-730-Tools/README.txt
echo "With that said, if you want to set it up on your own or have a better way of doing it, then feel free to change what you want." >> ~/UB-730-Tools/README.txt  
echo "" >> ~/UB-730-Tools/README.txt
echo "Malcolm Hayward (malcolm.hayward@ubalt.edu)" >> ~/UB-730-Tools/README.txt


# Instructions for troubleshooting wine
touch ~/UB-730-Tools/READforWineIssues.txt
echo "On my systems, Wine would not work unless wine-mono was installed." >> ~/UB-730-Tools/READforWineIssues.txt
echo "" >> ~/UB-730-Tools/READforWineIssues.txt
echo "Make sure that your Wine version is 5.0." >> ~/UB-730-Tools/READforWineIssues.txt
echo "	Commands to check Wine version: wine --version OR wine64 --version." >> ~/UB-730-Tools/READforWineIssues.txt
echo "" >> ~/UB-730-Tools/READforWineIssues.txt
echo "I will assume that your version is 5.0. I already downloaded Wine Mono for you. You just have to do three things." >> ~/UB-730-Tools/READforWineIssues.txt
echo "" >> ~/UB-730-Tools/READforWineIssues.txt
echo "1. Run this command: wine64 uninstaller" >> ~/UB-730-Tools/READforWineIssues.txt
echo "2. You will see a menu. There is an install button. Click that." >> ~/UB-730-Tools/READforWineIssues.txt
echo "3. A file explorer will appear. The mono file is in your Downloads directory (/home/<user>/Downloads). Install it." >> ~/UB-730-Tools/READforWineIssues.txt
echo "" >> ~/UB-730-Tools/READforWineIssues.txt
echo "Both wine and wine64 should work after that. You do not have to type in wine <command> when you run JLECmd. I made an alias so that you only need to type in JLECmd.exe to run it." >> ~/UB-730-Tools/READforWineIssues.txt
echo "That is only for JLECmd though. If there are any other Windows programs you want to run, you WILL have to use wine <command>, because I did not set an alias for any other .exe except for JLEC." >> ~/UB-730-Tools/READforWineIssues.txt
echo "If there are any questions or problems, send me an email (malcolm.hayward@ubalt.edu) and/or invite me to a Zoom meeting, and I'll help." >> ~/UB-730-Tools/READforWineIssues.txt 


# Finish message
echo "Done! Please restart the terminal for some settings to take effect."