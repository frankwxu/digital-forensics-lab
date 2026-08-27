# Digital Forensics Lab & Shared Cyber Forensic Intelligence Repository

<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/BJA_Logo.png" width="150"> <img src="https://www.nist.gov/sites/default/files/images/2017/06/16/dsh-st.jpg" width="150"><img src="https://www.nsf.gov/news/mmg/media/images/bitmaplogo_nolayers_f_e50fcd0b-607b-4271-a808-914d9c2f65dc.png" width="110">

### Repository Features

- **Interactive Digital Forensics Labs:** Designed to engage students and faculty
- **Linux-Centric Lab Environment:** Uses Kali Linux exclusively in all labs
- **Visual Learning Support:** Each lab includes PowerPoint presentations, associated files, and instructional screenshots
- **Holistic Coverage:** Encompasses a wide array of topics within the field of digital forensics
- **Open-Source Tools:** All tools used are free and open source
- **Ongoing Updates:** Supported by grants from the DOJ, DHS, and NSF, the team is committed to regularly updating the repository
- **Forensic Intelligence Integration:** Two structured forensic intelligence datasets in JSON format derived from real case studies

_To provide feedback or tell us how you use the course materials, please email wxu at ubalt dot edu. Your collaboration is sincerely valued._

---

## ![NEW](https://img.shields.io/badge/NEW-red) Digital Forensics Basics: Second Edition and Companion Materials

[<img src="https://m.media-amazon.com/images/I/71a9y0+-ctL._SL1500_.jpg" width="150" alt="Digital Forensics Basics: A Step-by-Step Guide for Beginners book cover">](https://www.amazon.com/Digital-Forensics-Basics-Step-Step-ebook/dp/B0FKZMJLV7)

The **649-page second edition** of [*Digital Forensics Basics: A Step-by-Step Guide for Beginners*](https://www.amazon.com/Digital-Forensics-Basics-Step-Step-ebook/dp/B0FKZMJLV7) is organized around selected instructional content from this GitHub repository. Rather than reproducing the repository as-is, the book reorganizes, expands, and refines that material into its own cohesive, chapter-by-chapter learning path. It offers enhanced content, clearer explanations, stronger connections between concepts and investigative workflows, and more carefully sequenced hands-on activities. These improvements create a smoother reading experience and make the material easier to follow for beginners, independent learners, and instructors building a course.

The book is supported by a dedicated [companion materials repository](https://github.com/frankwxu/Digital-Forensics-Basic-Book) that extends the reading experience beyond the text. It includes:

- **Chapter-aligned PowerPoint presentations** for reviewing key concepts, diagrams, terminology, and lab workflows
- **Downloadable lab and evidence files** organized by chapter for convenient hands-on practice
- **Expanded evidence-search materials**, including separate presentations on pattern matching, file metadata, and advanced search techniques
- **A supplemental Windows command-line tutorial** for readers who want additional foundational practice
- **Study and lab guidance** covering evidence notes, reproducibility, authorization, privacy, and the safe handling of forensic media
- **Curated tool references** for Autopsy, The Sleuth Kit, Wireshark, 7-Zip, and other utilities used throughout the exercises

Together, the book and its supplemental materials provide a more complete learning path: read the explanation, review the chapter presentation, download the corresponding practice files, and reinforce each concept through guided investigation.

Faculty members are eligible for a complimentary desk copy. To request the PDF, please contact me from your institutional email address and include a link to your faculty profile or university webpage.

---

## Repository Materials: Table of Contents

The list below serves as the table of contents for this **digital-forensics-lab repository**, not for the book. It indexes the labs, presentations, case studies, datasets, and other instructional resources available here. *(Latest noted repository addition: Eufy investigations, October 15, 2024.)*

- Basic Computer Skills for Digital Forensics
  - [Number Systems](/Basic_Computer_Skills_for_Forensics/0_Number_Systems.pptx) (Python data-conversion code added in January 2023)
  - [PC Introduction](/Basic_Computer_Skills_for_Forensics/1_PC_Introduction.pptx)
  - [Windows Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/2_Win_command_line_tutorial.pptx)
  - [Linux Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/3_Linux_command_line_tutorial.pptx)
  - [Advanced Linux Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/4_Advanced_linux_command_line.pptx)

- Computer and Digital Forensics (updated in October 2021)
  - [Introduction to Digital Forensics](/Basic_Computer_Skills_for_Forensics/5_Introduction_to_digital_forensics.pptx)
  - [Sleuth Kit Tutorial](/Basic_Computer_Skills_for_Forensics/6_Sleuth_Kit_Tutorial.pptx)
  - [USB Image Acquisition](/Basic_Computer_Skills_for_Forensics/7_USB_Image_Acquisition.pptx)
  - [Evidence Search - A Pattern Match Game](/Basic_Computer_Skills_for_Forensics/8_1_Evidence_search_a_pattern_match_game.pptx) (updated in May 2022)
  - [Evidence Search - File Metadata](/Basic_Computer_Skills_for_Forensics/8_2_Evidence_search_file_metadata.pptx)
  - [Data Carving](/Basic_Computer_Skills_for_Forensics/9_Data_Carving.pptx)
  - [Steganography](/Basic_Computer_Skills_for_Forensics/10_Steganography.pptx)
  - [Forensic Report Template](/Basic_Computer_Skills_for_Forensics/Forensic_Report_Template.pdf)

- Basic Networking Skills for Digital Forensics (added on March 17, 2023; uses the Python Scapy and NetfilterQueue libraries)
  - [HTTP Analysis Using Wireshark (Text)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_1_text.pptx)
  - [HTTP Analysis Using Wireshark (Image)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_2_image.pptx)
  - [SYN Flood Attack Investigation Using TShark](Networking_Forensics/20_HTTP_tshark_Forensics_1_SYN_Flood.pptx)
  - [SMTP Forensics](Networking_Forensics/30_SMTP_Email_Forensics.pptx)
  - [ARP Poisoning Forensics](Networking_Forensics/40_ARP_Poisoning_Forensics.pptx)
  - [Firewall](Networking_Forensics/50_Firewall_Drop.pptx)
  - [DNS Introduction](Networking_Forensics/70_DNS.pptx)
  - [DNS Spoofing Forensics](Networking_Forensics/80_DNS_Spoof_Forensics.pptx)
  - [WEP40 Wireless Aircrack](Networking_Forensics/90_Wireless_aircrack_WEP40_1.pptx)

- Computer Forensics Case Studies
  - [Investigating NIST Data Leakage (Windows XP)](#investigating-nist-data-leakage)
  - [Investigating P2P Data Leakage (Windows 10)](#investigating-p2p-data-leakage)
  - [Investigating Illegal Possession of Images ("Networking forensics")](#investigating-illegal-possession-of-images)
  - [Investigating Email Harassment](#investigating-email-harassment) (updated in February 2023)
  - [Investigating an Illegal File Transfer (Memory Forensics)](#investigating-an-illegal-file-transfer)
  - [Investigating a Hacking Case](#investigating-a-hacking-case)
  - [Investigating the Morris Worm Attack](#investigating-the-morris-worm-attack) (updated in January 2023; [poster](/papers/poster_Morris_Worm_Attack.pdf))
- Mobile/IoT Forensics Case Studies
  - [Investigating Eufy Doorbell](#investigating-eufy-doorbell) (added on October 15, 2024)
  - [Investigating Echo Show 8](#investigating-echo-show-8) (added on December 25, 2023)
  - [Investigating Android 10](#investigating-android-10) (added on October 24, 2021)
  - [Investigating iPhone iOS 13](#investigating-iphone-ios-1341) (updated on June 18, 2022)
  - [Investigating a DJI Drone](#investigating-a-dji-drone) (added on December 7, 2021)
- Forensic Intelligence Repository
  - [Email Forensics](/STIX_for_digital_forensics/Email_Harassment)
  - [Illegal Possession of Images](/STIX_for_digital_forensics/Illegal_Possession_Images)
- AI for Forensics
  - [CIKM 2024 tutorial session](https://cikm2024.org/tutorials/) with an accompanying [hands-on lab](AI4Forensics/CKIM2024/readme.md)
  - [Identifying IP Addresses Using a Fine-Tuned AI Model](/AI4Forensics/IP_Identifier_Fine_Tuning/IP_Identifer_Fine_Tuning.pptx)
  - [Profiling Suspects Using LLMs (Browser History)](/AI4Forensics/CKIM2024/Takeout/browser_analysis.ipynb) ([Colab version](/AI4Forensics/CKIM2024/Takeout/profile_browser_history_colab.ipynb))
  - [Political Insight Analysis Leveraging LLMs (Email)](#political-insight-analysis-leveraging-llms)
- [Investigating Group Crimes Using Cellebrite's 2022 Capture-the-Flag (CTF) Competition Dataset](https://github.com/frankwxu/digital-forensics-lab-p2). Faculty members may request PDF lab instructions.
  - Beth's iPhone
  - Heisenberg's Android phone
  - Marsha's iPhone

---

Please cite our [paper](/papers/compsac2022.pdf):

W. Xu, L. Deng, and D. Xu, "Towards Designing Shared Digital Forensics Instructional Materials," in <em>Proceedings of the 46th Annual International Computer Software and Applications Conference (COMPSAC 2022),</em> pp. 117-122, July 2022. ([Video Presentation](https://youtu.be/ypKuTauuQdk))

Alternatively, use the following BibTeX entry:

```bibtex
@inproceedings{xu2022forensics,
  title={Towards Designing Shared Digital Forensics Instructional Materials},
  author={Xu, Weifeng and Deng, Lin, and Xu, Dianxiang},
  booktitle={46th Annual International Computer Software and Applications Conference (COMPSAC 2022)},
  volume={1},
  pages={117--122},
  year={2022},
  organization={IEEE}
}
```

---

## Tool Installation

### Method 1: Importing a Customized Kali VM Image

The customized VM combines [Kali Linux 2021.4](http://old.kali.org/kali-images/kali-2021.4/) with the [tools](#tools) required to complete most of the labs listed above, except for the P2P data leakage case.

- Install [VirtualBox](https://www.virtualbox.org/).
- Import the customized [Kali Linux 2021.4 VM](https://www.dropbox.com/s/y7svxg2pyy94ab5/Kali-Linux-2020.4-vbox-amd64_tools.ova). The default virtual disk size is 80 GB.

### Method 2: Installing Tools Using the Customized Script

The script has been tested only on Kali Linux 2021.4. It installs the tools required to complete most of the labs listed above, except for the P2P data leakage case, which uses a separate script described in the presentations. Please let us know if you would like us to add more tools to the script.

- Install [VirtualBox](https://www.virtualbox.org/).

- Install [Kali Linux 2021.4](http://old.kali.org/kali-images/kali-2021.4/). We recommend configuring the VM with an 80 GB virtual disk because each data-leakage case image may exceed 30 GB.

- Follow the [tool-installation instructions](https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/Tool_installation.pptx), or run the commands below:

```
wget  https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/tool-install-zsh.sh
chmod +x tool-install-zsh.sh
./tool-install-zsh.sh
```

- Review the installed [tools](#tools). Most tool commands can be run globally, allowing you to skip many of the installation steps in the presentations.

### Method 3: Using a Docker Container Based on Ubuntu 22.04 LTS

- This method was added in September 2023 and may require additional testing. Please report any issues.
- The Docker host runs Ubuntu 22.04 LTS.
- The container is built on top of Ubuntu 22.04 LTS as well.
- All tools are preinstalled in the Ubuntu container.
- Follow the tutorial [Docker for Digital Forensic Investigation](https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/Docker_4_Digital_Forensics.pptx).

---

### Investigating NIST Data Leakage

This [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) examines a forensic image involving intellectual property theft. It includes:

- A large and complex case created by NIST. The NIST website provides the [scenario and DD/EnCase images](https://cfreds-archive.nist.gov/data_leakage_case/data-leakage-case.html), as well as the [solutions](https://cfreds-archive.nist.gov/data_leakage_case/leakage-answers.pdf).
- 14 hands-on digital forensics labs

**Topics Covered**

| Labs   | Topics Covered (Command Line)                                                                                                | Python Version                                                                           |
| ------ | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Lab 0  | [Environment Setup](NIST_Data_Leakage_Case/NIST_Data_Leakage_00_Env_Setting.pptx)                                            |                                                                                          |
| Lab 1  | [Windows Registry](NIST_Data_Leakage_Case/NIST_Data_Leakage_01_Registry.pptx)                                                |                                                                                          |
| Lab 2  | [Windows Event and XML](NIST_Data_Leakage_Case/NIST_Data_Leakage_02._WinEvt_XML.pptx)                                        | [Python version](NIST_Data_Leakage_Case/NIST_Data_Leakage_02._WinEvt_XML_Python.pptx)    |
| Lab 3  | [Web History and SQL](NIST_Data_Leakage_Case/NIST_Data_Leakage_03_WebHistory_SQL.pptx)                                       | [Python version](NIST_Data_Leakage_Case/NIST_Data_Leakage_03_WebHistory_SQL_Python.pptx) |
| Lab 4  | [Email Investigation](NIST_Data_Leakage_Case/NIST_Data_Leakage_04_Email_USB.pptx)                                            | [Python version](NIST_Data_Leakage_Case/NIST_Data_Leakage_04_Email_USB_Python.pptx)      |
| Lab 5  | [File Change History and USN Journal](NIST_Data_Leakage_Case/NIST_Data_Leakage_05_USNJournaling.pptx)                        |                                                                                          |
| Lab 6  | [Network Evidence, Shellbags, and Jump Lists](NIST_Data_Leakage_Case/NIST_Data_Leakage_06_Network_Shellbag_Jumplist.pptx)     |                                                                                          |
| Lab 7  | [Network Drive and Cloud](NIST_Data_Leakage_Case/NIST_Data_Leakage_07_NetworkDrive_Cloud.pptx)                               |                                                                                          |
| Lab 8  | [Master File Table ($MFT) and Log File ($LogFile) Analysis](NIST_Data_Leakage_Case/NIST_Data_Leakage_08_CD_%24MFT.pptx)       |                                                                                          |
| Lab 9  | [Windows Search History](NIST_Data_Leakage_Case/NIST_Data_Leakage_08_CD_%24MFT.pptx)                                         |                                                                                          |
| Lab 10 | [Windows Volume Shadow Copy Analysis and SQL Database Carving](NIST_Data_Leakage_Case/NIST_Data_Leakage_10_Vol_Shadow_Copy.pptx) |                                                                                       |
| Lab 11 | [Recycle Bin and Anti-Forensics](NIST_Data_Leakage_Case/NIST_Data_Leakage_11_RecycleBin_AntiForensics.pptx)                  |                                                                                          |
| Lab 12 | [Data Carving](NIST_Data_Leakage_Case/NIST_Data_Leakage_12_CD-R_Data_Carving.pptx)                                           |                                                                                          |
| Lab 13 | [Cracking Windows Passwords](NIST_Data_Leakage_Case/NIST_Data_Leakage_13_Crack_Win10_Login_Password.pptx)                    |                                                                                          |

---

### Investigating P2P Data Leakage

The [P2P data leakage case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) helps students apply forensic techniques to an investigation of intellectual property theft involving peer-to-peer software. The study includes:

- A large and complex case involving a uTorrent client. The case is similar to the NIST data leakage lab but provides a clearer, more detailed timeline.
- Well-documented evidence and explanations connecting each activity to the timeline.
- 10 hands-on digital forensics labs

**Topics Covered**

| Labs   | Topics Covered                                                                                        | Size of PPTs |
| ------ | ----------------------------------------------------------------------------------------------------- | ------------ |
| Lab 0  | [Lab Environment Setup](P2P_Leakage/Presentation/ID00_Lab_Setup.pptx)                               | 4M           |
| Lab 1  | [Disk Image and Partitions](P2P_Leakage/Presentation/ID01_Disk_Image_and_Partitions.pptx)             | 5M           |
| Lab 2  | [Windows Registry and File Directory](P2P_Leakage/Presentation/ID02_Registry_and_File_Directory.pptx) | 15M          |
| Lab 3  | [MFT Timeline](P2P_Leakage/Presentation/ID03_MFT_Timeline.pptx)                                       | 6M           |
| Lab 4  | [USN Journal Timeline](P2P_Leakage/Presentation/ID03_MFT_Timeline.pptx)                               | 3M           |
| Lab 5  | [uTorrent Log File](P2P_Leakage/Presentation/ID05_uTorrent_Log_File.pptx)                             | 9M           |
| Lab 6  | [File Signature](P2P_Leakage/Presentation/ID06_File_Signature.pptx)                                   | 8M           |
| Lab 7  | [Emails](P2P_Leakage/Presentation/ID07_Emails.pptx)                                                   | 9M           |
| Lab 8  | [Web History](P2P_Leakage/Presentation/ID08_Web_History.pptx)                                         | 11M          |
| Lab 9  | [Website Analysis](P2P_Leakage/Presentation/ID09_Website_Analysis.pptx)                               | 2M           |
| Lab 10 | [Timeline (Summary)](P2P_Leakage/Presentation/Questions.docx)                                         | 13K          |

---

### Investigating Illegal Possession of Images

This [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_Possession_Images) investigates the illegal possession of rhino images. The forensic image was contributed by Dr. Golden G. Richard III and was originally used in the DFRWS 2005 Rodeo Challenge. NIST hosts the [USB DD image](https://cfreds-archive.nist.gov/dfrws/Rhino_Hunt.html), and a copy is also available in this repository.

**Topics Covered**

| Labs  | Topics Covered                                                                                                                                | Size of PPTs |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Lab 1 | [Reviewing HTTP Analysis Using Wireshark (Text)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_1_text.pptx)                               | 3M           |
| Lab 2 | [Rhino Possession Investigation 1: File Recovery](Illegal_Possession_Images/Rhion_Possession_1_File_Recovering.pptx)                            | 9M           |
| Lab 3 | [Rhino Possession Investigation 2: Steganography](Illegal_Possession_Images/Rhion_Possession_2_Steganography.pptx)                              | 4M           |
| Lab 4 | [Rhino Possession Investigation 3: Extracting Evidence from FTP Traffic](Illegal_Possession_Images/Rhion_Possession_3_FTP_Traffic_crackzip.pptx) | 3M           |
| Lab 5 | [Rhino Possession Investigation 4: Extracting Evidence from HTTP Traffic](Illegal_Possession_Images/Rhion_Possession_4_HTTP_Traffic.pptx)      | 5M           |

---

### Investigating Email Harassment

This [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Email_Harassment) investigates a harassing email sent by a student to a faculty member. The case is hosted by Digital Corpora, where you can access the [scenario description](https://digitalcorpora.org/corpora/scenarios/nitroba-university-harassment-scenario) and [network traffic](http://downloads.digitalcorpora.org/corpora/scenarios/2008-nitroba/nitroba.pcap). This repository provides only the lab instructions.

**Topics Covered**

| Labs  | Topics Covered                                                                                                   | Size of PPTs |
| ----- | ---------------------------------------------------------------------------------------------------------------- | ------------ |
| Lab 0 | [Investigating a Harassing Email Using Wireshark](Email_Harassment/0_Investigate_Harassment_Email_Wireshark.pptx) | 3M           |
| Lab 1 | [Introduction to TShark Forensics](Email_Harassment/1_tshark_forensics_Introduction.pptx)                         | 7M           |
| Lab 2 | [Investigating a Harassing Email Using TShark](2_Investigate_Harassment_Email_TShark.pptx)                       | 2M           |

---

### Investigating an Illegal File Transfer

This [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_File_Transferring_Memory_Forensics) examines computer memory to reconstruct a timeline of unauthorized data transfers. The scenario involves the illicit transfer of sensitive files from a server to a USB device.

**Topics Covered**

| Labs   | Topics Covered                                                 | Size of PPTs |
| ------ | -------------------------------------------------------------- | ------------ |
| Lab 0  | [Memory Forensics](Illegal_File_Transferring_Memory_Forensics) | 11M          |
| Part 1 | Understanding the Suspect and Accounts                          |              |
| Part 2 | Understanding the Suspect's PC                                  |              |
| Part 3 | Network Forensics                                               |              |
| Part 4 | Investigating Command History                                   |              |
| Part 5 | Investigating the Suspect's USB Device                          |              |
| Part 6 | Investigating Internet Explorer History                         |              |
| Part 7 | Investigating File Explorer History                             |              |
| Part 8 | Timeline Analysis                                               |              |

---

### Investigating a Hacking Case

This [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Hacking_Case), which includes a disk image provided by [NIST](https://cfreds-archive.nist.gov/Hacking_Case.html), investigates a hacker who intercepts internet traffic within range of wireless access points.

**Topics Covered**

| Labs  | Topics Covered                                            | Size of PPTs |
| ----- | --------------------------------------------------------- | ------------ |
| Lab 0 | [Hacking Case](/NIST_Hacking_Case/NIST_Hacking_Case.pptx) | 8M           |

---

### Investigating the Morris Worm Attack

This case study investigates the [Morris worm attack](https://seedsecuritylabs.org/Labs_20.04/Networking/Morris_Worm/) using a VM provided by [SEED Labs](https://seedsecuritylabs.org/labsetup.html). The goal is to identify all evidence related to the attack.

**Topics Covered**

| Labs  | Topics Covered                                                         | Size of PPTs |
| ----- | ---------------------------------------------------------------------- | ------------ |
| Lab 0 | [Morris Worm Attack](/Morris_Worm/Morris_Attack.pptx)                  | 7M           |
| Lab 1 | [Investigating Morris Worm Attack](/Morris_Worm/Morris_Forensics.pptx) | 2M           |

---

### Investigating Eufy Doorbell

This case study examines a Eufy doorbell and HomeBase system using advanced forensic extraction techniques, including the chip-off method. The process begins with disassembly and chip removal, continues through image acquisition, and concludes with analysis. Key directories containing camera footage, SQLite databases, and various logs are analyzed to extract evidence. This approach helps reconstruct timelines, identify user interactions and system activity, and provide valuable insights for security investigations. This study focuses on HomeBase 2, although HomeBase 3 is now available.

**eMMC Image**

- [Doorbell eMMC Image](https://drive.google.com/file/d/1H2pHr2IsgaJrRvuJSIa5Cujz5orWR4dy/view?usp=sharing)

**Topics Covered**

| Labs  | Topics Covered                                                                                        |
| ----- | ----------------------------------------------------------------------------------------------------- |
| Lab 0 | [Doorbell Introduction](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx)                        |
| Lab 1 | [Doorbell Scenario Simulation](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx)                 |
| Lab 2 | [Doorbell Teardown and Chip-Off Image Acquisition](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx) |
| Lab 3 | [Doorbell Image Analysis and Mounting](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx)         |
| Lab 4 | [Doorbell Evidence Extraction](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx)                 |
| Lab 5 | [Doorbell P2P Communication Log](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx)               |
| Lab 6 | [Doorbell Daily (Sec) Log](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptxx)                   |
| Lab 7 | [Analyzing the Doorbell Camera Directory](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx)      |
| Lab 8 | [Analyzing the Doorbell SQLite Directory](/Eufy_Doorbell/PPTs/0_Eufy_Doorbell_Introduction.pptx)      |

---

### Investigating Echo Show 8

This case study demonstrates the use of the chip-off technique to extract evidence from a second-generation Amazon Echo Show 8. Several types of evidence are generated and placed on the device. The investigation uses reverse-engineering techniques to recover that evidence from the Echo Show's embedded MultiMediaCard (eMMC).

**eMMC Images**

- [Echo Show eMMC Image](https://miya.teracloud.jp/share/11d1e631cf6f8456)
- [Echo Show Userdata Partition Image](https://miya.teracloud.jp/share/11d15342aae11912)

**Topics Covered**

| Labs      | Topics Covered                                                                                                     | Lab Data                                |
| --------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Lab 0     | [Echo Show Introduction](/Echo_Device/ppts/0_Echo_Show_Introduction.pptx)                                          |                                         |
| Lab 1     | [Echo Show Evidence Planting](/Echo_Device/ppts/1_Echo_Show_Evidence_Planting.pptx)                                |                                         |
| Lab 2     | [Device Teardown and eMMC Chip-off](/Echo_Device/ppts/2_Device_Teardown_and_eMMC_Chip-off.pptx)                    |                                         |
| Lab 3     | [Image Acquisition and Mounting](/Echo_Device/ppts/3_Image_Acquisition_and_Mounting.pptx)                          |                                         |
| Lab 4.1.1 | [Specifications: Device and OS Information](/Echo_Device/ppts/4_1_1_Specifications%20_Device_and_OS_Info.pptx)     | [Link](/Echo_Device/lab_data/Lab_4_1_1) |
| Lab 4.1.2 | [Specifications: User Information](/Echo_Device/ppts/4_1_2_Specifications%20User_info.pptx)                       | [Link](/Echo_Device/lab_data/Lab_4_1_2) |
| Lab 4.1.3 | [Specifications: Network Connectivity Information](/Echo_Device/ppts/4_1_3_Specifications_Network_Connectivity_Info.pptx) | [Link](/Echo_Device/lab_data/Lab_4_1_3) |
| Lab 4.2.1 | [Web Activity](/Echo_Device/ppts/4_2_1_Web_Activity.pptx)                                                          | [Link](/Echo_Device/lab_data/Lab_4_2_1) |
| Lab 4.2.2 | [Phone Communication](/Echo_Device/ppts/4_2_2_Phone_Communication.pptx)                                            | [Link](/Echo_Device/lab_data/Lab_4_2_2) |
| Lab 4.3.1 | [Multimedia: Photos and Related Data](/Echo_Device/ppts/4_3_1_Multimedia_Photos_and_Related_Data.pptx)             | [Link](/Echo_Device/lab_data/Lab_4_3_1) |
| Lab 4.3.2 | [Multimedia: Videos and Related Data](/Echo_Device/ppts/4_3_2_Multimedia_Videos_and_Related_Data.pptx)             | [Link](/Echo_Device/lab_data/Lab_4_3_3) |
| Lab 4.3.3 | [Multimedia: Audio and Related Data](/Echo_Device/ppts/4_3_3_Multimedia_Audio_and_Related_Data.pptx)               | [Link](/Echo_Device/lab_data/Lab_4_3_3) |

---

### Investigating Android 10

The image was created by Joshua Hickman and is hosted by [Digital Corpora](https://digitalcorpora.org/corpora/cell-phones/android-10).

| Labs      | Topics Covered                                                                                         | Size of PPTs |
| --------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| Lab 0     | [Introduction to the Pixel 3](Android10/0_Intro_Pixel3_Android10.pptx)                                 | 3M           |
| Lab 1     | [Pixel 3 Image](Android10/1_Pixel3_Image.pptx)                                                         | 2M           |
| Lab 2     | [Pixel 3 Device](Android10/2_Pixel3_Device_Investigation.pptx)                                         | 4M           |
| Lab 3     | [Pixel 3 System Settings](Android10/3_Pixel3_System_settings.pptx)                                     | 5M           |
| Lab 4     | [Overview: App Lifecycle](Android10/4_Overivew_App_Life_Cycle.pptx)                                     | 11M          |
| Lab 5.1.1 | [AOSP App Investigations: Messaging](Android10/5_1_1_AOSP_App_Investigations_Messaging.pptx)           | 4M           |
| Lab 5.1.2 | [AOSP App Investigations: Contacts](Android10/5_1_2_AOSP_App_Investigations_Contacts.pptx)             | 3M           |
| Lab 5.1.3 | [AOSP App Investigations: Calendar](Android10/5_2_1_GMS_App_Investigations_Messaging.pptx)             | 1M           |
| Lab 5.2.1 | [GMS App Investigations: Messaging](Android10/5_2_2_GMS_App_Investigations_Dialer.pptx)                | 6M           |
| Lab 5.2.2 | [GMS App Investigations: Dialer](Android10/5_2_2_GMS_App_Investigations_Dialer.pptx)                   | 2M           |
| Lab 5.2.3 | [GMS App Investigations: Maps](Android10/5_2_3_GMS_App_Investigations_Maps.pptx)                       | 8M           |
| Lab 5.2.4 | [GMS App Investigations: Photos](Android10/5_2_4_GMS_App_Investigations_Photos.pptx)                   | 6M           |
| Lab 5.3.1 | [Third-Party App Investigations: Kik](Android10/5_3_1_Third_Party_App_Investigation_kik.pptx)          | 4M           |
| Lab 5.3.2 | [Third-Party App Investigations: TextNow](5_3_2_Third_Party_App_Investigation%20_textnow.pptx)         | 1M           |
| Lab 5.3.3 | [Third-Party App Investigations: WhatsApp](Android10/5_3_3_Third_Party_App_Investigation_whatsapp.pptx) | 3M          |
| Lab 6     | [Pixel 3 Rooting](Android10/6_Pixel3_rooting.pptx)                                                     | 5M           |

---

### Investigating iPhone iOS 13.4.1

The image was created by Joshua Hickman and is hosted by [Digital Corpora](https://digitalcorpora.org/corpora/cell-phones/ios-13).

| Labs   | Topics Covered                                                        | Size of PPTs |
| ------ | --------------------------------------------------------------------- | ------------ |
| Lab 0  | [Introduction to iPhone iOS 13](iOS/0_Intro_iPhone_iOS13.pptx)         | 5M           |
| Lab 1  | [iOS 13.4.1 Image](iOS/1_iOS_13.4.1_Image.pptx)                       | 5M           |
| Lab 2  | [iPhone Device Investigation](iOS/2_iPhone_Device_Investigation.pptx) | 3M           |
| Lab 3  | [iOS System Settings](iOS/3_iOS_System_settings.pptx)                 | 3M           |
| Lab 4  | [Overview of the App Lifecycle](iOS/4_Overivew_App_Life_Cycle.pptx)    | 2M           |
| Lab 5  | [Messages Investigation](iOS/5_Messages_Investigations.pptx)          | 3M           |
| Lab 6  | [Contacts Investigation](iOS/6_Contacts_Investigation.pptx)           | 3M           |
| Lab 7  | [Calendar Investigation](iOS/7_Calender_Investigation.pptx)           | 2M           |
| Lab 8  | [Safari Investigation](iOS/8_Safari_Investigation.pptx)               | 3M           |
| Lab 9  | [Photo Investigation](iOS/9_Photos_Investigation.pptx)                | 7M           |
| Lab 10 | [KnowledgeC Investigation](iOS/10_KnowledgeC_Investigation.pptx)      | 5M           |
| Lab 11 | [Health Investigation](iOS/11_Health_Investigation.pptx)              | 5M           |
| Lab 12 | [Location Investigation](iOS/12_iOS_Location_Investigation.pptx)      | 8M           |
| Lab 13 | [Cellebrite Investigation](iOS/13_Cellebrite_Investigation.pptx)      | 12M          |
| Lab 14 | [Magnet AXIOM Investigation](iOS/14_Magnet_Axiom_Investigation.pptx)  | 13M          |
| Lab 15 | [Jailbreak Investigation](iOS/15_iOS_Jailbreak.pptx)                  | 6M           |

---

### Investigating a DJI Drone

The dataset includes logical files extracted from a DJI controller (mobile device) and an image of the SD card used by the device. The drone dataset was created by [VTO Labs](https://www.vtolabs.com/drone-forensics). The lab covers GPS analysis and cached-image retrieval. This lab is a draft and will be improved in a future update.

| Labs  | Topics Covered                                                                                  | Size of PPTs |
| ----- | ----------------------------------------------------------------------------------------------- | ------------ |
| Lab 0 | [DJI Mavic Air Mobile](Drone_DJI_Mavic_Air/00_DJI_Mavic_Air_Mobile.pptx)                        | 13M          |
| Lab 1 | [DJI Mavic Air MicroSD Raw](Drone_DJI_Mavic_Air/01_DJI_Mavic_Air_microSD_raw.pptx)              | 2M           |
| Lab 2 | [DJI Mavic Air MicroSD EnCase Format](Drone_DJI_Mavic_Air/02_DJI_Mavic_Air_microSD_encase.pptx) | 2M           |

---

### Political Insight Analysis Leveraging LLMs

This case study demonstrates how to leverage large language models to derive political insights from an email dataset. It uses a set of leaked [emails](https://github.com/benhamner/hillary-clinton-emails?tab=readme-ov-file) obtained from Hillary Clinton's private email server.

The leaked emails represent a significant chapter in recent U.S. political history and raise questions about transparency, security, and the handling of sensitive information. During her tenure as U.S. Secretary of State from 2009 to 2013, Hillary Clinton used a private email server for official communications instead of the State Department's email system. She stated that she did so for convenience, allowing her to use a single device for both personal and official emails.

The dataset from Hillary Clinton's private email server is a comprehensive collection of communications covering her tenure as Secretary of State from 2009 to 2013. It includes approximately 30,000 emails on topics ranging from official diplomatic communications to personal correspondence. The release and subsequent analysis of these emails have played a significant role in political debates, legal inquiries, and public discussions about transparency and security in government communications.

Our dataset is [a set of email summaries](/AI4Forensics/CKIM2024/HillaryEmails/results_email_summary.txt). Each summary was generated by Gemini from an original message in the leaked [email dataset](https://github.com/benhamner/hillary-clinton-emails?tab=readme-ov-file). This case study focuses only on emails containing the keyword `Israel`.

Our results and code are available in a [Jupyter Notebook](/AI4Forensics/CKIM2024/HillaryEmails/email_analysis_political_insight.ipynb).

The following image presents political insights derived from summaries of emails related to Israel: <img src="/AI4Forensics/CKIM2024/HillaryEmails/political_insight_2024-05-31_10-29-52.jpg">

---

[Dark-Moon](https://github.com/ASCIT31/Dark-Moon): open source (GPL-3.0) autonomous AI penetration testing platform (web, API, Active Directory, Kubernetes), self hosted with proof of exploitation, a complementary offensive tool for students practising on authorized labs.
### Tools

| Name                    | Command           | Repository                                                      | Installation Method |
| ----------------------- | ----------------- | --------------------------------------------------------------- | ------------------- |
| Wine                    | wine --version    | https://source.winehq.org/git/wine.git/                         | Custom              |
| Vinetto                 | vinetto -h        | https://github.com/AtesComp/Vinetto                             | Custom              |
| imgclip                 | imgclip -h        | https://github.com/Arthelon/imgclip                             | apt install         |
| RegRipper               | rip.pl -h         | https://github.com/keydet89/RegRipper3.0                        | Customized script   |
| Windows-Prefetch-Parser | prefetch.py -h    | https://github.com/PoorBillionaire/Windows-Prefetch-Parser.git  | Custom              |
| python-evtx             | evtx_dump.py -h   | https://github.com/williballenthin/python-evtx                  | apt install         |
| libesedb-utils          | esedbexport -h    | https://github.com/libyal/libesedb                              | apt install         |
| libpff                  | pffexport -h      | https://github.com/libyal/libpff                                | apt install         |
| USN-Record-Carver       | usncarve.py -h    | https://github.com/PoorBillionaire/USN-Record-Carver            | apt install         |
| USN-Journal-Parser      | usn.py -h         | https://github.com/PoorBillionaire/USN-Journal-Parser           | apt install         |
| time_decode             | time_decode.py -h | https://github.com/digitalsleuth/time_decode                    | Git clone           |
| analyzeMFT              | analyzeMFT.py -h  | https://github.com/dkovar/analyzeMFT                            | Customized script   |
| libvshadow              | vshadowinfo -h    | https://github.com/libyal/libvshadow                            | Customized script   |
| INDXParse               | INDXParse.py -    |                                                                 | Customized script   |
| Carving SQLite database files      | undark -h         | https://github.com/inflex/undark.git                            | Customized script   |
| stegdetect              | stegdetect -V     |                                                                 | Customized script   |
| stegbreak               | stegbreak -V      |                                                                 | Customized script   |
| stego-toolkit           | jphide            |                                                                 | Customized script   |
| jpsestego-toolkitek     | jpseek            |                                                                 | Customized script   |
| volatility-2            | vol.py -h         | https://github.com/volatilityfoundation/volatility.git          | Customized script   |
| liblnk-utils            | lnkinfo -h        |                                                                 | apt install         |
| JLECmd                  |                   | https://f001.backblazeb2.com/file/EricZimmermanTools/JLECmd.zip | Git clone           |
| recentfilecache-parser  |                   | https://github.com/prolsen/recentfilecache-parser               |                     |
| LogFileParser           |                   | https://github.com/jschicht/LogFileParser.git                   | Git clone           |
| UsnJrnl2Csv             |                   | ttps://github.com/jschicht/UsnJrnl2Csv.git                      | Git clone           |

- Other tools installed using `apt install`:
  python3-pip, leafpad, terminator, sqlite3, tree, xmlstarlet, libhivex-bin, pasco, libhivex-bin, npm, binwalk, foremost, hashdeep, ewf-tools, nautilus

---

## Contributors

- Principal investigators
  - Dr. Frank Xu (Email: fxu at ubalt dot edu)
  - Dr. Debra L. Stanley
  - Dr. Lin Deng; Towson University
  - Dr. Wenbin Zhang; Florida International University

- Students:
  - Eric Xu: University of Maryland (LLM for Digital Forensics)
  - Jeel Khatiwala (Evaluating the Reliability of Digital Forensic Evidence Discovered by LLMs)
  - Mohit Dhabuwala (Open-source mobile forensics handbook)
  - Daniel Addai ([CTF](https://github.com/frankwxu/digital-forensics-lab-p2))
  - Sarfraz Shaikh (Echo Show, Eufy Doorbell)
  - Danny Ferreira (iPhone)
  - Harleen Kaur (Partial Android contribution)
  - Malcolm Hayward (P2P Leakage)
  - Richard (Max) Wheeless (Hacking case)
  - Chimezie Onwuegbuchulem (Docker for Digital Forensics)
  - Etinosa Osawe (AI for Forensics—identifying IP addresses with a fine-tuned language model)

---

## Star History

<a href="https://www.star-history.com/?repos=frankwxu%2Fdigital-forensics-lab&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=frankwxu/digital-forensics-lab&type=date&theme=dark&legend=top-left&sealed_token=QLG2IoC6rGLOmppzMTNZ6GUua_bQOcXoSDc94I_z0Tql-_Y5LoI_iYQ6VKqdFbNJecrH_ZgiM0pKnUuCZ9QpDTibmDIIuwEaMBMC1TKV4Zk4TpUl4nOrJCQyBtaxArRRs4uOHhtpylhwoxbbpscj__P_VvC7HHMwS-mEfDOZG4MTUIQlX7jtD4BidhAu" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=frankwxu/digital-forensics-lab&type=date&legend=top-left&sealed_token=QLG2IoC6rGLOmppzMTNZ6GUua_bQOcXoSDc94I_z0Tql-_Y5LoI_iYQ6VKqdFbNJecrH_ZgiM0pKnUuCZ9QpDTibmDIIuwEaMBMC1TKV4Zk4TpUl4nOrJCQyBtaxArRRs4uOHhtpylhwoxbbpscj__P_VvC7HHMwS-mEfDOZG4MTUIQlX7jtD4BidhAu" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=frankwxu/digital-forensics-lab&type=date&legend=top-left&sealed_token=QLG2IoC6rGLOmppzMTNZ6GUua_bQOcXoSDc94I_z0Tql-_Y5LoI_iYQ6VKqdFbNJecrH_ZgiM0pKnUuCZ9QpDTibmDIIuwEaMBMC1TKV4Zk4TpUl4nOrJCQyBtaxArRRs4uOHhtpylhwoxbbpscj__P_VvC7HHMwS-mEfDOZG4MTUIQlX7jtD4BidhAu" />
 </picture>
</a>
