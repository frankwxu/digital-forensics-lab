# Digital Forensics Lab & Shared Cyber Forensic Intelligence Repository

| Hands-on labs                                                                            | Forensic Intelligence Repository                                                              |
| ---------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/BJA_Logo.png" width="130"> | <img src="https://www.nist.gov/sites/default/files/images/2017/06/16/dsh-st.jpg" width="130"> |

### Features of Repository

===================

- Hands-on Digital Forensics Labs: designed for Students and Faculty
- Linux-based lab: All labs are purely based on [Kali Linux](https://www.kali.org/downloads/)
- Lab screenshots: Each lab has PPTs with instruction screenshots
- Comprehensive: Cover many topics in digital forensics
- Free: All tools are open source
- Updated: The project is funded by DOJ and will keep updating
- Two formalized forensic intelligence in JSON files based-on case studies

---

## Table of Contents (updating)

- Basic Computer Skills for Digital Forensics
  - [Number Systems](/Basic_Computer_Skills_for_Forensics/0_Number_Systems.pptx)
  - [PC Introduction](/Basic_Computer_Skills_for_Forensics/1_PC_Introduction.pptx)
  - [Windows Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/2_Win_command_line_tutorial.pptx)
  - [Linux Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/3_Linux_command_line_tutorial.pptx)
  - [Advanced Linux Command Line Tutorial](/Basic_Computer_Skills_for_Forensics/4_Advanced_linux_command_line.pptx)
- Computer and Digital Forensics (updated on Oct. 2021)
  - [Introduction to Digital Forensics](/Basic_Computer_Skills_for_Forensics/5_Introduction_to_digital_forensics.pptx)
  - [Sleuth Kit Tutorial](/Basic_Computer_Skills_for_Forensics/6_Sleuth_Kit_Tutorial.pptx)
  - [USB Image Acquisition](/Basic_Computer_Skills_for_Forensics/7_USB_Image_Acquisition.pptx)
  - [Evidence Search Techniques](/Basic_Computer_Skills_for_Forensics/8_Evidence_search_techniques.pptx)
  - [Data Carving](/Basic_Computer_Skills_for_Forensics/9_Data_Carving.pptx)
  - [Steganography](/Basic_Computer_Skills_for_Forensics/10_Steganography.pptx)
  - [Forensic Report Template](/Basic_Computer_Skills_for_Forensics/Forensic_Report_Template.pdf)
- Computer Forensics Case Study
  - [Investigating P2P Data Leakage](#Investigating-P2P-Data-Leakage) (added on June 2021)
  - [Investigating NIST Data Leakage](#Investigating-NIST-Data-Leakage)
  - [Investigating Illegal Possession of Images](#Investigating-Illegal-Possession-of-Images "Networking forensics")
  - [Investigating Email Harassment](#Investigating-Email-Harassment)
  - [Investigating Illegal File Transferring (Memory Forensics)](#Investigating-illegal-File-Transferring "Memory Forensics")
  - [Investigating Hacking Case](#Investigating-Hacking-Case)
- Mobile Forensics Case Study
  - [Investigating Android 10](#Investigating-Android-10) (added on Oct/24/2021)
  - iOS 13 (to be released...)
- Forensic Intelligence Repository
  - [Email forensics](/STIX_for_digital_forensics/Email_Harassment)
  - [Illegal Possession of Images](/STIX_for_digital_forensics/Illegal_Possession_Images)
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

The [P2P data leakage case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) is to help students to apply various forensic techniques to investigate intellectual property theft involving P2P. The study include

- A large and complex case involving a uTorrent client. The case is similar to NIST data leakage lab. However, it provides a clearer and more detailed timeline.
- Solid evidence with explanations. Each evidence that is associated with each activity is explained along with the timeline. We suggest using this before study NIST data leakage case study.
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

### Investigating NIST Data Leakage

==============

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Data_Leakage_Case) is to investigate an image involving intellectual property theft. The study include

- A large and complex case study created by NIST. You can access the [Senario, DD/Encase images](https://www.cfreds.nist.gov/data_leakage_case/data-leakage-case.html). You can also find the [solutions](https://www.cfreds.nist.gov/data_leakage_case/leakage-answers.pdf) on their website.
- 14 hands-on labs/topics in digital forensics

**Topics Covered**

| Labs   | Topics Covered                                                                                              | Size of PPTs |
| ------ | ----------------------------------------------------------------------------------------------------------- | ------------ |
| Lab 0  | [Environment Setting Up](NIST_Data_Leakage_Case/NIST_Data_Leakage_00_Env_Setting.pptx)                      | 2M           |
| Lab 1  | [Windows Registry](NIST_Data_Leakage_Case/NIST_Data_Leakage_01_Registry.pptx)                               | 3M           |
| Lab 2  | [Windows Event and XML](NIST_Data_Leakage_Case/NIST_Data_Leakage_02._WinEvt_XML.pptx)                       | 3M           |
| Lab 3  | [Web History and SQL](NIST_Data_Leakage_Case/NIST_Data_Leakage_02._WinEvt_XML.pptx)                         | 3M           |
| Lab 4  | [Email Investigation](NIST_Data_Leakage_Case/NIST_Data_Leakage_04_Email_USB.pptx)                           | 3M           |
| Lab 5  | [File Change History and USN Journal](NIST_Data_Leakage_Case/NIST_Data_Leakage_05_USNJournaling.pptx)       | 2M           |
| Lab 6  | [Network Evidence and shellbag](NIST_Data_Leakage_Case/NIST_Data_Leakage_06_Network_Shellbag_Jumplist.pptx) | 2M           |
| Lab 7  | [Network Drive and Windows shellbag](NIST_Data_Leakage_Case/NIST_Data_Leakage_07_NetworkDrive_Cloud.pptx)   | 5M           |
| Lab 8  | [Master File Table ($MFT) Analysis](NIST_Data_Leakage_Case/NIST_Data_Leakage_08_CD_%24MFT.pptx)             | 4M           |
| Lab 9  | [Windows Search History](NIST_Data_Leakage_Case/NIST_Data_Leakage_08_CD_%24MFT.pptx)                        | 4M           |
| Lab 10 | [Windows Volume Shadow Copy Analysis](NIST_Data_Leakage_Case/NIST_Data_Leakage_10_Vol_Shadow_Copy.pptx)     | 6M           |
| Lab 11 | [Recycle Bin and Anti-Forensics](NIST_Data_Leakage_Case/NIST_Data_Leakage_11_RecycleBin_AntiForensics.pptx) | 3M           |
| Lab 12 | [Data Carving](NIST_Data_Leakage_Case/NIST_Data_Leakage_12_CD-R_Data_Carving.pptx)                          | 3M           |
| Lab 13 | [Crack Windows Passwords](NIST_Data_Leakage_Case/NIST_Data_Leakage_13_Crack_Win10_Login_Password.pptx)      | 2M           |

---

### Investigating Illegal Possession of Images

=====================

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_Possession_Images) is to investigate the illegal possession of Rhino images. This image was contributed by Dr. Golden G. Richard III, and was originally used in the DFRWS 2005 RODEO CHALLENGE. NIST hosts the [USB DD image](https://www.cfreds.nist.gov/dfrws/Rhino_Hunt.html). A copy of the image is also available in the repository.

**Topics Covered**

| Labs  | Topics Covered                                                                                                                                | Size of PPTs |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Lab 0 | [HTTP Analysis using Wireshark (text)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_1_text.pptx)                                        | 3M           |
| Lab 1 | [HTTP Analysis using Wireshark (image)](Illegal_Possession_Images/HTTP_Wireshark_Forensics_2_image.pptx)                                      | 6M           |
| Lab 2 | [Rhion Possession Investigation 1: File recovering](Illegal_Possession_Images/Rhion_Possession_1_File_Recovering.pptx)                        | 9M           |
| Lab 3 | [Rhion Possession Investigation 2: Steganography](Illegal_Possession_Images/Rhion_Possession_2_Steganography.pptx)                            | 4M           |
| Lab 4 | [Rhion Possession Investigation 3: Extract Evidence from FTP Traffic](Illegal_Possession_Images/Rhion_Possession_3_FTP_Traffic_crackzip.pptx) | 3M           |
| Lab 5 | [Rhion Possession Investigation 4: Extract Evidence from HTTP Traffic](Illegal_Possession_Images/Rhion_Possession_4_HTTP_Traffic.pptx)        | 5M           |

### Investigating Email Harassment

=========

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Email_Harassment) is to investigate the harassment email sent by a student to a faculty member. The case is hosted by digitalcorpora.org. You can access the [senario description](https://digitalcorpora.org/corpora/scenarios/nitroba-university-harassment-scenario) and [network traffic](http://downloads.digitalcorpora.org/corpora/scenarios/2008-nitroba/nitroba.pcap) from their website. The repository only provides lab instructions.

**Topics Covered**

| Labs  | Topics Covered                                                                                                   | Size of PPTs |
| ----- | ---------------------------------------------------------------------------------------------------------------- | ------------ |
| Lab 0 | [Investigating Harassment Email using Wireshark](Email_Harassment/0_Investigate_Harassment_Email_Wireshark.pptx) | 3M           |
| Lab 1 | [t-shark Forensic Introduction](Email_Harassment/1_tshark_forensics_Introduction.pptx)                           | 2M           |
| Lab 2 | [Investigating Harassment Email using t-shark](2_Investigate_Harassment_Email_TShark.pptx)                       | 2M           |

### Investigating Illegal File Transferring (Memory Forensics )

=========

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/Illegal_File_Transferring_Memory_Forensics) is to investigate computer memory for reconstructing a timeline of illegal data transferring. The case includes a scenario of transfer sensitive files from a server to a USB.

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

### Investigating Hacking Case

=========

The [case study](https://github.com/frankwxu/digital-forensics-lab/tree/main/NIST_Hacking_Case), including a disk image provided by [NIST](https://www.cfreds.nist.gov/Hacking_Case.html) is to investigate a hacker who intercepts internet traffic within range of Wireless Access Points. Note that the PPT is encrypted with a password as one of the major assignments. Email fxu at ubalt dot edu to ask the password if you are a faculty member.

**Topics Covered**

| Labs  | Topics Covered                                            | Size of PPTs |
| ----- | --------------------------------------------------------- | ------------ |
| Lab 0 | [Hacking Case](/NIST_Hacking_Case/NIST_Hacking_Case.pptx) | 8M           |

### Investigating Android 10

The image is created by Joshua Hickman and hosted by [digitalcorpora](https://digitalcorpora.org/corpora/cell-phones/android-10).

=========

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

<script async src="//static.getclicky.com/101329461.js"></script>

<img width="1" height="1" src="//in.getclicky.com/101329461ns.gif" />

<a href="https://trackgit.com">
<img src="https://us-central1-trackgit-analytics.cloudfunctions.net/token/ping/ksb44j1gmfoc4ht18prk" alt="trackgit-views" />
</a>
