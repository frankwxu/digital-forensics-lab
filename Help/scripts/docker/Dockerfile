FROM ubuntu:22.04

LABEL author=Chimezie

# Forces the selection of US Eastern Standard time Zone. 
ENV TZ=US/Eastern \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install tzdata

# Update package list and install security updates
RUN apt-get update \
    && apt-get install -y apt-utils

RUN apt update \
    && apt upgrade -y \
    && apt autoremove -y \
    && apt-get update && apt-get install -y wget \
    && apt-get update && apt-get install sudo 
    
# Tools Directory
WORKDIR /tools/lab

# Install text editors
RUN sudo apt install -y nano \
    && apt install -y vim \
    && apt update && apt install -y gedit 
   
# Install Wine32 and Wine64
RUN sudo dpkg --add-architecture i386 \
    && dpkg --add-architecture amd64 \
    && apt-get update \
    && apt-get install -y --no-install-recommends wine32 \
    && apt-get install --no-install-recommends --assume-yes wine
ENV DISPLAY :0
    
# Install other packages
RUN sudo apt -y install python3-pip \
    && sudo apt -y install terminator \
    && apt -y install sqlite3 \
    && apt -y install tree \
    && apt -y install xmlstarlet \
    && apt -y install libhivex-bin \
    && apt -y install pasco \
    && apt -y install npm \
    && apt -y install binwalk \
    && apt -y install foremost \
    && apt -y install hashdeep \
    && apt -y install ewf-tools \
    && apt -y install nautilus

# Install pff-tools
RUN sudo apt-get update  \
    && sudo apt-get -y install pff-tools

# Install libesedb-utils
RUN sudo apt-get update \
    && sudo apt-get -y install libesedb-utils

# Install liblnk-utils
RUN sudo apt-get update 
RUN sudo apt-get install -y liblnk-utils || { echo 'Package installation failed'; exit 1; }

# Install usncarve
RUN sudo sudo apt-get update  \
    && pip install usncarve

# Install usnparser
RUN sudo apt-get update  \
    && pip install usnparser

# Install RegRipper
WORKDIR  /tools 

#Update the default repository first
RUN sudo apt-get update -y  \
    && apt-get install curl \
    && apt-get update && apt-get install -y git 
      
# Install necessary dependencies
RUN sudo apt-get update && apt-get install -y \
    dos2unix

# Clone the RegRipper repository
RUN git clone https://github.com/keydet89/RegRipper3.0.git /tools/RegRipper30

# Download the RegRipper installer script
RUN curl -sSL https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/scripts/RegRipper30-apt-git-Install.sh -o /tools/RegRipper30/RegRipper30-apt-git-Install.sh

# Convert the line endings to Unix format
RUN dos2unix /tools/RegRipper30/RegRipper30-apt-git-Install.sh

# Set the permissions for the installer script
RUN chmod +x /tools/RegRipper30/RegRipper30-apt-git-Install.sh

# Run the installer script
RUN /tools/RegRipper30/RegRipper30-apt-git-Install.sh

# Add RegRipper to the PATH
ENV PATH="/tools/RegRipper30:$PATH"


# Install Vinetto for Thumbcache
# Install Vinetto
RUN sudo apt-get update \
    && sudo apt-get -y install vinetto


# Install time_decode
# Set the working directory
WORKDIR /tools/lab

# Install colorama
RUN sudo pip install colorama

# Clone the time_decode repository
RUN git clone https://github.com/digitalsleuth/time_decode.git tools/time_decode

# Move the time_decode.py script to /usr/local/bin
RUN mv tools/time_decode/time_decode/time_decode.py /usr/local/bin/

# Set the working directory to the lab directory
WORKDIR /tools/lab

# Install INDXParse
# Set the working directory
WORKDIR /tools/INDXParse

# Download the INDXParse.py script
RUN sudo wget https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/NIST_Data_Leakage_Case/tools/INDXParse.7z -P tools
RUN sudo 7z x tools/INDXParse.7z -aoa -otools
RUN sudo sh -c 'chmod +x tools/INDXParse/*.py' 
RUN sudo sh -c 'mv tools/INDXParse/*.py /usr/local/bin/.'

# Clone the INDXParse repository
RUN sudo apt-get update \
    && git clone https://github.com/williballenthin/INDXParse.git

# Install the required Python packages
RUN sudo pip install construct

# Set the working directory
WORKDIR /tools

# Clone the analyzeMFT repository
RUN git clone https://github.com/dkovar/analyzeMFT.git analyzeMFT \
    && cd analyzeMFT \
    && apt-get update \
    && apt-get install -y python3 \
    && python3 setup.py install

# Install imgclip
# Set the working directory
WORKDIR /tools/lab

# Update and install imgclip dependencies
RUN sudo apt-get update \
    && apt-get install -y npm \
    && npm install -g imgclip


# Copy the necessary files to the container
# Set the working directory to the location of the index.js file
WORKDIR /usr/local/lib/node_modules/imgclip/node_modules/copy-paste

# Use the sed command to modify the file
RUN sed -i '58s/if(text?.pipe)/if(text \&\& pipe)/' /usr/local/lib/node_modules/imgclip/node_modules/copy-paste/index.js

# Continue with the rest of your Dockerfile


# Install libvshadow-alpha-20210425
# Update the package repository and install required dependencies
RUN sudo apt-get update \
    && apt-get install -y libfuse-dev git autoconf automake autopoint libtool pkg-config

# Download libvshadow

# Set the working directory
WORKDIR /tools

# Install required packages
RUN sudo apt-get update && apt-get install -y wget autoconf automake libtool

# Download libvshadow-alpha-20210425.tar.gz
RUN wget -q https://github.com/libyal/libvshadow/releases/download/20221030/libvshadow-alpha-20221030.tar.gz

# Extract the tar.gz file
RUN tar -xzf libvshadow-alpha-20221030.tar.gz

# Cleanup unnecessary files
RUN rm libvshadow-alpha-20221030.tar.gz

# Change directory to libvshadow-20210425
WORKDIR /tools/libvshadow-20221030

# Install dependencies
# RUN ./configure

# Generate the configure script and Configure, build, and install libvshadow
RUN ./configure && make && make install

# Configure library installation prefix
RUN ./configure --prefix=/usr

# Update library cache
RUN ldconfig

# Install Windows--PerserPrefetch and required packages
# Set the working directory
WORKDIR /tools

# Update package repository and install required packages
RUN sudo apt-get update && apt-get install -y python3-evtx 

# Update the package repository and install required dependencies
RUN sudo apt-get update \
    && apt-get install -y python3-pip

# Clone Windows-Prefetch Parser repository
RUN git clone https://github.com/williballenthin/python-evtx.git

# Change directory to python-evtx
WORKDIR /tools/python-evtx

# Install python-evtx library
RUN sudo python3 setup.py install

# Install windowsprefetch
RUN sudo pip install windowsprefetch

# Install undark for carving sqlite .db 
WORKDIR /tools
RUN sudo git clone https://github.com/inflex/undark.git ./undark
WORKDIR /tools/undark
RUN sudo make
RUN sudo mv undark /usr/local/bin/. 
WORKDIR /tools

# Install LogFileParser
# Set the working directory
WORKDIR /tools/lab

# Update the package repository and install git
RUN sudo apt-get update && apt-get install -y git

# Clone LogFileParser repository
RUN git clone https://github.com/jschicht/LogFileParser.git

# Install UsnJrnl2Csv
# Set the working directory
WORKDIR /tools/lab

# Update the package repository and install git
# RUN apt-get update && apt-get install -y git

# Clone UsnJrnl2Csv repository
RUN git clone https://github.com/jschicht/UsnJrnl2Csv.git


# Install JLECmd
# Set the working directory
WORKDIR /tools

# Update the package repository and install wget and unzip
RUN sudo apt-get update && apt-get install -y wget unzip

# Download JLECmd.zip
RUN wget -q https://f001.backblazeb2.com/file/EricZimmermanTools/JLECmd.zip

# Unzip JLECmd.zip
RUN unzip JLECmd.zip

# Remove the JLECmd.zip file
RUN rm JLECmd.zip


# Install volitility 2
# Update the system first
RUN apt-get update && apt-get full-upgrade -y

# Install dependencies for Volitility2
RUN sudo apt update \
    && sudo apt install -y software-properties-common \
    && sudo add-apt-repository ppa:deadsnakes/ppa \
    && sudo apt update \
    && sudo apt install -y python2.7

# Install pip for Python 2
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
RUN python2.7 get-pip.py

# Install Dependencies for pip modules
RUN sudo apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python2.7-dev


# Install pip modules which are needed to install some other packages
RUN sudo pip2 install --no-binary :all: pycrypto
RUN sudo pip2 install cryptography
RUN sudo pip2 install yara-python
RUN sudo pip2 install distorm3==3.4.4

# In case it was not properly installed previously, uninstall it first
RUN sudo pip uninstall pycryptodomex  

# Reinstall it again
RUN sudo pip install pycryptodomex


# Install additional tools and dependencies for Python2
RUN sudo apt-get install -y python2 python2-dev dwarfdump build-essential yara zip curl

# Download and set up the latest version of Volatility 2
RUN git clone https://github.com/volatilityfoundation/volatility.git
RUN cd volatility && python2 setup.py install

# Install volitility 3
# Update the system
RUN sudo apt-get update && apt-get full-upgrade -y

# Install system dependencies
RUN sudo apt-get install -y python3 python3-pip dwarfdump yara zip git

# Install Volatility 3 from GitHub
RUN git clone https://github.com/volatilityfoundation/volatility3.git /tools/volatility3

# Install Volatility 3 dependencies
RUN sudo pip3 install -r /tools/volatility3/requirements.txt

# Add Volatility 3 to the PATH
ENV PATH="/opt/volatility3:${PATH}"

# Install stego-toolkit
# Update the system
#RUN apt-get update && apt-get full-upgrade -y

# Install required dependencies for stego-toolkit
RUN sudo apt-get update && apt-get install -y steghide 

# Clone the stego-toolkit repository
RUN git clone https://github.com/DominicBreuker/stego-toolkit.git /tools/stego-toolkit

# Change directory to the stego-toolkit installation directory
WORKDIR /tools/stego-toolkit/install

# Make jphide.sh executable
RUN chmod +x /tools/stego-toolkit/install/jphide.sh

# Run jphide.sh installation script
RUN /tools/stego-toolkit/install/jphide.sh

# Install stegdetect
# Set the working directory
WORKDIR /tools

# Update the system and install necessary dependencies
RUN sudo apt-get update && apt-get install -y wget p7zip-full

# Download and extract stegdetect
RUN wget -q https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Illegal_Possession_Images/tools/stegdetect.7z -P tools \
    && 7z x tools/stegdetect.7z -aoa -otools \
    && rm -f tools/stegdetect.7z

# Copy stegdetect and stegbreak binaries to /usr/bin
RUN cp tools/stegdetect/stegdetect /usr/bin/. \
    && cp tools/stegdetect/stegbreak /usr/bin/.

WORKDIR /

# Verify installations
RUN wine --version
RUN imgclip -h 
RUN pffexport -h
RUN esedbexport -h
RUN lnkinfo -h
RUN usncarve.py -h
RUN usn.py -h
RUN rip.pl -h
RUN vinetto -h
RUN time_decode.py -h
RUN prefetch.py -h
RUN evtx_dump.py -h
RUN INDXParse.py -h
RUN analyzeMFT.py -h
RUN vshadowinfo -h
RUN undark -h
RUN true || jphide 
RUN true || jpseek 
RUN vol.py -h
RUN stegdetect -V  || true
RUN stegbreak  -V  || true

# Set the entry point or default command
CMD ["/bin/bash"] 

# End of the Dockerfile
