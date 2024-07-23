# Digital Forensics Lab & Shared Cyber Forensic Intelligence Repository

<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/BJA_Logo.png" width="150"> <img src="https://www.nist.gov/sites/default/files/images/2017/06/16/dsh-st.jpg" width="150"><img src="https://www.nsf.gov/news/mmg/media/images/bitmaplogo_nolayers_f_e50fcd0b-607b-4271-a808-914d9c2f65dc.png" width="110">

### Features of Repository

- **Interactive Digital Forensics Labs:** Tailored for students and faculty engagement
- **Linux-Centric Lab Environment:** Utilizes Kali Linux exclusively for all labs
- **Visual Learning Support:** Each lab includes PowerPoint presentations, associated files, and instructional screenshots
- **Holistic Coverage:** Encompasses a wide array of topics within the field of digital forensics
- **Open Source Tools:** All tools utilized are freely available and open source
- **Ongoing Updates:** Supported by grants from the DOJ, DHS, and NSF, the team is committed to regularly updating the repository
- **Forensic Intelligence Integration:** Two structured forensic intelligence datasets in JSON format derived from real case studies

_For feedback or to express your usage of the course materials, please reach out via email at wxu at ubalt dot edu. Your collaboration is sincerely valued_

---

Please cite our [paper](/papers/compsac2022.pdf):

W. Xu, L. Deng, and D. Xu, "Towards Designing Shared Digital Forensics Instructional Materials," in <em>Proceeding of the 46st Annual International Computer Software and Applications Conference (COMPSAC 2022),</em> pp. 117-122, July 2022. ([Video Presentation](https://youtu.be/ypKuTauuQdk))

or in BibTeX

@inproceedings{xu2022forensics, \
&emsp;title={Towards Designing Shared Digital Forensics Instructional Materials}, \
&emsp;author={Xu, Weifeng and Deng, Lin, and Xu, Dianxiang}, \
&emsp;booktitle={46st Annual International Computer Software and Applications Conference (COMPSAC 2022)},\
&emsp;volume={1},\
&emsp;pages={117--122},\
&emsp;year={2022},\
&emsp;organization={IEEE}\
}

---

## Table of Contents (Major Holidy release Dec 25, 2023: Echo Show investigations preview)

- Basic Computer Skills for Digital Forensics

  - [Number Systems](/Basic_Computer_Skills_for_Forensics/0_Number_Systems.pptx) (add Python code for data conversion 1/2023)
  - [PC Introduction](/Basic_Computer_Skills_for_Forensics/1_PC_Introduction.pptx)
  - [Windows Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/2_Win_command_line_tutorial.pptx)
  - [Linux Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/3_Linux_command_line_tutorial.pptx)
  - [Advanced Linux Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/4_Advanced_linux_command_line.pptx)

- Basic Networking Skills for Digital Forensics (added 3/17/2023. Use Paython Scapy and netfilterqueue libraries.)

  - [HTTP Analysis using Wireshark (text)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_1_text.pptx)
  - [HTTP Analysis using Wireshark (image)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_2_image.pptx)
  - [SYN Flood Attack Investigation using tshark](Networking_Forensics/20_HTTP_tshark_Forensics_1_SYN_Flood.pptx)
  - [SMTP Forensics](Networking_Forensics/30_SMTP_Email_Forensics.pptx)
  - [ARP Poisoning Forensics](Networking_Forensics/40_ARP_Poisoning_Forensics.pptx)
  - [Firewall](Networking_Forensics/50_Firewall_Drop.pptx)
  - [DNS Introduction](Networking_Forensics/70_DNS.pptx)
  - [DNS Spoofing Forensics](Networking_Forensics/80_DNS_Spoof_Forensics.pptx)
  - [WEP40 Wireless Aircrack](Networking_Forensics/90_Wireless_aircrack_WEP40_1.pptx)

- Computer and Digital Forensics (updated on Oct. 2021)
  - [Introduction to Digital Forensics](/Basic_Computer_Skills_for_Forensics/5_Introduction_to_digital_forensics.pptx)
  - [Sleuth Kit Tutorial](/Basic_Computer_Skills_for_Forensics/6_Sleuth_Kit_Tutorial.pptx)
  - [USB Image Acquisition](/Basic_Computer_Skills_for_Forensics/7_USB_Image_Acquisition.pptx)
  - [Evidence Search - A Pattern Match Game](/Basic_Computer_Skills_for_Forensics/8_1_Evidence_search_a_pattern_match_game.pptx) (updated on May 2022)
  - [Evidence Search - File Metadata](/Basic_Computer_Skills_for_Forensics/8_2_Evidence_search_file_metadata.pptx)
  - [Data Carving](/Basic_Computer_Skills_for_Forensics/9_Data_Carving.pptx)
  - [Steganography](/Basic_Computer_Skills_for_Forensics/10_Steganography.pptx)
  - [Forensic Report Template](/Basic_Computer_Skills_for_Forensics/Forensic_Report_Template.pdf)
- Computer Forensics Case Study
  - [Investigating NIST Data Leakage (Windows XP)](#investigating-nist-data-leakage)
  - [Investigating P2P Data Leakage (Windows 10)](#investigating-p2p-data-leakage)
  - [Investigating Illegal Possession of Images ("Networking forensics")](#investigating-illegal-possession-of-images)
  - [Investigating Email Harassment](#investigating-email-harassment) (updated on Feb 2023)
  - [Investigating Illegal File Transferring (Memory Forensics)](#investigating-illegal-file-transferring)
  - [Investigating Hacking Case](#investigating-hacking-case)
  - [Investigating Morris Worm Attack](#investigating-morris-worm-attack) (updated on Jan 2023, [POSTER](/papers/poster_Morris_Worm_Attack.pdf))
- Mobile/IoT Forensics Case Study
  - [Investigating Echo Show 8](#investigating-echo-show-8) (added on 12/25/2023)
  - [Investigating Android 10](#investigating-android-10) (added on 10/24/2021)
  - [Investigating iPhone iOS 13](#investigating-iphone-ios-13) (updated on 6/18/2022)
  - [Investigating Drone](#investigating-drone-dji) (add on 12/07/2021)
- Forensic Intelligence Repository
  - [Email forensics](/STIX_for_digital_forensics/Email_Harassment)
  - [Illegal Possession of Images](/STIX_for_digital_forensics/Illegal_Possession_Images)
- AI for Forensics
  - Tutorial session on [CKIM2024](https://cikm2024.org/tutorials/). You can access [hands-on lab](AI4Forensics/CKIM2024/readme.md)
  - [Identifying IP Addresses using a Fine-tuned AI Model](/AI4Forensics/IP_Identifier_Fine_Tuning/IP_Identifer_Fine_Tuning.pptx)
  - [Profiling Suspects Leveraging LLMs (Browser History)](/AI4Forensics/CKIM2024/Takeout/browser_analysis.ipynb) [colab](/AI4Forensics/CKIM2024/Takeout/profile_browser_history_colab.ipynb)
  - [Political Insight Analysis Leveraging LLMs (Email)](#political-insight-analysis-leveraging-llms)

## Tool Installation

### Method 1: Importing customized Kali VM image

The customized Kali VM = Kali ([2021.4](http://old.kali.org/kali-images/kali-2021.4/)) + [tools](#Tools) used for completing most of the labs listed above (except p2p Data Leakage case)

- Install [Virtualbox](https://www.virtualbox.org/)
- Import the customized [Kali 2021.4](https://www.dropbox.com/s/y7svxg2pyy94ab5/Kali-Linux-2020.4-vbox-amd64_tools.ova). Notes: the default harddisk size is 80G.

### Method 2: Installing tools using the customized script (the script ONLY is tested on Kali 2021.4)

The following script will install tools needed for completing most of the labs listed above (except p2p Data Leakage case, which has its own script described in PPTs). Please let us know if you need us to add more tools to the script.

- Install [Virtualbox](https://www.virtualbox.org/)

- Install [Kali 2021.4](http://old.kali.org/kali-images/kali-2021.4/). Notes: Suggest You configure the disk size of Kali VM 80G because the size of each leakage cases image is 30G+

- Run a tool installation script [instructions](https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/Tool_installation.pptx), or you can simply follow the commands below

```
wget  https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/tool-install-zsh.sh
chmod +x tool-install-zsh.sh
./tool-install-zsh.sh
```

- Installed [tools](#Tools). Note that most of the commands for tools can executed globally. Now you can skip most of tool installation steps in PPTs.

### Method 3: Using a Docker container based on Ubuntu 22.04 LTS (added in 09/23, may need more testing, report any issues please)

- The host machine of the Docker container is Ubuntu 22.04 LTS.
- The container is built on top of Ubuntu 22.04 LTS as well.
- All tools are pre-install on the Ubuntu container.
- You can follow the tuturial [Docker for Digital Forensic Investgiation](https://raw.githubusercontent.com/frankwxu/digital-forensics-lab/main/Help/Docker_4_Digital_Forensics.pptx)

---

### Investigating NIST Data Leakage

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) is to investigate an image involving intellectual property theft. The study include

- A large and complex case study created by NIST. You can access the [Scenario, DD/Encase images](https://cfreds-archive.nist.gov/data_leakage_case/data-leakage-case.html). You can also find the [solutions](https://cfreds-archive.nist.gov/data_leakage_case/leakage-answers.pdf) on their website.
- 14 hands-on labs/topics in digital forensics

**Topics Covered**

| Labs   | Topics Covered (Command Line)                                                                                                | Python Version                                                                           |
| ------ | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Lab 0  | [Environment Setting Up](NIST_Data_Leakage_Case/NIST_Data_Leakage_00_Env_Setting.pptx)                                       |                                                                                          |
| Lab 1  | [Windows Registry](NIST_Data_Leakage_Case/NIST_Data_Leakage_01_Registry.pptx)                                                |                                                                                          |
| Lab 2  | [Windows Event and XML](NIST_Data_Leakage_Case/NIST_Data_Leakage_02._WinEvt_XML.pptx)                                        | [Python version](NIST_Data_Leakage_Case/NIST_Data_Leakage_02._WinEvt_XML_Python.pptx)    |
| Lab 3  | [Web History and SQL](NIST_Data_Leakage_Case/NIST_Data_Leakage_03_WebHistory_SQL.pptx)                                       | [Python version](NIST_Data_Leakage_Case/NIST_Data_Leakage_03_WebHistory_SQL_Python.pptx) |
| Lab 4  | [Email Investigation](NIST_Data_Leakage_Case/NIST_Data_Leakage_04_Email_USB.pptx)                                            | [Python version](NIST_Data_Leakage_Case/NIST_Data_Leakage_04_Email_USB_Python.pptx)      |
| Lab 5  | [File Change History and USN Journal](NIST_Data_Leakage_Case/NIST_Data_Leakage_05_USNJournaling.pptx)                        |                                                                                          |
| Lab 6  | [Network Evidence and shellbag](NIST_Data_Leakage_Case/NIST_Data_Leakage_06_Network_Shellbag_Jumplist.pptx)                  |                                                                                          |
| Lab 7  | [Network Drive and Cloud](NIST_Data_Leakage_Case/NIST_Data_Leakage_07_NetworkDrive_Cloud.pptx)                               |                                                                                          |
| Lab 8  | [Master File Table ($MFT) and Log File  ($logFile) Analysis](NIST_Data_Leakage_Case/NIST_Data_Leakage_08_CD_%24MFT.pptx)     |                                                                                          |
| Lab 9  | [Windows Search History](NIST_Data_Leakage_Case/NIST_Data_Leakage_08_CD_%24MFT.pptx)                                         |                                                                                          |
| Lab 10 | [Windows Volume Shadow Copy Analysis/SQL database carving](NIST_Data_Leakage_Case/NIST_Data_Leakage_10_Vol_Shadow_Copy.pptx) |                                                                                          |
| Lab 11 | [Recycle Bin and Anti-Forensics](NIST_Data_Leakage_Case/NIST_Data_Leakage_11_RecycleBin_AntiForensics.pptx)                  |                                                                                          |
| Lab 12 | [Data Carving](NIST_Data_Leakage_Case/NIST_Data_Leakage_12_CD-R_Data_Carving.pptx)                                           |                                                                                          |
| Lab 13 | [Crack Windows Passwords](NIST_Data_Leakage_Case/NIST_Data_Leakage_13_Crack_Win10_Login_Password.pptx)                       |                                                                                          |

---

### Investigating P2P Data Leakage

The [P2P data leakage case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) is to help students to apply various forensic techniques to investigate intellectual property theft involving P2P. The study includes

- A large and complex case involving a uTorrent client. The case is similar to NIST data leakage lab. However, it provides a clearer and more detailed timeline.
- Solid evidence with explanations. Each evidence that is associated with each activity is explained along with the timeline.
- 10 hands-on labs/topics in digital forensics

**Topics Covered**

| Labs   | Topics Covered                                                                                        | Size of PPTs |
| ------ | ----------------------------------------------------------------------------------------------------- | ------------ |
| Lab 0  | [Lab Environment Setting Up](P2P_Leakage/Presentation/ID00_Lab_Setup.pptx)                            | 4M           |
| Lab 1  | [Disk Image and Partitions](P2P_Leakage/Presentation/ID01_Disk_Image_and_Partitions.pptx)             | 5M           |
| Lab 2  | [Windows Registry and File Directory](P2P_Leakage/Presentation/ID02_Registry_and_File_Directory.pptx) | 15M          |
| Lab 3  | [MFT Timeline ](P2P_Leakage/Presentation/ID03_MFT_Timeline.pptx)                                      | 6M           |
| Lab 4  | [USN Journal Timeline](P2P_Leakage/Presentation/ID03_MFT_Timeline.pptx)                               | 3M           |
| Lab 5  | [uTorrent Log File ](P2P_Leakage/Presentation/ID05_uTorrent_Log_File.pptx)                            | 9M           |
| Lab 6  | [File Signature ](P2P_Leakage/Presentation/ID06_File_Signature.pptx)                                  | 8M           |
| Lab 7  | [Emails ](P2P_Leakage/Presentation/ID07_Emails.pptx)                                                  | 9M           |
| Lab 8  | [Web History ](P2P_Leakage/Presentation/ID08_Web_History.pptx)                                        | 11M          |
| Lab 9  | [Website Analysis ](P2P_Leakage/Presentation/ID09_Website_Analysis.pptx)                              | 2M           |
| Lab 10 | [Timeline (Summary)](P2P_Leakage/Presentation/Questions.docx)                                         | 13K          |

---

### Investigating Illegal Possession of Images

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_Possession_Images) is to investigate the illegal possession of Rhino images. This image was contributed by Dr. Golden G. Richard III, and was originally used in the DFRWS 2005 RODEO CHALLENGE. NIST hosts the [USB DD image](https://cfreds-archive.nist.gov/dfrws/Rhino_Hunt.html). A copy of the image is also available in the repository.

**Topics Covered**

| Labs  | Topics Covered                                                                                                                                | Size of PPTs |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Lab 1 | [Review HTTP Analysis using Wireshark (text)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_1_text.pptx)                                 | 3M           |
| Lab 2 | [Rhion Possession Investigation 1: File recovering](Illegal_Possession_Images/Rhion_Possession_1_File_Recovering.pptx)                        | 9M           |
| Lab 3 | [Rhion Possession Investigation 2: Steganography](Illegal_Possession_Images/Rhion_Possession_2_Steganography.pptx)                            | 4M           |
| Lab 4 | [Rhion Possession Investigation 3: Extract Evidence from FTP Traffic](Illegal_Possession_Images/Rhion_Possession_3_FTP_Traffic_crackzip.pptx) | 3M           |
| Lab 5 | [Rhion Possession Investigation 4: Extract Evidence from HTTP Traffic](Illegal_Possession_Images/Rhion_Possession_4_HTTP_Traffic.pptx)        | 5M           |

---

### Investigating Email Harassment

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Email_Harassment) is to investigate the harassment email sent by a student to a faculty member. The case is hosted by digitalcorpora.org. You can access the [senario description](https://digitalcorpora.org/corpora/scenarios/nitroba-university-harassment-scenario) and [network traffic](http://downloads.digitalcorpora.org/corpora/scenarios/2008-nitroba/nitroba.pcap) from their website. The repository only provides lab instructions.

**Topics Covered**

| Labs  | Topics Covered                                                                                                   | Size of PPTs |
| ----- | ---------------------------------------------------------------------------------------------------------------- | ------------ |
| Lab 0 | [Investigating Harassment Email using Wireshark](Email_Harassment/0_Investigate_Harassment_Email_Wireshark.pptx) | 3M           |
| Lab 1 | [t-shark Forensic Introduction](Email_Harassment/1_tshark_forensics_Introduction.pptx)                           | 7M           |
| Lab 2 | [Investigating Harassment Email using t-shark](2_Investigate_Harassment_Email_TShark.pptx)                       | 2M           |

---

### Investigating Illegal File Transferring

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_File_Transferring_Memory_Forensics) aims to examine computer memory to reconstruct a timeline of unauthorized data transfers. The scenario involves the illicit transfer of sensitive files from a server to a USB device.

**Topics Covered**

| Labs   | Topics Covered                                                 | Size of PPTs |
| ------ | -------------------------------------------------------------- | ------------ |
| Lab 0  | [Memory Forensics](Illegal_File_Transferring_Memory_Forensics) | 11M          |
| part 1 | Understand the Suspect and Accounts                            |              |
| part 2 | Understand the Suspect’s PC                                    |              |
| part 3 | Network Forensics                                              |              |
| part 4 | Investigate Command History                                    |              |
| part 5 | Investigate Suspect’s USB                                      |              |
| part 6 | Investigate Internet Explorer History                          |              |
| part 7 | Investigate File Explorer History                              |              |
| part 8 | Timeline Analysis                                              |              |

---

### Investigating Hacking Case

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Hacking_Case), including a disk image provided by [NIST](https://cfreds-archive.nist.gov/Hacking_Case.html) is to investigate a hacker who intercepts internet traffic within range of Wireless Access Points.

**Topics Covered**

| Labs  | Topics Covered                                            | Size of PPTs |
| ----- | --------------------------------------------------------- | ------------ |
| Lab 0 | [Hacking Case](/NIST_Hacking_Case/NIST_Hacking_Case.pptx) | 8M           |

---

### Investigating Morris Worm Attack

The case study is an investigation of the [Morris Worm Attacking](https://seedsecuritylabs.org/Labs_20.04/Networking/Morris_Worm/). We are using the VM provided by [SeedLab](https://seedsecuritylabs.org/labsetup.html). The goal of the lab is to find all evidence related to Morris Worm attacking.

**Topics Covered**

| Labs  | Topics Covered                                                         | Size of PPTs |
| ----- | ---------------------------------------------------------------------- | ------------ |
| Lab 0 | [Morris Worm Attack](/Morris_Worm/Morris_Attack.pptx)                  | 7M           |
| Lab 1 | [Investigating Morris Worm Attack](/Morris_Worm/Morris_Forensics.pptx) | 2M           |

---

### Investigating Echo Show 8

The case study outlines the use of the chip-off technique to extract evidence from an Amazon Echo Show device. Different types of evidence are produced and inserted into the Echo Show 8 (2nd generation). The investigative process includes the utilization of a reverse engineering approach to retrieve the implanted evidence from the embedded MultiMediaCard (eMMC) of the Echo Show device.

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
| Lab 4.1.1 | [Specifications: Device and OS Info](/Echo_Device/ppts/4_1_1_Specifications%20_Device_and_OS_Info.pptx)            | [link](/Echo_Device/lab_data/Lab_4_1_1) |
| Lab 4.1.2 | [Specifications: User info](/Echo_Device/ppts/4_1_2_Specifications%20User_info.pptx)                               | [link](/Echo_Device/lab_data/Lab_4_1_2) |
| Lab 4.1.3 | [Specifications: Network Connectivity Info](/Echo_Device/ppts/4_1_3_Specifications_Network_Connectivity_Info.pptx) | [link](/Echo_Device/lab_data/Lab_4_1_3) |
| Lab 4.2.1 | [Web Activity](/Echo_Device/ppts/4_2_1_Web_Activity.pptx)                                                          | [link](/Echo_Device/lab_data/Lab_4_2_1) |
| Lab 4.2.2 | [Phone Communication](/Echo_Device/ppts/4_2_2_Phone_Communication.pptx)                                            | [link](/Echo_Device/lab_data/Lab_4_2_2) |
| Lab 4.3.1 | [Multimedia: Photos and related Data](/Echo_Device/ppts/4_3_1_Multimedia_Photos_and_Related_Data.pptx)             | [link](/Echo_Device/lab_data/Lab_4_3_1) |
| Lab 4.3.2 | [Multimedia: Videos and related Data](/Echo_Device/ppts/4_3_2_Multimedia_Videos_and_Related_Data.pptx)             | [link](/Echo_Device/lab_data/Lab_4_3_3) |
| Lab 4.3.3 | [Multimedia: Audio and related Data](/Echo_Device/ppts/4_3_3_Multimedia_Audio_and_Related_Data.pptx)               | [link](/Echo_Device/lab_data/Lab_4_3_3) |

---

### Investigating Android 10

The image is created by Joshua Hickman and hosted by [digitalcorpora](https://digitalcorpora.org/corpora/cell-phones/android-10).

| Labs      | Topics Covered                                                                                         | Size of PPTs |
| --------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| Lab 0     | [Intro Pixel 3](Andriod10/0_Intro_Pixel3_Andriod10.pptx)                                               | 3M           |
| Lab 1     | [Pixel 3 Image](Andriod10/1_Pixel3_Image.pptx)                                                         | 2M           |
| Lab 2     | [Pixel 3 Device](Andriod10/2_Pixel3_Device_Investigation.pptx)                                         | 4M           |
| Lab 3     | [Pixel 3 System Setting](Andriod10/3_Pixel3_System_settings.pptx)                                      | 5M           |
| Lab 4     | [Overview: App Life Cycle](Andriod10/4_Overivew_App_Life_Cycle.pptx)                                   | 11M          |
| Lab 5.1.1 | [AOSP App Investigations: Messaging](Andriod10/5_1_1_AOSP_App_Investigations_Messaging.pptx)           | 4M           |
| Lab 5.1.2 | [AOSP App Investigations: Contacts](Andriod10/5_1_2_AOSP_App_Investigations_Contacts.pptx)             | 3M           |
| Lab 5.1.3 | [AOSP App Investigations: Calendar](Andriod10/5_2_1_GMS_App_Investigations_Messaging.pptx)             | 1M           |
| Lab 5.2.1 | [GMS App Investigations: Messaging](Andriod10/5_2_2_GMS_App_Investigations_Dialer.pptx)                | 6M           |
| Lab 5.2.2 | [GMS App Investigations: Dialer](Andriod10/5_2_2_GMS_App_Investigations_Dialer.pptx)                   | 2M           |
| Lab 5.2.3 | [GMS App Investigations: Maps](Andriod10/5_2_3_GMS_App_Investigations_Maps.pptx)                       | 8M           |
| Lab 5.2.4 | [GMS App Investigations: Photos](Andriod10/5_2_4_GMS_App_Investigations_Photos.pptx)                   | 6M           |
| Lab 5.3.1 | [Third-Party App Investigations: Kik](Andriod10/5_3_1_Third_Party_App_Investigation_kik.pptx)          | 4M           |
| Lab 5.3.2 | [Third-Party App Investigations: textnow](5_3_2_Third_Party_App_Investigation%20_textnow.pptx)         | 1M           |
| Lab 5.3.3 | [Third-Party App Investigations: whatapp](Andriod10/5_3_3_Third_Party_App_Investigation_whatsapp.pptx) | 3M           |
| Lab 6     | [Pixel 3 Rooting](Andriod10/6_Pixel3_rooting.pptx)                                                     | 5M           |

---

### Investigating iPhone iOS 13.4.1

The image is created by Joshua Hickman and hosted by [digitalcorpora](https://digitalcorpora.org/corpora/cell-phones/ios-13).

| Labs   | Topics Covered                                                        | Size of PPTs |
| ------ | --------------------------------------------------------------------- | ------------ |
| Lab 0  | [Intro Intro iPhone iOS 13](iOS/0_Intro_iPhone_iOS13.pptx)            | 5M           |
| Lab 1  | [iOS 13.4.1 Image](iOS/1_iOS_13.4.1_Image.pptx)                       | 5M           |
| Lab 2  | [iPhone Device investigation](iOS/2_iPhone_Device_Investigation.pptx) | 3M           |
| Lab 3  | [iOS System Settings](iOS/3_iOS_System_settings.pptx)                 | 3M           |
| Lab 4  | [Overview of App Life Cycle](iOS/4_Overivew_App_Life_Cycle.pptx)      | 2M           |
| Lab 5  | [Messages Investigations](iOS/5_Messages_Investigations.pptx)         | 3M           |
| Lab 6  | [Contacts Investigations](iOS/6_Contacts_Investigation.pptx)          | 3M           |
| Lab 7  | [Calender Investigations](iOS/7_Calender_Investigation.pptx)          | 2M           |
| Lab 8  | [Safari Investigations](iOS/8_Safari_Investigation.pptx)              | 3M           |
| Lab 9  | [Photo Investigations](iOS/9_Photos_Investigation.pptx)               | 7M           |
| Lab 10 | [KnowledgeC Investigations](iOS/10_KnowledgeC_Investigation.pptx)     | 5M           |
| Lab 11 | [Health\_ Investigations](iOS/11_Health_Investigation.pptx)           | 5M           |
| Lab 12 | [Location Investigations](iOS/12_iOS_Location_Investigation.pptx)     | 8M           |
| Lab 13 | [Cellebrite Investigations](iOS/13_Cellebrite_Investigation.pptx)     | 12M          |
| Lab 14 | [Magnet Axiom Investigations](iOS/14_Magnet_Axiom_Investigation.pptx) | 13M          |
| Lab 14 | [Jailbreak Investigations](iOS/15_iOS_Jailbreak.pptx)                 | 6M           |

---

### Investigating Drone DJI

The dataset includes logical files extracted from a DJI controller (mobile device) and an SD card image used by the device. The Drone dataset is created by [VTO Labs](https://www.vtolabs.com/drone-forensics). The lab covers GPS investigation and cached image retrieval. Note that it is a draft. We will improve the lab later.

| Labs  | Topics Covered                                                                                  | Size of PPTs |
| ----- | ----------------------------------------------------------------------------------------------- | ------------ |
| Lab 0 | [DJI Mavic Air Mobile](Drone_DJI_Mavic_Air/00_DJI_Mavic_Air_Mobile.pptx)                        | 13M          |
| Lab 1 | [DJI Mavic Air MicroSD Raw](Drone_DJI_Mavic_Air/01_DJI_Mavic_Air_microSD_raw.pptx)              | 2M           |
| Lab 2 | [DJI Mavic Air MicroSD Encase Format](Drone_DJI_Mavic_Air/02_DJI_Mavic_Air_microSD_encase.pptx) | 2M           |

---

### Political Insight Analysis Leveraging LLMs

The case study demonstrates how to Leverage Large Language Models to gain political insight based on an email dataset. The dataset we have used in the case study is a set of leaked [emails](https://github.com/benhamner/hillary-clinton-emails?tab=readme-ov-file) obtained from Hillary Clinton's private email server.

The background of the leaked emails is a significant chapter in recent U.S. political history, involving questions of transparency, security, and the handling of sensitive information. During Hillary's tenure as U.S. Secretary of State from 2009 to 2013, Hillary Clinton used a private email server for her official communications instead of the official State Department email system. She stated that this was done for convenience, allowing her to use a single device for both personal and official emails.

The leaked email dataset from Hillary Clinton's private email server is a comprehensive collection of communications covering her entire tenure as Secretary of State from 2009 to 2013. It includes approximately 30,000 emails with a wide range of topics from official diplomatic communications to personal correspondences. The release and subsequent analysis of these emails have played a crucial role in political debates, legal inquiries, and public discussions about transparency and security in government communications.

Our dataset: [a set of email summaries](/AI4Forensics/CKIM2024/HillaryEmails/results_email_summary.txt). Each email summary is a summarization of an email generated by Gemini from an original email in the original leaked [email dataset](https://github.com/benhamner/hillary-clinton-emails?tab=readme-ov-file). We are only interested in emails containing the keyword "israel".

Our results: [Code in Jupyter Notebook](/AI4Forensics/CKIM2024/HillaryEmails/email_analysis_political_insight.ipynb).

Here are some political insights based on the leaked email summaries obtained from Hillary Clinton's private email server that are related to Israel: <img src="/AI4Forensics/CKIM2024/HillaryEmails/political_insight_2024-05-31_10-29-52.jpg">

---

### Tools

| Name                    | Command           | Repository                                                      | Installation Method |
| ----------------------- | ----------------- | --------------------------------------------------------------- | ------------------- |
| Wine                    | wine --version    | https://source.winehq.org/git/wine.git/                         | Custom              |
| Vinetto                 | vinetto -h        | https://github.com/AtesComp/Vinetto                             | Custom              |
| imgclip                 | imgclip -h        | https://github.com/Arthelon/imgclip                             | apt install         |
| RegRipper               | rip.pl -h         | https://github.com/keydet89/RegRipper3.0                        | Customized scirpt   |
| Windows-Prefetch-Parser | prefetch.py -h    | https://github.com/PoorBillionaire/Windows-Prefetch-Parser.git  | Custom              |
| python-evtx             | evtx_dump.py -h   | https://github.com/williballenthin/python-evtx                  | apt install         |
| libesedb-utils          | esedbexport -h    | https://github.com/libyal/libesedb                              | apt install         |
| libpff                  | pffexport -h      | https://github.com/libyal/libpff                                | apt install         |
| USN-Record-Carver       | usncarve.py -h    | https://github.com/PoorBillionaire/USN-Record-Carver            | apt install         |
| USN-Journal-Parser      | usn.py -h         | https://github.com/PoorBillionaire/USN-Journal-Parser           | apt install         |
| time_decode             | time_decode.py -h | https://github.com/digitalsleuth/time_decode                    | Git clone           |
| analyzeMFT              | analyzeMFT.py -h  | https://github.com/dkovar/analyzeMFT                            | Customized scirpt   |
| libvshadow              | vshadowinfo -h    | https://github.com/libyal/libvshadow                            | Customized scirpt   |
| INDXParse               | INDXParse.py -    |                                                                 | Customized scirpt   |
| carving sqlite .db      | undark -h         | https://github.com/inflex/undark.git                            | Customized scirpt   |
| stegdetect              | stegdetect -V     |                                                                 | Customized scirpt   |
| stegbreak               | stegbreak -V      |                                                                 | Customized scirpt   |
| stego-toolkit           | jphide            |                                                                 | Customized scirpt   |
| jpsestego-toolkitek     | jpseek            |                                                                 | Customized scirpt   |
| volatility-2            | vol.py -h         | https://github.com/volatilityfoundation/volatility.git          | Customized scirpt   |
| liblnk-utils            | lnkinfo -h        |                                                                 | apt install         |
| JLECmd                  |                   | https://f001.backblazeb2.com/file/EricZimmermanTools/JLECmd.zip | Git clone           |
| recentfilecache-parser  |                   | https://github.com/prolsen/recentfilecache-parser               |                     |
| LogFileParser           |                   | https://github.com/jschicht/LogFileParser.git                   | Git clone           |
| UsnJrnl2Csv             |                   | ttps://github.com/jschicht/UsnJrnl2Csv.git                      | Git clone           |

- Other tools installed via apt install
  python3-pip, leafpad, terminator, sqlite3, tree, xmlstarlet, libhivex-bin, pasco, libhivex-bin, npm, binwalk, foremost, hashdeep, ewf-tools, nautilus

---

## Contribution

- PI of the project
  - Dr. Frank Xu (Email: fxu at ubalt dot edu)
- Students:
  - Eric Xu: University of Maryland (LLM for Digital Forensics)
  - Sarfraz Shaikh: University of Baltimore (Echo Show)
  - Danny Ferreira (iPhone)
  - Harleen Kaur (Partial of Android)
  - Malcolm Hayward (P2P Leakage)
  - Richard (Max) Wheeless (Hacking case)
  - Chimezie Onwuegbuchulem (Docker for Digital Forensics)
  - Etinosa Osawe (AI for Forensics - Identifying IPs with a Fine-tuned Language Model)

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=frankwxu/digital-forensics-lab&type=Date)](https://star-history.com/#frankwxu/digital-forensics-lab&Date)

<a href="https://trackgit.com">
<img src="https://us-central1-trackgit-analytics.cloudfunctions.net/token/ping/ksb44j1gmfoc4ht18prk" alt="trackgit-views" />
</a>
