# Digital Forensics Lab

<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/BJA_Logo.png" width="150">

### Features of hands-on labs

===================

- Hands-on Digital Forensics Labs: designed for Students and Faculty
- Linux-based lab: All labs are purely based on [Kali Linux](https://www.kali.org/downloads/)
- Lab screenshots: Each lab has a PPT with lab screenshots
- Comprehensive: Cover many topics in digital forensics
- Free: All tools are open source
- Updated: The project is funded by DOJ and will keep updating

---

## Table of Contents (updating)

- Case Study
  - [Investigating P2P Data Leakage](#Investigating-P2P-Data-Leakage) (added on June 2021)
  - [Investigating NIST Data Leakage](#Investigating-NIST-Data-Leakage)
  - [Investigating Illegal Possession of Images](#Investigating-Illegal-Possession-of-Images)
  - [Investigating Email Harassment](#Investigating-Email-Harassment)
  - [Investigating Illegal File Transferring (Memory Forensics)](#Investigating-illegal-File-Transferring "Memory Forensics")
  - [Investigating Hacking Case](#Investigating-Hacking-Case)
- Tool Installation
  - [Tools Used](#Tools-Used)
  - [Installation PPTs](https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/Kali_Installation_2020.pptx)
  - Installation Scripts (see commands as follows)

```
# The following commands will install all tools needed for Data Leakage Case. We will upgrade the script to add more tools for other labs soon.

wget  https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/tool-install-zsh.sh
chmod +x tool-install-zsh.sh
./tool-install-zsh.sh
```

---

### Investigating P2P Data Leakage

==============

The [P2P data leakage case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) is to help students to apply various forensic techniques to investigate intellectual property theft involving P2P, such uTorrent client. The study include

- A large and complex case study is similar to NIST data leakage lab, but it provides a clearer and more detailed timeline. Solid evidence is explained for each activity performed by a suspect. We suggest to use this before study NIST data leakage case study.
- 13 hands-on labs/topics in digital forensics

**Topics Covered**

| Labs   | Topics Covered                      | Size of PPTs |
| ------ | ----------------------------------- | ------------ |
| Lab 0  | Lab Environment Setting Up          | 4M           |
| Lab 1  | Disk Image and Partitions           | 5M           |
| Lab 2  | Windows Registry and File Directory | 15M          |
| Lab 3  | MFT Timeline                        | 6M           |
| Lab 4  | USN Journal Timeline                | 3M           |
| Lab 5  | uTorrent Log File                   | 9M           |
| Lab 6  | File Signature                      | 8M           |
| Lab 7  | Emails                              | 9M           |
| Lab 8  | Web History                         | 11M          |
| Lab 9  | Website Analysis                    | 2M           |
| Lab 10 | Timeline (Summary)                  | 13K          |

---

### Investigating NIST Data Leakage

==============

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) is to investigate an image involving intellectual property theft. The study include

- A large and complex case study created by NIST. You can access the [Senario, DD/Encase images](https://www.cfreds.nist.gov/data_leakage_case/data-leakage-case.html). You can also find the [solutions](https://www.cfreds.nist.gov/data_leakage_case/leakage-answers.pdf) on their website.
- 13 hands-on labs/topics in digital forensics

**Topics Covered**

| Labs   | Topics Covered                      | Size of PPTs |
| ------ | ----------------------------------- | ------------ |
| Lab 0  | Environment Setting Up              | 2M           |
| Lab 1  | Windows Registry                    | 3M           |
| Lab 2  | Windows Event and XML               | 3M           |
| Lab 3  | Web History and SQL                 | 3M           |
| Lab 4  | Email Investigation                 | 3M           |
| Lab 5  | File Change History and USN Journal | 2M           |
| Lab 6  | Network Evidence and shellbag       | 2M           |
| Lab 7  | Network Drive and Windows shellbag  | 5M           |
| Lab 8  | Master File Table ($MFT) Analysis   | 4M           |
| Lab 9  | Windows Search History              | 4M           |
| Lab 10 | Windows Volume Shadow Copy Analysis | 6M           |
| Lab 11 | Data Carving                        | 3M           |
| Lab 12 | Crack Windows Passwords             | 2M           |

---

### Investigating Illegal Possession of Images

=====================

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_Possession_Images) is to investigate the illegal possession of Rhino images. This image was contributed by Dr. Golden G. Richard III, and was originally used in the DFRWS 2005 RODEO CHALLENGE. NIST hosts the [USB DD image](https://www.cfreds.nist.gov/dfrws/Rhino_Hunt.html). A copy of the image is also available in the repository.

**Topics Covered**

| Labs  | Topics Covered                                                       | Size of PPTs |
| ----- | -------------------------------------------------------------------- | ------------ |
| Lab 0 | HTTP Analysis using Wireshark (text)                                 | 3M           |
| Lab 1 | HTTP Analysis using Wireshark (image)                                | 6M           |
| Lab 2 | The Sleuth Kid Tutorial                                              | 1M           |
| Lab 3 | Rhion Possession Investigation 1: File recovering                    | 9M           |
| Lab 4 | Rhion Possession Investigation 2: Steganography                      | 4M           |
| Lab 5 | Rhion Possession Investigation 3: Extract Evidence from FTP Traffic  | 3M           |
| Lab 6 | Rhion Possession Investigation 4: Extract Evidence from HTTP Traffic | 5M           |

### Investigating Email Harassment

=========

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Email_Harassment) is to investigate the harassment email sent by a student to a faculty member. The case is hosted by digitalcorpora.org. You can access the [senario description](https://digitalcorpora.org/corpora/scenarios/nitroba-university-harassment-scenario) and [network traffic](http://downloads.digitalcorpora.org/corpora/scenarios/2008-nitroba/nitroba.pcap) from their website. The repository only provides lab instructions.

**Topics Covered**

| Labs  | Topics Covered                                 | Size of PPTs |
| ----- | ---------------------------------------------- | ------------ |
| Lab 0 | Investigating Harassment Email using Wireshark | 3M           |
| Lab 1 | t-shark Forensic Introduction                  | 2M           |
| Lab 2 | Investigating Harassment Email using t-shark   | 2M           |

### Investigating Illegal File Transferring

=========

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_File_Transferring_Memory_Forensics) is to investigate computer memory for reconstructing a timeline of illegal data transferring. The case includes a scenario of transfer sensitive files from a server to a USB.

**Topics Covered**

| Labs   | Topics Covered                        | Size of PPTs |
| ------ | ------------------------------------- | ------------ |
| Lab 0  | Memory Forensics                      | 11M          |
| part 1 | Understand the Suspect and Accounts   |              |
| part 2 | Understand the Suspect’s PC           |              |
| part 3 | Network Forensics                     |              |
| part 4 | Investigate Command History           |              |
| part 5 | Investigate Suspect’s USB             |              |
| part 6 | Investigate Internet Explorer History |              |
| part 7 | Investigate File Explorer History     |              |
| part 8 | Timeline Analysis                     |              |

### Investigating Hacking Case

=========

The case study, including a disk image provided by [NIST](https://www.cfreds.nist.gov/Hacking_Case.html) is to investigate a hacker who intercepts internet traffic within range of Wireless Access Points. Note that the PPT is encrypted with a password as one of the major assignments. Email fxu at ubalt dot edu to ask the password if you are a faculty member.

**Topics Covered**

| Labs  | Topics Covered   | Size of PPTs |
| ----- | ---------------- | ------------ |
| Lab 0 | Memory Forensics | 8M           |

### Tools Used

========

| Name                    | version    | vendor                                                          |
| ----------------------- | ---------- | --------------------------------------------------------------- |
| Wine                    | 6.0        | https://source.winehq.org/git/wine.git/                         |
| Vinetto                 | 0.98       | https://github.com/AtesComp/Vinetto                             |
| imgclip                 | 05.12.2017 | https://github.com/Arthelon/imgclip                             |
| Tree                    | 06.01.2020 | https://github.com/kddeisz/tree                                 |
| RegRipper               | 3.0        | https://github.com/keydet89/RegRipper3.0                        |
| Windows-Prefetch-Parser | 05.01.2016 | https://github.com/PoorBillionaire/Windows-Prefetch-Parser.git  |
| python-evtx             | 05.21.2020 | https://github.com/williballenthin/python-evtx                  |
| xmlstarlet              | 1.6.1      | https://github.com/fishjam/xmlstarlet                           |
| hivex                   | 09.15.2020 | https://github.com/libguestfs/hivex                             |
| libesedb                | 01.01.2021 | https://github.com/libyal/libesedb                              |
| pasco-project           | 02.09.2017 | https://annsli.github.io/pasco-project/                         |
| libpff                  | 01.17.2021 | https://github.com/libyal/libpff                                |
| USN-Record-Carver       | 05.21.2017 | https://github.com/PoorBillionaire/USN-Record-Carver            |
| USN-Journal-Parser      | 1212.2018  | https://github.com/PoorBillionaire/USN-Journal-Parser           |
| JLECmd                  | 1.4.0.0    | https://f001.backblazeb2.com/file/EricZimmermanTools/JLECmd.zip |
| libnl-utils             | 3.2.27     | https://packages.ubuntu.com/xenial/libs/libnl-utils             |
| time_decode             | 12.13.2020 | https://github.com/digitalsleuth/time_decode                    |
| analyzeMFT              | 2.0.4      | https://github.com/dkovar/analyzeMFT                            |
| libvshadow              | 12.20.2020 | https://github.com/libyal/libvshadow                            |
| recentfilecache-parser  | 02.13.2018 | https://github.com/prolsen/recentfilecache-parser               |

## Contribution

=============

- Frank Xu
- Malcolm Hayward
- Richard (Max) Wheeless
