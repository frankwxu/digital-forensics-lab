@ECHO OFF 
:: This batch file details Windows 10, hardware, and networking configuration.
TITLE System Info
ECHO Please wait... Checking system information.
:: Section 1: Windows 10 information
ECHO ==========================
ECHO WINDOWS INFO
ECHO ============================
systeminfo | find "OS Name"
systeminfo | find "OS Version"
systeminfo | find "System Type"
:: Section 2: Hardware information.
ECHO ============================
ECHO HARDWARE INFO
ECHO ============================
systeminfo | find "Total Physical Memory"
wmic cpu get name
wmic diskdrive get name,model,size
:: Section 3: Networking information.
ECHO ============================
ECHO NETWORK INFO
ECHO ============================
ipconfig | findstr IPv4
START https://support.microsoft.com/en-us/windows/windows-10-system-requirements-6d4e9a79-66bf-7950-467c-795cf0386715
PAUSE