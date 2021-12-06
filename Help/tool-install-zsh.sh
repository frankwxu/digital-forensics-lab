#! /bin/bash

cd ~
[ ! -d "lab" ] && mkdir lab || cd lab

##############################################
# Tool Installation Report Summary 
##############################################
[ -f ~/installation-report.txt ] && sudo rm ~/installation-report.txt
touch ~/installation-report.txt
echo  -e "\e[1;32m " >> ~/installation-report.txt
echo  -e "\e[1;32m " >> ~/installation-report.txt
echo  -e "\e[1;32m*******************************" >> ~/installation-report.txt
echo  -e "\e[1;32m*   University of Baltimore   *" >> ~/installation-report.txt
echo  -e "\e[1;32m*    Frank Xu wxu@ubalt.edu   *" >> ~/installation-report.txt
echo  -e "\e[1;32m*******************************" >> ~/installation-report.txt

message(){
  (eval "$2")  | grep -iq "$3" &> /dev/null
  if [ $? == 1 ]; then 
    echo  -e "\e[1;31mTool $1: \"$2\" installation Failed!" >> ~/installation-report.txt
  else
    echo  -e "\e[1;32mTool $1: \"$2\" installation successed!" >> ~/installation-report.txt
  fi
}

#############################################
# Lab tools: NIST Data Leakage
##############################################
#install wine
#https://linuxhint.com/install_wine_-ubuntu_20-24/ 
sudo apt -y update
sudo apt -y upgrade
# install both boot
sudo dpkg --add-architecture i386 
sudo apt -y update 
sudo apt -y install wine64 wine32
tool_name="wine"
command_string="wine --version"
sudo apt -y install $tool_name
key_str="wine-"
message $tool_name "$command_string" "$key_str"


#install other packages
sudo apt -y install python3-pip
sudo apt -y install leafpad
sudo apt -y install terminator
sudo apt -y install sqlite3
sudo apt -y install tree
sudo apt -y install xmlstarlet
sudo apt -y install libhivex-bin
sudo apt -y install pasco

sudo apt -y install npm
sudo apt -y install binwalk
sudo apt -y install foremost
sudo apt -y install hashdeep 
sudo apt -y install ewf-tools 
sudo apt -y install nautilus

#Install pff-tools
tool_name="pff-tools"
command_string="pffexport -h"
sudo apt -y install $tool_name
key_str="usage"
message $tool_name "$command_string" "$key_str"

#Install libesedb-utils
tool_name="libesedb-utils"
command_string="esedbexport -h"
sudo apt -y install $tool_name
key_str="usage"
message $tool_name "$command_string" "$key_str"

#Install liblnk-utils
tool_name="liblnk-utils"
command_string="lnkinfo -h"
sudo apt -y install $tool_name
key_str="usage"
message $tool_name "$command_string" "$key_str"


#Install usncarve
tool_name="usncarve"
command_string="usncarve.py -h"
sudo pip install $tool_name
key_str="usage"
message $tool_name "$command_string" "$key_str"

#Install usnparser
tool_name="usnparser"
command_string="usn.py -h"
sudo pip install $tool_name
key_str="usage"
message $tool_name "$command_string" "$key_str"

# install RegRipper
cd ~/lab
tool_name="RegRipper30"
command_string="rip.pl -h"
key_str="RegRipper tool"
[ -d "tools/RegRipper30/" ] && sudo rm -rf tools/RegRipper30 
sudo mkdir tools/RegRipper30
sudo wget -q https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/scripts/RegRipper30-apt-git-Install.sh -P tools/RegRipper30/
sudo chmod 755 tools/RegRipper30/RegRipper30-apt-git-Install.sh
sudo tools/RegRipper30/RegRipper30-apt-git-Install.sh
message $tool_name "$command_string" "$key_str"

#Install Vinetto for Thumbcache
cd ~/lab
tool_name="Vinetto"
command_string="vinetto -h"
key_str="usage"
[ -d "tools/Vinetto/" ] && sudo rm -rf tools/Vinetto 
sudo git clone https://github.com/AtesComp/Vinetto.git tools/Vinetto
cd tools/Vinetto
sudo pip install .	
message $tool_name "$command_string" "$key_str"

#Install time_decode
cd ~/lab
tool_name="time_decode"
command_string="time_decode.py -h"
key_str="usage"
[ -d "tools/time_decode/" ] && sudo rm -rf tools/time_decode 
sudo git clone https://github.com/digitalsleuth/time_decode.git tools/time_decode
sudo mv tools/time_decode/time_decode/time_decode.py /usr/local/bin/. 
message $tool_name "$command_string" "$key_str"

#Install windowsprefetch
cd ~/lab
tool_name="windowsprefetch"
command_string="prefetch.py -h"
key_str="usage"
sudo pip install $tool_name
sudo cp /home/kali/.local/bin/prefetch.py /usr/local/bin/. 
message $tool_name "$command_string" "$key_str"

#Install evtx_dump
cd ~/lab
tool_name="python3-evtx"
command_string="evtx_dump.py -h"
sudo apt -y install $tool_name
key_str="usage"
message $tool_name "$command_string" "$key_str"

#Install INDXParse
cd ~/lab
tool_name="INDXParse"
command_string="INDXParse.py -h"
key_str="usage"
[ -d "tools/INDXParse/" ] && sudo rm -rf tools/INDXParse 
sudo wget https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/NIST_Data_Leakage_Case/tools/INDXParse.7z -P tools
sudo 7z x tools/INDXParse.7z -aoa -otools
sudo sh -c 'chmod +x tools/INDXParse/*.py' 
sudo sh -c 'mv tools/INDXParse/*.py /usr/local/bin/.' 
message $tool_name "$command_string" "$key_str"

#Install 
cd ~/lab
tool_name="analyzeMFT"
command_string="analyzeMFT.py -h"
key_str="usage"
[ -d "tools/analyzeMFT/" ] && sudo rm -rf tools/analyzeMFT
sudo git clone https://github.com/dkovar/analyzeMFT.git  tools/analyzeMFT
cd tools/analyzeMFT
alias python=/usr/bin/python2
sudo python setup.py install
unalias python
message $tool_name "$command_string" "$key_str"

#Install imgclip
cd ~/lab
tool_name="imgclip"
command_string="imgclip -h"
sudo npm install -g $tool_name
key_str="usage"
message $tool_name "$command_string" "$key_str"

#Install libvshadow-alpha-20210425
#https://github.com/libyal/libvshadow/wiki/Building
cd ~/lab
tool_name="libvshadow-alpha-20210425"
command_string="vshadowinfo -h"
key_str="usage"
sudo apt install -y libfuse-dev
sudo apt install -y git autoconf automake autopoint libtool pkg-config
[ -d "tools/libvshadow-20210425" ] && sudo rm -ft tools/libvshadow-20210425 
sudo wget -q wget https://github.com/libyal/libvshadow/releases/download/20210425/libvshadow-alpha-20210425.tar.gz -P tools
cd tools
sudo tar -xf libvshadow-alpha-20210425.tar.gz
[ -f "libvshadow-alpha-20210425.tar.gz" ] && sudo rm libvshadow-alpha-20210425.tar.gz 
cd libvshadow-20210425
./configure
sudo make
sudo make install
sudo ./configure --prefix=/usr
sudo ldconfig
message $tool_name "$command_string" "$key_str"

#Install undark for carving sqlite .db 
cd ~/lab
tool_name="undark"
command_string="undark -h"
key_str="SQLite3"
[ -d "tools/undark/" ] && sudo rm -rf tools/undark 
sudo git clone https://github.com/inflex/undark.git tools/undark
cd tools/undark
sudo make
sudo mv undark /usr/local/bin/. 
message $tool_name "$command_string" "$key_str"
cd ~/lab

#Install LogFileParser
cd ~/lab
[ -d "LogFileParser/" ] && sudo rm -rf LogFileParser 
sudo git clone https://github.com/jschicht/LogFileParser.git

#Install UsnJrnl2Csv
cd ~/lab
[ -d "UsnJrnl2Csv/" ] && sudo rm -rf UsnJrnl2Csv 
sudo git clone https://github.com/jschicht/UsnJrnl2Csv.git

#Install JLECmd
cd ~/lab
[ -f "JLECmd.exe" ] && sudo rm JLECmd.exe
wget -q https://f001.backblazeb2.com/file/EricZimmermanTools/JLECmd.zip
unzip JLECmd.zip 
sudo rm JLECmd.zip


#############################################
# Lab Tools: Illegal Possession Images
#############################################
#install stegdetect 
cd ~/lab
tool_name="stegdetect"
command_string="stegdetect -V"
key_str="Stegdetect Version"
[ -d "tools/stegdetect/" ] && sudo rm -rf tools/stegdetect 
sudo wget https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Illegal_Possession_Images/tools/stegdetect.7z -P tools
sudo 7z x tools/stegdetect.7z -aoa -otools
[ -f "tools/stegdetect.7z" ] && sudo rm -rf tools/stegdetect.7z 
sudo cp tools/stegdetect/stegdetect /usr/bin/.
message $tool_name "$command_string" "$key_str"

sudo cp tools/stegdetect/stegbreak /usr/bin/.
tool_name="stegbreak"
command_string="stegbreak -V"
key_str="stegbreak Version"
message $tool_name "$command_string" "$key_str"

#install stego-toolkit 
cd ~/lab
tool_name="stego-toolkit "
command_string="jphide"
key_str="jphide"
[ -d "tools/stego-toolkit/" ] && sudo rm -rf tools/stego-toolkit
sudo git clone https://github.com/DominicBreuker/stego-toolkit.git tools/stego-toolkit
cd tools/stego-toolkit/install
sudo chmod +x jphide.sh
sudo ./jphide.sh
message $tool_name "$command_string" "$key_str"
command_string="jpseek"
key_str="jpseek"
message $tool_name "$command_string" "$key_str"

#############################################
# Lab Tools: Memory Forensics
# https://seanthegeek.net/1172/how-to-install-volatility-2-and-volatility-3-on-debian-ubuntu-or-kali-linux/
#############################################
cd ~/lab
sudo apt install -y build-essential git libdistorm3-dev yara libraw1394-11 libcapstone-dev capstone-tool tzdata

sudo apt install -y python2 python2.7-dev libpython2-dev
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
sudo python2 -m pip install -U setuptools wheel

python2 -m pip install -U distorm3 yara pycrypto pillow openpyxl ujson pytz ipython capstone
sudo python2 -m pip install yara
sudo ln -s /usr/local/lib/python2.7/dist-packages/usr/lib/libyara.so /usr/lib/libyara.so
python2 -m pip install -U git+https://github.com/volatilityfoundation/volatility.git
echo 'export PATH=/home/kali/.local/bin:$PATH' >> ~/.zshrc

tool_name="volatility-2"
command_string="vol.py -h"
key_str="usage"
message $tool_name "$command_string" "$key_str"

# Delete all downloaded source code
[ -d "tools" ] && sudo rm -rf tools

# Show report
echo  -e "\e[1;31mNeed to reboot the VM to execute some commands, e.g., volatility2 \"vol.py -h\" with Kali account" >> ~/installation-report.txt

cat ~/installation-report.txt
