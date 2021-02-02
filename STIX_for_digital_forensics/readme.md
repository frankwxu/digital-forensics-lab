# STIX for Digital Forensics

## Objectives

The goal of the project is to explore and build an extended STIX™ (xSTIX), to exchange Cyber Forensic Intelligence (CFI). While STIX focuses on understanding, responding to, and mitigating computer-based attacks, the xSTIX allows cyber forensics communities to better understand what and how digital evidence is left on hosts and networks during these attacks and to reconstruct digital forensic-based crime scenes after attacks.

The xSTIX includes a set of Cyber Forensic Objects (CFOs). CFOs are CFI domain objects that are corresponding to concepts used in hosts and networks but are more intensively used for CFI, e.g., the concepts of file and webpage visits. Each CFO represents an event generated and recorded by firmware, drivers, operating systems, and software applications. The recorded event is often used to meet functional or non-functional requirements of a feature/system. For example, the Windows security feature requires logging all security-related activities for auditing; Google drive records all files' status for a faster local and remote files synchronization. CFOs are different from STIX Cyber-Observable Data objects because CFOs are pre-processed data in the context of CFI instead of raw data that Cyber-observable Objects want to describe.

## Extension Format

- Objects: We follow the STIX specification for [customizing objects](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_p2sz1mp7z524). The most important rule to create a new object type is that the value of the type property in a Custom Object SHOULD start with “x-” followed by a source unique identifier (like a domain name with dots replaced by hyphens), a hyphen and then the name. For example, x-example-com-customobject.
- [Required Properties](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_xzbicbtscatx):
  - **type** (string)： The value of this property MUST be one of CFOs.
  - **spec_version** (string): The current version is 2.1, i.e., **"spec_version": "2.1"**.
  - **id** (identifier): This id MUST meet the requirements of the identifier type [see STIX section 2.9](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_64yvzeku5a5c).
  - **created** (timestamp): The created property represents the time at which the object was originally created by an investigator (i.e., object creator).
  - **modified** (timestamp): The modified property is only used by CFOs that support versioning and represents the time that this particular version of the object was last modified.
  - **created_by_re**(identifier): The object creator is the entity (e.g., system, organization, instance of a tool) that generates the id property for a given object. It is optional in STIX SDO.
- [Common Properties used in CFOs](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_xzbicbtscatx)
  - external_references (list of type external-reference): The external_references property specifies a list of external references which refers to non-STIX information. This property is used to provide one or more URLs, descriptions, or IDs to records in other systems.

---

## Table of Contents (updating)

- Cyber Forensic Objects (CFOs)
  - [Windows Event Object](#Windows-Event-Object)
  - [Webpage Visit Event Object](#Webpage-Visit-Event-Object)
  - [Plug and Play (PnP) Event Object](#Plug-and-Play-PnP-Event-Object)
  - [File Visit Event Object](#File-Visit-Event-Object)
    - [RecentFileCache](#RecentFileCache)
    - [Shimcache](#Shimcache)
    - [UserAssist](#TUserAssist)
    - [Prefetch](#Prefetch)
    - [USNJournal](#USNJournal)
    - [Shellbags](#Shellbags)
    - [Jumplist](#Jumplist)
    - [Lnk]($Lnk)
    - [RMU]($RMU)
    - [MFT]($MFT)
    - [AppLog](#AppLog)
  - [Investigation Tool](#Investigation-Tool)
- Property Extension
  - [Extension for Windows Registry Key Object](#Extension-for-Windows-Registry-Key-Object)
- Other extension
  - [threat-actor-type-ov external reference](#threat-actor-type-ov-external-reference])

## Windows Event Record Object

**Type Name:** x-windows-evt-record

The Windows Event Record object represents an event recorded by Windows OS, including applicatioin, security, steup, system, and forwarded-events.

### Properties

| Property Name              | Type       | Description                                                                                                                                                    |
| -------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type (required)            | string     | The value of this property MUST be x-windows-evt-record.                                                                                                       |
| record_number              | string     | Specified the number of the record.                                                                                                                            |
| time_generated             | timestamp  | Specified the time at which this entry was submitted.                                                                                                          |
| time_written               | timestamp  | Specified the time at which this entry was received by the service to be written to the log.                                                                   |
| event_source               | string     | Specifies name of the name of the software or the name of a subcomponent of the application if the application is large that logs the event.                   |
| event_id                   | integer    | The value is specific to the event source for the event, and is used with source name to locate a description string in the message file for the event source. |
| event_id_string            | integer    | Specified the description string of event_id.                                                                                                                  |
| event_type                 | string     | It MUST be one EventType defined in [Windows Doc](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-eventlogrecord)                            |
| event_category             | enum       | Categories help to organize events                                                                                                                             |
| user_account_ref(required) | identifier | The user account that is associated with the evewnt.                                                                                                           |
| saved_to_ref(required)     | identity   | Specifies object type that event object belongs to. It MUST be a type of file or artifact                                                                      |

Notes:

- event_source has a few types, such as application, secuirty, system, customlog, etc.
- user_account_ref can be retrived based on SID.

### Relationships

| Source | Relationship Type | Target | Description |
| ------ | ----------------- | ------ | ----------- |

### Example 1: describes a "logon" event recorded in the security event file.

```json
[
  {
    "type": "x-windows-evt",
    "spec_version": "2.1",
    "id": "x-windows-evt--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "record_number": "12145",
    "time_generated": "2015-01-06T20:03:00.000Z",
    "time_written": "2015-01-06T20:03:00.100Z",
    "event_source": "Microsoft Windows security auditing.",
    "event_id": "4624",
    "event_id_string": "An account was successfully logged on",
    "event_type": "EVENTLOG_AUDIT_SUCCESS",
    "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
    "saved_to_ref": "file--79e0da61-48e2-4552-874f-83d74262f39d",
    "created": "2021-01-06T20:03:00.000Z",
    "modified": "2021-01-06T20:03:00.000Z",
    "external_references": [
      {
        "source_name": "ns-winnt-eventlogrecord",
        "url": "https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-eventlogrecord"
      }
    ]
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--79e0da61-48e2-4552-874f-83d74262f39d",
    "hashes": {
      "SHA-256": "fe90a7e910cb3a4739bed9180e807e93fa70c90f25a8915476f5e4bfbac681db"
    },
    "size": 4518,
    "name": "security.evt"
  }
]
```

### Example 2: describes a system event generated by CD-Rom

```json
{
  "type": "x-windows-evt",
  "spec_version": "2.1",
  "id": "x-windows-evt--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "record_number": "4512",
  "time_generated": "2015-01-06T20:03:00.000Z",
  "time_written": "2015-01-06T20:03:00.100Z",
  "event_source": "cdrom",
  "event_id": "16388",
  "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
  "saved_to_ref": "file--79e0da61-48e2-4552-874f-83d74262f39d",
  "created": "2021-01-06T20:03:00.000Z",
  "modified": "2021-01-06T20:03:00.000Z",
  "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
  "saved_to_ref": "file--e2dd9934-e6aa-440a-9d51-21ccf990c4f5"
}
```

## Webpage Visit Event Object

**Type Name:** x-webpage-visit-evt

The Webpage Visit Event object represents a single visit to a webpage.

### Properties

| Property Name          | Type       | Description                                                                                |
| ---------------------- | ---------- | ------------------------------------------------------------------------------------------ |
| type (required)        | string     | The value of this property MUST be browser-history.                                        |
| entry_id               | string     | Specifies the unqie entry ID in a file (i.e., save_to_ref) that the event saved to.        |
| url_ref                | identifier | Specify a visit to a url.                                                                  |
| title                  | string     | Speify the title of a web page (if a URL is a webpage) that has been visited.              |
| visit_time             | timestamp  | The last time visited.                                                                     |
| visit_count            | integer    | The number of times visited                                                                |
| browser_ref            | identifier | The value type for this property SHOULD software.                                          |
| file_requested_ref     | identifier | The ID of the file the http requested.                                                     |
| user_account_ref       | identifier | The user account that is associated with record.                                           |
| saved_to_ref(required) | identifier | Specifies object type that event object belongs to. It MUST be a type of file or artifact. |

### Relationships

| Source | Relationship Type | Target | Description |
| ------ | ----------------- | ------ | ----------- |

### Examples

```json
[
  {
    "type": "x-browser-history-evt",
    "spec_version": "2.1",
    "id": "x-browser-history-evt--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "url_ref": "url--9cc5a5dc-0acd-46f5-ae3f-724370087622",
    "title": "B.S. in Cyber Forensics | University of Baltimore",
    "visit-time": "2021-01-06T20:03:22.000Z",
    "visit-count": 2,
    "browser_ref": "software--b67a8d52-d438-4ace-8285-c6d485e34192",
    "file_requested_ref ": "file--10624790-0e43-4498-89da-8979ab4215ae",
    "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
    "saved_to_ref": "file--843f6a43-0603-4e0d-84a4-198386eecf4f"
  },
  {
    "type": "url",
    "spec_version": "2.1",
    "id": "url--9cc5a5dc-0acd-46f5-ae3f-724370087622",
    "v,alue": "https://www.ubalt.edu/cpa/undergraduate-majors-and-minors/majors/cyber-forensics/"
  },
  {
    "type": "software",
    "spec_version": "2.1",
    "id": "software--b67a8d52-d438-4ace-8285-c6d485e34192",
    "name": "chrome",
    "cpe": "cpe:2.3:a:google:chrome:88.0.4324.104:*:*:*:*:*:*:*",
    "vendor": "Google"
  }
]
```

## Plug and Play (PnP) Event Object

**Type Name:** x-pnp-evt

The Plug and Play (PnP) Event object represents an event recorded by Windows Kernel-Mode Plug (pnp) and Play Manager. PnP manager is a combination of hardware technology and software techniques that enables a PC to recognize when a device is added to the system. With PnP, the system configuration can change with little or no input from the user.

### Properties

The completed log properties can be access [Microsoft office docs- Format of a text log section body](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/format-of-a-text-log-section-body)

| Property Name          | Type       | Description                                                                                                                                                |
| ---------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type (required)        | string     | The value of this property MUST be x-pnp-evt.                                                                                                              |
| entry_prefix           | enum       | The values of this property MUST come from the message-type-ov enumeration.                                                                                |
| time_stamp             | timestamp  | Indicates the system time when the logged event occurred.                                                                                                  |
| event_category         | string     | Indicates the category of SetupAPI operation that made the log entry. MUST be one of predefined Event_category operation strings, e.g.device installation. |
| formatted_message      | string     | Contains the specific information that applies to the log entry.                                                                                           |
| saved_to_ref(required) | identifier | Specifies object type that event object belongs to. It MUST be a type of file or artifact (e.g., cache, memory), e.g., steupAPI.log                        |

### Message Type Vocabulary

Vocabulary Name: message-type-ov

| ocabulary Value | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| error           | An Error message                                                     |
| warning         | An warning message                                                   |
| other-info      | Information message other than an error message or a warning message |

### Examples

```json
{
  "type": "x-pnp-evt",
  "spec_version": "2.1",
  "id": "x-pnp-evt--58959aae-d1e0-4e12-a879-270efe33c6e3",
  "entry_prefix": "other-info",
  "time_stamp": "2021-01-06T20:03:22.000Z",
  "event_category": "device installation",
  "formatted_message ": "Device Install (Hardware initiated) - USB\\VID_0781&PID_5517\\4C5300124505311010593",
  "saved_to_ref": "file--176353bd-b61d-4944-b0cd-0b98783c50b5"
}
```

## File Visit Event Object

**Type Name:** x-file-visit-evt

The File Visit Event object represents properties that are associasted with a file/directory visited by operating systems or applications. The event is generated when a file is read, modified, executed, preloaded. etc. The event may be saved in different forms, e.g., file, cache, Windows registry, etc.

### Properties

| Property Name             | Type       | Description                                                                                                                                                    |
| ------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type (required)           | string     | The value of this property MUST be x-file-visit-evt.                                                                                                           |
| visit_type                | enum       | Specifies how file was visited. The values of this property MUST come from the file-visit-type-enum enumeration.                                               |
| visit_time                | timestamp  | Specifies the time a file was visited.                                                                                                                         |
| visit_file_guid           | string     | The GUID of an application, e.g., {A3D53349-6E61-4557-8FC7-0028EDCEEBF6}} is Windows 8.                                                                        |
| visit_count               | integer    | The total number of times the program has visited.                                                                                                             |
| visit_file_ref (required) | identifier | Specifies the file or directory that was recently visited.                                                                                                     |
| record_reason             | open-vocab | Specifies a resaon why an event is recorded. It MUST come from the file-visit-evt-record-reason-ov open vocabulary.                                            |
| created_by_software_ref   | identifier | The softwre that is used to capture and save the event. The value of this property MUST be the identifier for a SCO software object.                           |
| saved_to_ref(required)    | identifier | Specifies object type that event object belongs to. It MUST be a type of file (e.g., RecentFileCache.bcf or Amcache.hve), registry, artifact, or or directory. |

### File Visit Type Enum

Vocabulary Name: file-visit-type-enum

| Vocabulary Value | Description                                                                   |
| ---------------- | ----------------------------------------------------------------------------- |
| creation         | A file was visited for creation.                                              |
| reading          | A file was visited for reading.                                               |
| modification     | A file was was visited for modification (content is to be modified).          |
| updating         | The meta data of a file was visited for changing (e.g. permissions)           |
| execution        | A file was visited for execution.                                             |
| deletion         | A file was visited for deletion.                                              |
| preloading       | A file was visited for preloading to memory.                                  |
| prefetching      | A file was visited for prefetching to memory.                                 |
| loading          | A file was visited for loading to memory.                                     |
| unloading        | A file was visited for unloading from memory.                                 |
| other            |                                                                               |
| unknown          | There is not enough information available to determine how file was accessed. |

### File Visit Event Record Reason Vocabulary

**Vocabulary Name:** file-visit-evt-record-reason-ov

| Vocabulary Value | Description                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| userassist       | Track every GUI-based programs launched from the desktop in the userassist registry key. |
| shimcache        | Shimcache is created to identify application compatibility issues.                       |
| recentfilecache  | RecentFileCache.bcf only containes references to programs that recently executed.        |
| prefetch         |                                                                                          |
| muicache         | Support multiple language for software.                                                  |
| usnjournal       | Store Update Sequence Number Journal.                                                    |
| shellbag         | Store user preferences for GUI folder display within Windows Explorer.                   |
| jumplist         | Represents a list of items and tasks displayed as a menu on a Windows 7 taskbar button.  |
| mru              | Most recently used files.                                                                |
| autorun          |                                                                                          |
| mft              | Master file table                                                                        |
| applog           | Logs generated by applications.                                                          |

### RecentFileCache

RecentFileCache.bcf only containes references to programs that recently executed. setuputility.exe is recently executed.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--83aee86d-1523-4111-938e-8edc8a6c804f",
    "visit_type": "execution",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_file_ref": "file--7bd8980c-91eb-461a-a357-ae75a35374e6",
    "record_reason": "recentfilecache",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "file--176353bd-b61d-4944-b0cd-0b98783c50b5"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--7bd8980c-91eb-461a-a357-ae75a35374e6",
    "size": 25536,
    "name": "setuputility.exe "
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--176353bd-b61d-4944-b0cd-0b98783c50b5",
    "hashes": {
      "SHA-256": "fe90a7e910cb3a4739bed9180e807e93fa70c90f25a8915476f5e4bfbac681db"
    },
    "size": 51164,
    "name": "RecentFileCache.bcf"
  },
  {
    "type": "software",
    "spec_version": "2.1",
    "id": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "name": "Windows",
    "cpe": "cpe:2.3:o:microsoft:Windows:-:*:*:*:*:*:*:*",
    "version": "7",
    "vendor": "Microsoft"
  }
]
```

### Shimcache

Shimcache is created to identify application compatibility issues. Two actions/events that can cause the Shimcache to record an entry:
(1) A file is executed and (2) A user interactively browses a directory.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--83aee86d-1523-4111-938e-8edc8a6c804f",
    "visit_type": "executed",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_file_ref": "file--7bd8980c-91eb-461a-a357-ae75a35374e6",
    "record_reason": "shimcache",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "windows-registry-key--2ba37ae7-2745-5082-9dfd-9486dad41016"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--150c4200-02c6-475d-ac44-2d4e65de9f36",
    "size": 5536,
    "name": "twext.dll "
  },
  {
    "type": "windows-registry-key",
    "spec_version": "2.1",
    "id": "windows-registry-key--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Session Manager\\AppCompatCache\\"
  }
]
```

### UserAssist

Windows System, every GUI-based programs launched from the desktop are tracked in this registry key HKEY_USERS\{SID}\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist.
An Example of Security ID (SID) is S-1-5-21-394942887-4226445097-2438273937-1001.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "visit_type": "execution",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_file_ref": "file--674f8200-b56a-473b-9b1d-32a911ac5387",
    "visit_count": 1,
    "record_reason": "userassist",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "windows-registry-key--2ba37ae7-2745-5082-9dfd-9486dad41016"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--150c4200-02c6-475d-ac44-2d4e65de9f36",
    "size": 55136,
    "name": "WINWORD.EXE"
  },
  {
    "type": "windows-registry-key",
    "spec_version": "2.1",
    "id": "windows-registry-key--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "key": "HKEY_USERS\\S-1-5-21-394942887-4226445097-2438273937-1001\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist"
  }
]
```

### Prefetch

Prefetch preloads most frequently used software into memory. The Typeshows the chrome.exe-999b1ba.pf contains chrome.exe-999b1ba.exe, the time when the exe file is executed, last time executed, and how many times it was exeucted.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "visit_type": "execution",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_count": 71,
    "visit_file_ref": "file--674f8200-b56a-473b-9b1d-32a911ac5387",
    "record_reason": "prefetch",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "file--2ba37ae7-2745-5082-9dfd-9486dad41016"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--150c4200-02c6-475d-ac44-2d4e65de9f36",
    "name": "chrome.exe-999b1ba.exe "
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "hashes": {
      "MD5": "af15a4b4b0c8378d1206336962d7b5b9"
    },
    "name": "chrome.exe-999b1ba.pf "
  }
]
```

### USNJournal

USN (Update Sequence Number) Journal records all files changes (e.g.., rename) that are made to volume.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "visit_type": "modification",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_file_ref": "file--674f8200-b56a-473b-9b1d-32a911ac5387",
    "record_reason": "usnjournal",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "file--2ba37ae7-2745-5082-9dfd-9486dad41016"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--150c4200-02c6-475d-ac44-2d4e65de9f36",
    "name": "Desert.jpg "
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "hashes": {
      "MD5": "eaeb631cc86f85835dcad66766b8f3cc"
    },
    "name": "UsnJrnl_2020-11-28.csv"
  }
]
```

### Shellbags

Windows uses the Shellbag keys to store user preferences for GUI folder display within Windows Explorer to improve user experience and “remember” preferences. The following Type descrbes a USB drive is attached/visited.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "visit_type": "read",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_file_ref": "file--28d2e12c-c56c-4aaf-aeed-d0b69ccc601c",
    "record_reason": "shellbag",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "file--14a4a46c-0957-4b9d-900d-35cb8379055c"
  },
  {
    "type": "directory",
    "spec_version": "2.1",
    "id": "directory--28d2e12c-c56c-4aaf-aeed-d0b69ccc601c",
    "name": "My Computer\\E:\\"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--14a4a46c-0957-4b9d-900d-35cb8379055c",
    "hashes": {
      "MD5": "1741ab33fd6a05a4963564f36a043afc"
    },
    "name": "UsrClass_informat.dat"
  }
]
```

### Jumplist

Jumplist represents a list of items and tasks displayed as a menu on a Windows 7 taskbar button. The following Type shows a Jumplist of Word 2010 Pinned and Recent accessed files.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "visit_type": "read",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_file_ref": "file--28d2e12c-c56c-4aaf-aeed-d0b69ccc601c",
    "record_reason": "jumplist",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "file--14a4a46c-0957-4b9d-900d-35cb8379055c"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--28d2e12c-c56c-4aaf-aeed-d0b69ccc601c",
    "name": "winter_whether_advisory.zip"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--14a4a46c-0957-4b9d-900d-35cb8379055c",
    "hashes": {
      "MD5": "9857b91a6427496e72d779893e6d49fb"
    },
    "name": "a7bd71699cd38d1c.automaticDestinations-ms"
  }
]
```

### Lnk

lnk is a shortcut or "link" used by Windows as a reference to an original file, folder, or application. The example describes an event is generated when a file is accessed by a link.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--ac69c037-c578-4c5e-ad6a-23d53a0b1d6e",
    "visit_type": "read",
    "visit_time ": "2021-01-16T21:03:22.000Z",
    "visit_file_ref": "file-8c33da4c-fb61-4658-b28c-a5c60f561d78",
    "record_reason": "lnk",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "file--676b743a-3a56-4084-aeb5-fa9cfadf5663"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--8c33da4c-fb61-4658-b28c-a5c60f561d78",
    "name": "(secret_project)_pricing_decision.xlsx"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--676b743a-3a56-4084-aeb5-fa9cfadf5663",
    "hashes": {
      "MD5": "9857b91a6427496e72d779893e6d49fb"
    },
    "name": "(secret_project)_pricing_decision.xlsx.lnk"
  }
]
```

### RMU

Most Recently Used files.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--8cdbf030-89d9-48be-b733-5f4900706f0e",
    "visit_type": "read",
    "visit_time ": "2021-01-16T21:03:22.000Z",
    "visit_file_ref": "file-8c33da4c-fb61-4658-b28c-a5c60f561d78",
    "record_reason": "rmu",
    "created_by_software_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "saved_to_ref": "file--676b743a-3a56-4084-aeb5-fa9cfadf5663"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--8c33da4c-fb61-4658-b28c-a5c60f561d78",
    "name": "(secret_project)_pricing_decision.xlsx"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--676b743a-3a56-4084-aeb5-fa9cfadf5663",
    "hashes": {
      "MD5": "9857b91a6427496e72d779893e6d49fb"
    },
    "name": "informant.DAT"
  }
]
```

### MFT

A deletion was logged by MFT

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--9880e636-38b0-471a-8266-8a622a95b3a5",
    "visit_type": "read",
    "visit_time ": "2021-01-16T21:03:22.000Z",
    "visit_file_ref": "file-f7d4aa7a-d02c-481e-8bdc-450cb0669b5d",
    "record_reason": "mft",
    "saved_to_ref": "file--19be1a16-4b87-4fc4-b056-dc9e0389d4bd"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--f7d4aa7a-d02c-481e-8bdc-450cb0669b5d",
    "name": "desktop.ini"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--19be1a16-4b87-4fc4-b056-dc9e0389d4bd",
    "hashes": {
      "MD5": "64c6451132676e5a14e20d7d9283fa58"
    },
    "name": "$MFT"
  }
]
```

### AppLog

An event logged by Google drive. The event shows a file (happy_holiday.jpg) has been deleted.

```json
[
  {
    "type": "x-file-visit-evt",
    "spec_version": "2.1",
    "id": "x-file-visit-evt--9880e636-38b0-471a-8266-8a622a95b3a5",
    "visit_type": "read",
    "visit_time ": "2021-01-16T21:03:22.000Z",
    "visit_file_ref": "file-8cdbf030-89d9-48be-b733-5f4900706f0e",
    "record_reason": "rmu",
    "created_by_software_ref": "software--764c3bcd-e053-46dc-b77d-51de1a311b39",
    "saved_to_ref": "file--d5faf70b-36b8-437c-9137-6c0fc83b1e69"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--8cdbf030-89d9-48be-b733-5f4900706f0e",
    "name": "(secret_project)_pricing_decision.xlsx"
  },
  {
    "type": "file",
    "spec_version": "2.1",
    "id": "file--d5faf70b-36b8-437c-9137-6c0fc83b1e69",
    "hashes": {
      "MD5": "64c6451132676e5a14e20d7d9283fa58"
    },
    "name": "sync_log.log"
  },
  {
    "type": "software",
    "spec_version": "2.1",
    "id": "software--764c3bcd-e053-46dc-b77d-51de1a311b39",
    "name": "Windows",
    "cpe": "cpe:2.3:a:google:drive:-:*:*:*:*:*:*:*",
    "version": "1.0.257",
    "vendor": "Google"
  }
]
```

## Investigation Tool

**Type Name:** x-investigation-tool

Investigation Tools are software that can be used by cyber investigators to perform digital forensic investigations. This CFO MUST NOT be used to characterize malware and SDO tools.

### Optional Common Properties: external_references

### Investigation Tool Specific Properties

| Property Name   | Type                    | Description                                                                                   |
| --------------- | ----------------------- | --------------------------------------------------------------------------------------------- |
| type (required) | string                  | The value of this property MUST be x-file-visit-evt.                                          |
| last_modified   | timestamps              | The last modified date of the investigation tool.                                             |
| description     | string                  | A description that provides more details and context about the investigation tool.            |
| tool_types      | list of type open-vocab | The values for this property SHOULD come from the investigation-tool-type-ov open vocabulary. |
| aliases         | list of type string     | Alternative names used to identify this investigation tool.                                   |
| tool_version    | string                  | The version identifier associated with the investigation tool.                                |
| software_ref    | identifier              | Specifier the software product (if CPE or SWID is known) used as the investigation tool.      |

## Investigation Tool Type Vocabulary

**Vocabulary Name:** investigation-tool-type-ov
Investigation Tool Type is an open vocabulary that describes the type of the tools used for cyber investigations. It doesn't include common software, such as MS office, database etc.

| Vocabulary Value   | Description                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| decryption         | Tools used to perform decryption tasks.                                                                         |
| decode             | Tools used to decode data in a readable form.                                                                   |
| data-recovery      | Tools used to process of retrieving inaccessible, lost, corrupted, damaged or formatted data from disk storage. |
| data-carving       | Tools used to reassemble useful information from raw data fragments when no filesystem metadata is available.   |
| anti-steganography | Tools used to against steganography.                                                                            |
| data_extraction    | Tools used to extract information from file systems.                                                            |
| parse              | Tools used to parse and/or decode files, including registry parsers and log parsers.                            |
| dump               | Tools used to dump information from cache or memory.                                                            |
| unknown            | There is not enough information available to determine the type of tool.                                        |

### Examples

Use an open-source software to parse and decode $LogFile records

```json
{
  "type": "x-investigation-tool",
  "spec_version": "2.1",
  "id": "x-investigation-tool--c65a985d-dc31-441e-840b-54381cef4e31",
  "name": "LogFileParser",
  "tool_types": ["decode", "parse"],
  "description": "This program decodes and parses $LogFile records and transaction entries.",
  "external_references": [
    {
      "source_name": "LogFileParser",
      "url": "https://github.com/jschicht/LogFileParser"
    }
  ]
}
```

## Extension for Windows Registry Key Object

We focus on extending the data property of registry value as the data may contain rich information that needs to be organized and formalized as digital evidence. The pattern of the extension is shown below. Note that the string **"x_data"** is assigned to **"data"** (e.g., **"data": "x_data"**) as a place holder and **x_data:[]** is the extended property that contains formalized information of data.

```json
{
  "type": "windows-registry-key",
  "spec_version": "2.1",
  "id": "windows-registry-key--2ba37ae7-2745-5082-9dfd-9486dad41016",
  "key": "hkey_local_machine\\system\\bar\\foo",
  "values": [
    {
      "name": "Foo",
      "data": "x_data",
      "data_type": "REG_BINARY"
    }
  ],
  "x_data": [
    {
      "type": "x-extended-type",
      "id": "x-extended-type--83aee86d-1523-4111-938e-8edc8a6c804f"
    }
  ]
}
```

---

## threat-actor-type-ov external reference

| Vocabulary Value                     | Description                                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------- |
| criminal-intellectual-property-theft | An individual that intentionally deprives someone of his or her intellectual property |
| criminal-ransomware                  |                                                                                       |
| criminal-business-email-compromise   |                                                                                       |
| criminal-identity-theft              |                                                                                       |
| criminal-spoofing-and-phishing       |                                                                                       |
| criminal-memory-laundry              |                                                                                       |
| insider-disgruntled-sabotage         |                                                                                       |
| insider-disgruntled-violence         |                                                                                       |
| insider-disgruntled-theft            |                                                                                       |
| insider-disgruntled-fraud            |                                                                                       |
| insider-disgruntled-espionage        |                                                                                       |
| insider-disgruntled-embarrassing     |                                                                                       |
| insider-disgruntled-harassing        |                                                                                       |
| illegal-possessor                    | An individual that owns, produces, distributes illegal information and device.        |
| online- predators                    | An individual that makes sexual advances to minors.                                   |

# references:

- https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4608
- [Event Logging Structures](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-logging-structures?redirectedfrom=MSDN)
- https://github.com/libyal/libevt/blob/main/documentation/Windows%20Event%20Log%20(EVT)%20format.asciidoc
- https://github.com/williballenthin/python-evtx
- https://www.loggly.com/ultimate-guide/windows-logging-basics/#:~:text=The%20Windows%20event%20log%20contains,For%20example%2C%20IIS%20Access%20Logs.
- https://docs.microsoft.com/en-us/windows-hardware/drivers/install/format-of-a-text-log-section-body

```

```
