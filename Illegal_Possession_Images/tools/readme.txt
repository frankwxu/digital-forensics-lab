stegdetect_src.7z is a fixed version source code
changes:
file/file.c: change char *prognamex;	 to char *progname_fix;	


stegdetect.7z is compiled version



#install stegdetect 
sudo apt install -y dh-autoreconf
[ -d "tools/stegdetect/" ] && sudo rm -rf tools/stegdetect 
sudo git clone https://github.com/poizan42/stegdetect tools/stegdetect
change the file.c
cd tools/stegdetect/ 
sudo autoreconf -f -i
sudo ./configure 
sudo make