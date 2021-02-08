# STIX for Digital Forensics

## Objectives

The goal of the project is to explore and build an extended STIX™ (xSTIX) for exchanging Cyber Forensic Intelligence (CFI). While STIX focuses on understanding, responding to, and mitigating computer-based attacks, the xSTIX allows cyber forensics communities to better understand what and how digital evidence is left on hosts and networks during these attacks and to reconstruct digital forensic-based crime scenes after attacks. The reconstructed crime scenes along with the supporting evidence should be presentable and explainable in courts.

The xSTIX includes a set of Cyber Forensic Objects (CFOs), customized properties, and extended open vocabulary. They are categorized as follows:

- **Cyber Forensic Objects (CFOs)**

  - **Cyber Forensic Domain Objects (CFDOs):** CFDOs are CFI domain objects that are corresponding to concepts used in hosts and networks but are more intensively used for CFI, e.g., the concepts of disk image, file visit evidence, and webpage webpage visit evidence. A collection of CFDOs answer questions such as (1) how evidence is generated, collected, and stored, (2) who left evidence on disk images, (3) What cybercrime activities were performed? (4) What and how evidence does indicate these activities? Note that the concept of evidence plays a key role of CFI due to the natural of cyber forensic investigations. Evidence is log data resides on disks. The log data, in various forms, is often generated and used to meet functional or non-functional requirements of a feature/system originally. For example, the Windows security feature requires logging all security-related activities for auditing; Google drive records all files' status for a faster local and remote files synchronization. Cyber investigations often utilize these logs to reconstruct the behaviors of users. CFDOs are different from STIX Cyber-Observable Data objects because CFDOs are pre-processed data in the context of CFI instead of raw data that Cyber-observable Objects want to describe.

  - **Cyber Forensic Observable Objects (CFOOs):** CFOOs are similar to STIX SCOs. They are used to describe Cyber-observable Objects that frequently used for for CFI, e.g., a disk partition object represents the contents and structure of a disk segment.

- **Custom Properties to STIX objects:**: Customize properties of existing STIX objects to support forensic investigations. For example, registry value as the data may contain rich information that needs to be organized and formalized as digital evidence. The organized information will be formalized in new customized properties.

- **Open Vocabulary extension:** Add vocabulary in the field of cyber forensic investigations.

## Extension Format

- **CFOs:** We follow the STIX specification for [customizing objects](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_p2sz1mp7z524). The most important rule to create a new object type is that the value of the type property in a Custom Object SHOULD start with “x-” followed by a source unique identifier (like a domain name with dots replaced by hyphens), a hyphen and then the name. For example, x-example-com-customobject.
- **Custom Properties:** We follow the [doc](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_8072zpptza86).
- **Open Vocabulary extension:** We follow [open vocabulary extension](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_bnnxah80y7by). Values that are not from the suggested vocabulary SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.

## Properites of CFOs

- [Required Properties for all CFOs (CFDOs and CFOOs)](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_xzbicbtscatx)
  - **type** (string)： The value of this property MUST be one of CFOs.
  - **spec_version** (string): The current version is 2.1, i.e., **"spec_version": "2.1"**.
  - **id** (identifier): This id MUST meet the requirements of the identifier type [see STIX section 2.9](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_64yvzeku5a5c).
- Additional Required Properties for CFDOs
  - **created** (timestamp): The created property represents the time at which the object was originally created by an investigator (i.e., object creator).
  - **modified** (timestamp): The modified property is only used by CFOs that support versioning and represents the time that this particular version of the object was last modified.
  - **created_by_ref**(identifier): The object creator is the entity (e.g., system, organization, instance of a tool) that generates the id property for a given object. It is optional in STIX SDO.
- [Common Properties used in all CFOs](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_xzbicbtscatx)
  - **description** (string): A description that provides more details and context about the object.
  - **external_references** (list of type external-reference): The external_references property specifies a list of external references which refers to non-STIX information. This property is used to provide one or more URLs, descriptions, or IDs to records in other systems.

---

## Table of Contents (updating)

- Cyber Forensic Domain Objects (CFDOs)

  - [Windows Event Evidence Object](#Windows-Event-Evidence-Object)
  - [Webpage Visit Evidence Object](#Webpage-Visit-Evidence-Object)
  - [Plug and Play (PnP) Event Evidence Object](#Plug-and-Play-PnP-Event-Evidence-Object)
  - [File Visit Evidence Object](#File-Visit-Evidence-Object)
    - [RecentFileCache](#RecentFileCache)
    - [Shimcache](#Shimcache)
    - [UserAssist](#UserAssist)
    - [Prefetch](#Prefetch)
    - [USNJournal](#USNJournal)
    - [Shellbags](#Shellbags)
    - [Jumplist](#Jumplist)
    - [Lnk]($Lnk)
    - [RMU]($RMU)
    - [MFT]($MFT)
    - [AppLog](#AppLog)
  - [Tool State Evidence Object](#Tool-State-Evidence-Object)
  - [Disk Image Object](#Disk-Image-Object)
  - [Investigation Tool Object](#Investigation-Tool-Object)
  - [Action Object](#Action-Object)
  - [Timeline Object](#Timeline-Object)
  - [Scenario Object](#Scenario=Object)

- Cyber Forensic observable Objects (CFOOs)

  - [Disk Partition Object](#Disk-Partition-Object)
  - [Secondary Storage Object](#Secondary-Storage-Object)
  - [Computer Object](#Computer-Object)

- Property Extension
  - [Extension for Windows Registry Key Object](#Extension-for-Windows-Registry-Key-Object)
- Open Vocabulary extension
  - [threat-actor-type-ov extension](#threat-actor-type-ov-extension])
  - [ani-forensic-tool-type-ov](#tool-type-ov-extension)

## Windows Event Evidence Object

**Type Name:** x-windows-evt-evidence

A Windows Event Evidence object represents properties of an event, which is recorded by Windows OS.

### Properties

| Property Name        | Type       | Description                                                                                                                                                        |
| -------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| type (required)      | string     | The value of this property MUST be x-windows-evt-evidence.                                                                                                         |
| record_number        | string     | Specifies the number of the entry in a saved event log.                                                                                                            |
| time_generated       | timestamp  | Specifies the time at which this entry was submitted.                                                                                                              |
| time_written         | timestamp  | Specifies the time at which this entry was received by the service to be written to the log.                                                                       |
| event_generator      | string     | Specifies the name of the software (or the name of a subcomponent of the software if the software is large) that generates the event.                              |
| event_id             | integer    | The value is specific to the event source for the event, and is used with the source name to locate a description string in the message file for the event source. |
| event_id_string      | integer    | Specified the description string of event_id.                                                                                                                      |
| event_type           | string     | It MUST be one EventType defined in [Windows Doc](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-eventlogrecord)                                |
| source_ref(required) | identifier | Specifies object type that event object belongs to. It MUST be a type of file or artifact                                                                          |

Notes:

- event_source has a few types, such as application, security, system, customlog, etc.
- user_account_ref can be retrieved based on SID.

### Relationships

| Source                 | Relationship Type | Target           | Description                                                                                     |
| ---------------------- | ----------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| x-windows-evt-evidence | traced-back-to    | user-account     | This Relationship describes that a Windows Event Evidence can be traced back to a user-account. |
| x-windows-evt-evidence | extracted-from    | x-disk-partition | This Relationship describes that x-windows-evt-evidence is extracted from x-disk-partition.     |

### Example 1: describes a "logon" event recorded in the security event file.

```json
[
  {
    "type": "x-windows-evt-evidence",
    "spec_version": "2.1",
    "id": "x-windows-evt-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "record_number": "12145",
    "time_generated": "2015-01-06T20:03:00.000Z",
    "time_written": "2015-01-06T20:03:00.100Z",
    "event_generator": "Microsoft Windows security auditing.",
    "event_id": "4624",
    "event_id_string": "An account was successfully logged on",
    "event_type": "EVENTLOG_AUDIT_SUCCESS",
    "user_account_ref ": "user-account--0d5b424b-93b8-5cd8-ac36-306e1789d63c",
    "source_ref": "file--79e0da61-48e2-4552-874f-83d74262f39d",
    "created": "2021-01-06T20:03:00.000Z",
    "modified": "2021-01-06T20:03:00.000Z",
    "created_by_ref": "identity-704d9d08-060e-48f6-ace9-fde3eeb712ab",
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
  },
  {
    "type": "user-account",
    "spec_version": "2.1",
    "id": "user-account--0d5b424b-93b8-5cd8-ac36-306e1789d63c",
    "user_id": "1001",
    "account_login": "jdoe",
    "account_type": "Windows",
    "display_name": "John Doe",
    "is_service_account": false,
    "is_privileged": false,
    "can_escalate_privs": true,
    "account_created": "2016-01-20T12:31:12Z",
    "credential_last_changed": "2016-01-20T14:27:43Z",
    "account_first_login": "2016-01-20T14:26:07Z",
    "account_last_login": "2016-07-22T16:08:28Z"
  },
  {
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--014841f8-eb38-4673-9904-70f67c92dd8b",
    "created": "2020-01-16T18:52:24.277Z",
    "modified": "2020-01-16T18:52:24.277Z",
    "relationship_type": "traced-back-to",
    "source_ref": "x-windows-evt-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "target_ref": "user-account--0d5b424b-93b8-5cd8-ac36-306e1789d63c"
  }
]
```

### Example 2: describes a system event generated by CD-Rom

```json
{
  "type": "x-windows-evt-evidence",
  "spec_version": "2.1",
  "id": "x-windows-evt-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "record_number": "4512",
  "time_generated": "2015-01-06T20:03:00.000Z",
  "time_written": "2015-01-06T20:03:00.100Z",
  "event_generator": "cdrom",
  "event_id": "16388",
  "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
  "source_ref": "file--79e0da61-48e2-4552-874f-83d74262f39d",
  "created": "2021-01-06T20:03:00.000Z",
  "modified": "2021-01-06T20:03:00.000Z",
  "source_ref": "file--e2dd9934-e6aa-440a-9d51-21ccf990c4f5",
  "created_by_ref": "identity-704d9d08-060e-48f6-ace9-fde3eeb712ab"
}
```

## Webpage Visit Evidence Object

**Type Name:** x-webpage-visit-evidence

A Webpage Visit Evidence object represents a visit to a webpage.

### Properties

| Property Name        | Type       | Description                                                                                |
| -------------------- | ---------- | ------------------------------------------------------------------------------------------ |
| type (required)      | string     | The value of this property MUST be x-webpage-visit-evidence.                               |
| record_number        | string     | Specifies the unique entry ID in a file (i.e., save_to_ref) that the event saved to.       |
| url_ref              | identifier | Specify a visit to a URL.                                                                  |
| title                | string     | Specifies the title of a web page (if a URL is a webpage) that has been visited.           |
| visit_time           | timestamp  | The last time visited.                                                                     |
| visit_count          | integer    | The number of times visited                                                                |
| browser_ref          | identifier | The value type for this property SHOULD software.                                          |
| file_requested_ref   | identifier | The ID of the file the HTTP requested.                                                     |
| source_ref(required) | identifier | Specifies object type that event object belongs to. It MUST be a type of file or artifact. |

### Relationships

| Source                   | Relationship Type | Target           | Description                                                                                                |
| ------------------------ | ----------------- | ---------------- | ---------------------------------------------------------------------------------------------------------- |
| x-webpage-visit-evidence | traced-back-to    | user-account     | This Relationship describes that a webpage visit evidence can be traced back to a user-account.            |
| x-webpage-visit-evidence | extracted-from    | x-disk-partition | This Relationship describes that a piece of x-webpage-visit-evidence is extracted from a x-disk-partition. |

### Examples

```json
[
  {
    "type": "x-webpage-visit-evidence",
    "spec_version": "2.1",
    "id": "x-webpage-visit-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "url_ref": "url--9cc5a5dc-0acd-46f5-ae3f-724370087622",
    "title": "B.S. in Cyber Forensics | University of Baltimore",
    "visit-time": "2021-01-06T20:03:22.000Z",
    "visit-count": 2,
    "browser_ref": "software--b67a8d52-d438-4ace-8285-c6d485e34192",
    "file_requested_ref ": "file--10624790-0e43-4498-89da-8979ab4215ae",
    "source_ref": "file--843f6a43-0603-4e0d-84a4-198386eecf4f",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2014-04-06T20:03:00.000Z",
    "modified": "2014-04-06T20:03:00.000Z"
  },
  {
    "type": "url",
    "spec_version": "2.1",
    "id": "url--9cc5a5dc-0acd-46f5-ae3f-724370087622",
    "value": "https://www.ubalt.edu/cpa/undergraduate-majors-and-minors/majors/cyber-forensics/"
  },
  {
    "type": "software",
    "spec_version": "2.1",
    "id": "software--b67a8d52-d438-4ace-8285-c6d485e34192",
    "name": "chrome",
    "cpe": "cpe:2.3:a:google:chrome:88.0.4324.104:*:*:*:*:*:*:*",
    "vendor": "Google"
  },
  {
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--014841f8-eb38-4673-9904-70f67c92dd8b",
    "created": "2020-01-16T18:52:24.277Z",
    "modified": "2020-01-16T18:52:24.277Z",
    "relationship_type": "traced-back-to",
    "source_ref": "x-webpage-visit-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "target_ref": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb"
  }
]
```

## Plug and Play (PnP) Event Evidence Object

**Type Name:** x-pnp-evt-evidence

The Plug and Play (PnP) Event Evidence object represents an event recorded by Windows Kernel-Mode Plug (pnp) and Play Manager. PnP manager is a combination of hardware technology and software techniques that enables a PC to recognize when a device is added to the system. With PnP, the system configuration can change with little or no input from the user. installation events are logged in SetupAPI.dev.log.

### Properties

The completed log properties can be accessed [Microsoft office docs- Format of a text log section body](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/format-of-a-text-log-section-body)

| Property Name        | Type       | Description                                                                                                                                                    |
| -------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type (required)      | string     | The value of this property MUST be x-pnp-evt-evidence.                                                                                                         |
| message_type         | enum       | The values of this property MUST come from the x-pnp-message-type-enum enumeration.                                                                            |
| time_generated       | timestamp  | Specified the time at which this entry was submitted.                                                                                                          |
| time_written         | timestamp  | Specified the time at which this entry was received by the service to be written to the log.                                                                   |
| event_category       | string     | Indicates the category of SetupAPI operation that made the log entry. MUST be one of the predefined event_category operation strings, e.g.device installation. |
| formatted_message    | string     | Contains the specific information that applies to the log entry.                                                                                               |
| source_ref(required) | identifier | Specifies object type that event object belongs to. It MUST be a type of file or artifact (e.g., cache, memory), e.g., steupAPI.log                            |

### Message Type Vocabulary

Vocabulary Name: x-pnp-message-type-enum

| Vocabulary Value | Description                                                          |
| ---------------- | -------------------------------------------------------------------- |
| error            | An Error message                                                     |
| warning          | An warning message                                                   |
| other-info       | Information message other than an error message or a warning message |

### Relationships

| Source             | Relationship Type | Target           | Description                                                                                          |
| ------------------ | ----------------- | ---------------- | ---------------------------------------------------------------------------------------------------- |
| x-pnp-evt-evidence | traced-back-to    | user-account     | This Relationship describes that a pnp event evidence can be traced back to a user-account.          |
| x-pnp-evt-evidence | extracted-from    | x-disk-partition | This Relationship describes that a piece of x-pnp-evt-evidence is extracted from a x-disk-partition. |

### Examples

```json
{
  "type": "x-pnp-evt-evidence",
  "spec_version": "2.1",
  "id": "x-pnp-evt-evidence--58959aae-d1e0-4e12-a879-270efe33c6e3",
  "message_type": "other-info",
  "time_written": "2021-01-06T20:03:22.000Z",
  "event_category": "device installation",
  "formatted_message ": "Device Install (Hardware initiated) - USB\\VID_0781&PID_5517\\4C5300124505311010593",
  "source_ref": "file--176353bd-b61d-4944-b0cd-0b98783c50b5",
  "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
  "created": "2014-04-06T20:03:00.000Z",
  "modified": "2014-04-06T20:03:00.000Z",
  "external_references": [
    {
      "source_name": " event_category and SetupAPI operation",
      "url": "https://docs.microsoft.com/en-us/windows-hardware/drivers/install/format-of-a-text-log-section-body"
    }
  ]
}
```

## File Visit Evidence Object

**Type Name:** x-file-visit-evidence

A File Visit object represents properties that are associated with a file/directory/network directory visit (for various reasons) performed by operating systems or applications. The operation to the file during the visit can be read, create, etc. The visit may be saved in different forms, e.g., file, cache, Windows registry, etc.

### Properties

| Property Name               | Type       | Description                                                                                                          |
| --------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| type (required)             | string     | The value of this property MUST be x-file-visit-evidence.                                                            |
| op                          | enum       | Specifies how the file was visited. The values of this property MUST come from the x-file-visit-op-enum enumeration. |
| visit_time                  | timestamp  | Specifies the time a file was visited.                                                                               |
| visitor_ref                 | identifier | Specifier the a visitor, e.g., software or software components, who visited a file.                                  |
| visit_count                 | integer    | The total number of times the program has visited.                                                                   |
| record_reason               | enum       | Specifies a main reasons why a software records the visit. It MUST come from the x-file-visit-record-reason-enum.    |
| file_visited_ref (required) | identifier | Specifies a file or directory that was recently visited.                                                             |
| source_ref(required)        | identifier | Specifies the destination (e.g., file, registry, artifact, or directory) the record was saved to.                    |
| common_name                 | open-vocab | Specifies the evidence name that is commonly referred by investigators. It MUST from x-file-visit-common-name-ov.    |

### File Visit Operation Enum

**Vocabulary Name**: x-file-visit-op-enum

| Vocabulary Value | Description                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| create           | A file was visited for creation.                                                         |
| read             | A file was visited for reading.                                                          |
| modify           | A file was visited for modification (content is to be modified).                         |
| update           | The metadata of a file was visited for changing (e.g. permissions)                       |
| execute          | A file was visited for execution.                                                        |
| delete           | A file was visited for deletion.                                                         |
| preload          | A file was visited for preloading to memory.                                             |
| prefetch         | A file was visited for prefetching to memory.                                            |
| load             | A file was visited for loading to memory.                                                |
| unload           | A file was visited for unloading from memory.                                            |
| other            |                                                                                          |
| unknown          | There is not enough information available to determine how file was or will be accessed. |

### File Visit Record Reason Enum

**Vocabulary Name:** x-file-visit-record-reason-enum

| Vocabulary Value | Description                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------- |
| functionality    | To support functionalities of a software, e.g., mft,                                                                        |
| security         | To protect systems from attacks.                                                                                            |
| accountability   | The obligation imposed by law or regulations to keep systems explainable by keeping accurate record of internal activities. |
| maintainability  | To support the maintainability of a system.                                                                                 |
| reliability      | The quality of being reliable, dependable or trustworthy, e.g., data recovery ($logFile) and backup (usnjournal).           |
| scalability      | To support the scalability of the system.                                                                                   |
| performance      | For fast service, often including using cache, e.g., recentfilecache, prefetch                                              |
| usability        | For easy to use, e.g., userassist, muicache, shellbag, jumplist, mru                                                        |
| reusability      | To improve reusability of a system.                                                                                         |
| compatibility    | To identify and fix application compatibility or portability issues, e.g., shimcache.                                       |
| history          | Not for specific reasons, just logging key activities of a software.                                                        |

### File Visit Common Name Vocabulary

**Vocabulary Name:** x-file-visit-common-name-ov

| Term            | Description                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| userassist      | Track every GUI-based programs launched from the desktop in the userassist registry key.              |
| shimcache       | Shimcache is created to identify application compatibility issues.                                    |
| recentfilecache | RecentFileCache.bcf only contains references to programs that recently executed.                      |
| prefetch        |                                                                                                       |
| muicache        | Support multiple languages for software.                                                              |
| usnjournal      | Store Update Sequence Number Journal.                                                                 |
| shellbag        | Store user preferences for GUI folder display within Windows Explorer.                                |
| jumplist        | Represents a list of items and tasks displayed as a menu on a Windows 7 taskbar button.               |
| mru             | Most recently used files.                                                                             |
| autorun         |                                                                                                       |
| mft             | Master file table for file management.                                                                |
| bam             | Background Activity Moderator is a Windows service that Controls activity of background applications. |
| applog          | Application logs.                                                                                     |

### Relationships

| Source                | Relationship Type | Target           | Description                                                                                            |
| --------------------- | ----------------- | ---------------- | ------------------------------------------------------------------------------------------------------ |
| x-file-visit-evidence | traced-back-to    | user-account     | This Relationship describes that a file visit evidence can be traced back to a user-account.           |
| x-file-visit-evidence | extracted-from    | x-disk-partition | This Relationship describes that a piece ofx-file-visit-evidence is extracted from a x-disk-partition. |

### RecentFileCache

RecentFileCache.bcf only contains references to programs that were recently executed. setuputility.exe is recently executed.

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--83aee86d-1523-4111-938e-8edc8a6c804f",
    "op": "execute",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "file--7bd8980c-91eb-461a-a357-ae75a35374e6",
    "record_reason": "performance",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "file--176353bd-b61d-4944-b0cd-0b98783c50b5",
    "common_name": "recentfilecache",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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
  },
  {
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--014841f8-eb38-4673-9904-70f67c92dd8b",
    "created": "2020-01-16T18:52:24.277Z",
    "modified": "2020-01-16T18:52:24.277Z",
    "relationship_type": "traced-back-to",
    "source_ref": "x-file-visit-evidence--83aee86d-1523-4111-938e-8edc8a6c804f",
    "target_ref": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb"
  }
]
```

### Shimcache

Shimcache is created to identify application compatibility issues. Two actions/events that can cause the Shimcache to record an entry:
(1) A file is executed and (2) A user interactively browses (read) a directory.

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--83aee86d-1523-4111-938e-8edc8a6c804f",
    "op": "execute",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "file--7bd8980c-91eb-461a-a357-ae75a35374e6",
    "record_reason": "compatibility",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "windows-registry-key--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "common_name": "shimcache",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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
    "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Session Manager\\AppCompatCache"
  }
]
```

### UserAssist

Windows System, every GUI-based programs launched from the desktop are tracked in this registry key HKEY_USERS\{SID}\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist.
An Example of a Security ID (SID) is S-1-5-21-394942887-4226445097-2438273937-1001.

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "op": "execute",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_count": 1,
    "file_visited_ref ": "file--150c4200-02c6-475d-ac44-2d4e65de9f36",
    "record_reason": "usability",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "windows-registry-key--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "common_name": "userassist",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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

Prefetch preloads the most frequently used software into memory. The Typeshows the chrome.exe-999b1ba.pf contains chrome.exe-999b1ba.exe, the time when the executable file is executed, last time executed, and how many times it was executed.

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--116964e0-56c8-42ef-850c-9b84e4fc6b4f",
    "op": "execute",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "visit_count": 71,
    "file_visited_ref ": "file--150c4200-02c6-475d-ac44-2d4e65de9f36",
    "record_reason": "performance",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "file--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "common_name": "prefetch",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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

USN (Update Sequence Number) Journal records all files' changes (e.g.., rename) that are made to a volume.

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "op": "modify",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "file--150c4200-02c6-475d-ac44-2d4e65de9f36",
    "record_reason": "reliability",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "file--2ba37ae7-2745-5082-9dfd-9486dad41016",
    "common_name": "usnjournal",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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
    "name": "$UsnJrnl"
  }
]
```

### Shellbags

Windows uses the Shellbag keys to store user preferences for GUI folder display within Windows Explorer to improve user experience and “remember” preferences. The following Type describes a USB drive is attached/visited.

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--36e6b5d9-f04e-45f0-90fd-ead11a3069a6",
    "op": "read",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "directory--28d2e12c-c56c-4aaf-aeed-d0b69ccc601c",
    "record_reason": "performance",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "windows-registry-key--14a4a46c-0957-4b9d-900d-35cb8379055c",
    "common_name": "shellbag",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
  },
  {
    "type": "directory",
    "spec_version": "2.1",
    "id": "directory--28d2e12c-c56c-4aaf-aeed-d0b69ccc601c",
    "name": "My Computer\\E:\\"
  },
  {
    "type": "windows-registry-key",
    "spec_version": "2.1",
    "id": "windows-registry-key--14a4a46c-0957-4b9d-900d-35cb8379055c",
    "key": "HKEY_CLASS_ROOT\\HKEY_CLASSES_ROOT\\Local Settings\\Software\\Microsoft\\Windows\\Shell"
  }
]
```

### Jumplist

Jumplist represents a list of items and tasks displayed as a menu on a Windows 7 taskbar button. The following Type shows a Jumplist of Word 2010 Pinned and Recent accessed files.

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--2bec785c-e1b0-4834-9a3a-9d04bd0749fe",
    "op": "read",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "file--28d2e12c-c56c-4aaf-aeed-d0b69ccc601c",
    "record_reason": "performance",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "windows-registry-key--14a4a46c-0957-4b9d-900d-35cb8379055c",
    "common_name": "jumplist",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--ac69c037-c578-4c5e-ad6a-23d53a0b1d6e",
    "op": "read",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "file-8c33da4c-fb61-4658-b28c-a5c60f561d78",
    "record_reason": "usability",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "file--676b743a-3a56-4084-aeb5-fa9cfadf5663",
    "common_name": "lnk",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--8cdbf030-89d9-48be-b733-5f4900706f0e",
    "op": "read",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "file-8c33da4c-fb61-4658-b28c-a5c60f561d78",
    "record_reason": "usability",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "file--676b743a-3a56-4084-aeb5-fa9cfadf5663",
    "common_name": "rmu",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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

A desktop.ini in MFT

```json
[
  {
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--9880e636-38b0-471a-8266-8a622a95b3a5",
    "op": "other",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref": "file-f7d4aa7a-d02c-481e-8bdc-450cb0669b5d",
    "record_reason": "functionality",
    "visitor_ref": "software--a67ca75e-bda5-45e0-8bf0-b5884528d228",
    "source_ref": "file--19be1a16-4b87-4fc4-b056-dc9e0389d4bd",
    "common_name": "mft",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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
    "type": "x-file-visit-evidence",
    "spec_version": "2.1",
    "id": "x-file-visit-evidence--a2b48cc8-aaba-429f-9c1f-bcf1dbf3ada2",
    "op": "delete",
    "visit_time ": "2021-01-06T20:03:22.000Z",
    "file_visited_ref ": "file-8cdbf030-89d9-48be-b733-5f4900706f0e",
    "record_reason": "functionality",
    "visitor_ref": "software--764c3bcd-e053-46dc-b77d-51de1a311b39",
    "source_ref": "file--d5faf70b-36b8-437c-9137-6c0fc83b1e69",
    "common_name": "applog",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
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

## Tool State Evidence Object

**Type Name:** x-tool-state-evidence

The Tool State Evidence object represents an attacking (anti-forensic) tool's state at a specific time, including downloading, installing, running, uninstalling, cleaning. Each state is exclusive.

### Properties

| Property Name    | Type       | Description                                                                                                                             |
| ---------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| type (required)  | string     | The value of this property MUST be x-tool-state-evidence.                                                                               |
| state            | enum       | Specifies a state of tool. It MUST come from x-tool-state-enum enumeration.                                                             |
| enter_state_time | timestamp  | Specifies the time a tool entering the state.                                                                                           |
| exit_state_time  | timestamp  | Specifies the time a tool existing the state.                                                                                           |
| tool_ref         | identifier | An ID reference to a Tool object. If the tool is an anti-forensics tool, the type of the tool MUST come from ani-forenisc-tool-type-ov. |

### Relationships

| Source                | Relationship Type | Target           | Description                                                                                             |
| --------------------- | ----------------- | ---------------- | ------------------------------------------------------------------------------------------------------- |
| x-tool-state-evidence | traced-back-to    | user-account     | This Relationship describes that a tool state evidence can be traced back to a user-account.            |
| x-tool-state-evidence | extracted-from    | x-disk-partition | This Relationship describes that a piece of x-tool-state-evidence is extracted from a x-disk-partition. |

### Tool State Enumeration

**Enumeration Name**: x-tool-state-enum

| Vocabulary Value | Description                                             |
| ---------------- | ------------------------------------------------------- |
| downloading      | A tool was downloading                                  |
| installing       | A tool was installing                                   |
| running          |                                                         |
| uninstalling     |                                                         |
| cleaning         | All files that are related to the tool has been removed |

### Example: describes a system event generated by CD-Rom

```json
[
  {
    "type": "x-tool-state-evidence",
    "spec_version": "2.1",
    "id": "x-tool-state-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "state": "installing",
    "exit_state_time": "2005-02-06T20:03:00.000Z",
    "created": "2021-01-06T20:03:00.000Z",
    "modified": "2021-01-06T20:03:00.000Z",
    "created_by_ref": "identity-704d9d08-060e-48f6-ace9-fde3eeb712ab"
  },

  {
    "type": "tool",
    "spec_version": "2.1",
    "id": "tool--4d82bd3e-24a3-4f9d-b8f3-b57267fe06a9",
    "created": "2015-05-15T09:12:16.432Z",
    "modified": "2015-05-15T09:12:16.432Z",
    "name": "steghide",
    "tool_types": ["steganography"],
    "tool_version": "0.5.1",
    "description": "steganography",
    "external_references": [
      {
        "source_name": "steghide",
        "url": "http://steghide.sourceforge.net/"
      }
    ]
  }
]
```

## Disk Image Object

**Type Name:** x-disk-image

[A disk image](https://en.wikipedia.org/wiki/Disk_image), in computing, is a computer file containing the contents and structure of a disk volume or of an entire data storage device, such as a hard disk drive, tape drive, floppy disk, optical disc, or USB flash drive.

### Disk Image Specific Properties

| Property Name           | Type                          | Description                                                                |
| ----------------------- | ----------------------------- | -------------------------------------------------------------------------- |
| type (required)         | string                        | The value of this property MUST be x-disk-image.                           |
| image_id                | string                        | Specifies an id of a disk image.                                           |
| description             | string                        | Specifies the description of a disk image.                                 |
| partitions              | list of type x-disk-partition | Specifies a list of partitions that an disk image contains.                |
| acquired_on             | timestamp                     | Specifies the time the image was acquired.                                 |
| format                  | open-vocab                    | Specifies the disk image format. It MUST come from x-disk-image-format-ov. |
| acquired_using_tool_ref | identifier                    | Specifies the software that creates the disk image.                        |
| acquired_by_ref         | identifier                    | Specifies the person that create a disk image.                             |
| image_file_ref          | identifier                    | Specifies a image file.                                                    |

### Relationships

| Source       | Relationship Type | Target           | Description                                                                    |
| ------------ | ----------------- | ---------------- | ------------------------------------------------------------------------------ |
| x-disk-image | image-of          | x-crime-case     | This Relationship describes that a disk image is an image of x-crime-case.     |
| x-disk-image | image-of          | x-secondary-disk | This Relationship describes that a disk image is an image of x-secondary-disk. |

### Disk Image Format Vocabulary

**Vocabulary Name:** x-disk-image-format-ov

| Vocabulary Value | Description                                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| e01              | Encase Evidence image file format                                                                                                |
| dd               | A bit-of-bit copy of the raw data file                                                                                           |
| lef              | Encase Logical Evidence files                                                                                                    |
| zip              | It is an archival forensic image file format that supports lossless data compression without losing the originality of the data. |
| dmg              | A disk image file that is generally created by the Apple Mac OS X.                                                               |

### Examples

```json
[
  {
    "type": "x-disk-image",
    "spec_version": "2.1",
    "id": "x-disk-image-evidence--87a3e4ee-102c-4cc9-9017-96089a0e0680",
    "partitions": [
      "x-disk-partition--c65a985d-dc31-441e-840b-54381cef4e31",
      "x-disk-partition--9bc65596-8fa7-441c-b5a1-71a43d46b221"
    ],
    "acquired_on": "2021-01-06T20:03:22.000Z",
    "format": "dd",
    "image_file_ref": "file--6e735550-51e8-483a-b0d6-29d6ff5cfbf3",
    "acquired_by_ref": "identity--b9babea0-63eb-4981-8e6d-f6603cf7e46a",
    "acquired_using_tool_ref": "x-investigation-tool--0a5b5f22-ba62-42f1-9d74-a94e87f4b45c",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
  },
  {
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--014841f8-eb38-4673-9904-70f67c92dd8b",
    "created": "2020-01-16T18:52:24.277Z",
    "modified": "2020-01-16T18:52:24.277Z",
    "relationship_type": "image-of",
    "source_ref": "x-disk-image--87a3e4ee-102c-4cc9-9017-96089a0e0680",
    "target_ref": "x-crime-case--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb"
  }
]
```

## Investigation Tool Object

**Type Name:** x-investigation-tool

Investigation Tools are software that can be used by cyber investigators to perform digital forensic investigations. This CFO MUST NOT be used to characterize malware and SDO tools.

### Investigation Tool Specific Properties

| Property Name   | Type                    | Description                                                                                     |
| --------------- | ----------------------- | ----------------------------------------------------------------------------------------------- |
| type (required) | string                  | The value of this property MUST be x-investigation-tool.                                        |
| last_modified   | timestamps              | The last modified date of the investigation tool.                                               |
| description     | string                  | A description that provides more details and context about the investigation tool.              |
| tool_types      | list of type open-vocab | The values for this property SHOULD come from the x-investigation-tool-type-ov open vocabulary. |
| aliases         | list of type string     | Alternative names used to identify this investigation tool.                                     |
| tool_version    | string                  | The version identifier associated with the investigation tool.                                  |
| software_ref    | identifier              | Specifier the software product (if CPE or SWID is known) used as the investigation tool.        |

## Investigation Tool Type Vocabulary

**Vocabulary Name:** x-investigation-tool-type-ov
Investigation Tool Type is an open vocabulary that describes the type of tools used for cyber investigations. It doesn't include common software, such as MS Office, database, etc.

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

## Action Object

**Type Name:** x-action

An action is one cyber criminal activity performed under a user account.

## Action Specific Properties

| Property Name   | Type                    | Description                                                              |
| --------------- | ----------------------- | ------------------------------------------------------------------------ |
| type (required) | string                  | The value of this property MUST be x-action.                             |
| name            | string                  | Specifies the name of an action.                                         |
| description     | string                  | A description that provides more details and context about the Action.   |
| performed_time  | timestamp               | Specified the time that performed an action.                             |
| note            | string                  | Additional note that describes an action.                                |
| evidence_refs   | list of type identifier | Specifies a list of evidence objects that are associated with an action. |

### Relationships

| Source   | Relationship Type | Target       | Description                                                                |
| -------- | ----------------- | ------------ | -------------------------------------------------------------------------- |
| x-action | traced-back-to    | user-account | This Relationship describes that an action is traced-back-to user-account. |

## Example: An action that search for anti-forensics tools

```json
[
  {
    "type": "x-action",
    "spec_version": "2.1",
    "id": "x-action--87a3e4ee-102c-4cc9-9017-96089a0e0680",
    "name": "Search anti-forensic tool online",
    "description": "Search application online using IE",
    "performed_time ": "2015-25-25T14:46:44:44Z",
    "evidence_refs": [
      "x-webpage-visit-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f"
    ],
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
  },
  {
    "type": "x-webpage-visit-evidence",
    "spec_version": "2.1",
    "id": "x-webpage-visit-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "url_ref": "url--9cc5a5dc-0acd-46f5-ae3f-724370087622",
    "visit-time": "2015-25-25T14:46:44:44Z",
    "visit-count": 2,
    "browser_ref": "software--b67a8d52-d438-4ace-8285-c6d485e34192",
    "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
    "source_ref": "file--843f6a43-0603-4e0d-84a4-198386eecf4f",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2014-04-06T20:03:00.000Z",
    "modified": "2014-04-06T20:03:00.000Z"
  },
  {
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--014841f8-eb38-4673-9904-70f67c92dd8b",
    "created": "2020-01-16T18:52:24.277Z",
    "modified": "2020-01-16T18:52:24.277Z",
    "relationship_type": "traced-back-to",
    "source_ref": "x-action--87a3e4ee-102c-4cc9-9017-96089a0e0680",
    "target_ref": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb"
  }
]
```

## Example: Install ccleaner tool

```json
{
  "type": "x-action",
  "spec_version": "2.1",
  "id": "x-action--87a3e4ee-102c-4cc9-9017-96089a0e0680",
  "name": "Install ccleaner tool",
  "description": "Install ccleaner anti-forensic tool",
  "performed_time ": "2015-25-25T14:46:44:44Z",
  "evidence_refs": [
    "x-tool-state-evidence--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "x-file-visit-evidence--83aee86d-1523-4111-938e-8edc8a6c804f"
  ],
  "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
  "created": "2021-04-06T20:03:00.000Z",
  "modified": "2021-04-06T20:03:00.000Z"
}
```

# Timeline Object

**Type Name:** x-timeline

A Timeline object describes a specific cybercrime scenario that is represented by a sequence of actions performed by a threat-actor.

## Timeline Specific Properties

| Property Name      | Type                  | Description                                                            |
| ------------------ | --------------------- | ---------------------------------------------------------------------- |
| type (required)    | string                | The value of this property MUST be x-timeline.                         |
| actions            | list of type x-action | Specifies a list of actions in chronological order.                    |
| name               | string                | Specifies the name of a timeline.                                      |
| description        | string                | A description that provides more details and context about a timeline. |
| reconstructed_from | identifier            | Specifies timeline is reconstructed from a crime case.                 |
| reconstructed_by   | identifier            | Specifies timeline is reconstructed by an identity.                    |

### Relationships

| Source     | Relationship Type | Target       | Description                                                                 |
| ---------- | ----------------- | ------------ | --------------------------------------------------------------------------- |
| x-timeline | traced-back-to    | user-account | This Relationship describes that a timeline is traced-back-to user-account. |

## Example: data leakage using a UBS

```json
[
  {
    "type": "x-timeline",
    "spec_version": "2.1",
    "id": "x-timeline--5e54d8e8-1c4b-4a16-bb1b-7ab2acb06fff",
    "name": "data leakage using a UBS",
    "description": "An threat actor uses a USB to transfer files.",
    "actions": [
      "x-action--6ba0fce7-1ff9-44a4-9fbb-28760afc7827",
      "x-action--83aee86d-1523-4111-938e-8edc8a6c804f"
    ],
    "reconstructed_from": "x-crime-case--49aadd9f-8bb0-4728-bd56-7bc708714516",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
  },
  {
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--6598bf44-1c10-4218-af9f-75b5b71c23a7",
    "created": "2021-05-15T09:12:16.432Z",
    "modified": "2021-05-15T09:12:16.432Z",
    "relationship_type": "traced-back-to ",
    "source_ref": "x-timeline--5e54d8e8-1c4b-4a16-bb1b-7ab2acb06fff",
    "target_ref": "user-account-2485b844-4efe-4343-84c8-eb33312dd56f"
  }
]
```

# Crime Case Object

**Type Name:** x-crime-case

A Crime Case object represents a background description of a potential cybercrime case given to a cyber forensics investigator. Note that a crime case may consist of multiple scanarios.

## Crime Case Properties

| Property Name   | Type                    | Description                                                                 |
| --------------- | ----------------------- | --------------------------------------------------------------------------- |
| type (required) | string                  | The value of this property MUST be x-crime-case.                            |
| case_id         | string                  | Specifies a case identifier that is assigned to a case.                     |
| name            | string                  | Specifies the name of a case.                                               |
| description     | string                  | A description that provides more details and context about a case.          |
| disk_images     | list of type disk_image | Specifies a list of dis_images that are associated with a crime case.       |
| case_file_refs  | list of type file       | Specifies docs (other than disk images) that are associated with the cases. |

### Relationships

| Source       | Relationship Type | Target       | Description                                                                 |
| ------------ | ----------------- | ------------ | --------------------------------------------------------------------------- |
| x-crime-case | assigned-to       | identity     | This Relationship describes that the investigator was assigned to the case. |
| x-crime-case | has               | threat-actor | This Relationship describes that a x-crime-case has a threat-actor.         |

## Example: NIST data leakage case

```json
[
  {
    "type": "x-crime-case",
    "spec_version": "2.1",
    "id": "x-crime-case--5e54d8e8-1c4b-4a16-bb1b-7ab2acb06fff",
    "name": "NIST data leakage",
    "description": "The case study is provided by NIST.",
    "disk_images": [
      "x-disk-image--64da9550-6f78-4f2f-99dc-4693cf719338",
      "x-disk_image--2a9f86c9-602b-43e3-bd2a-542b7544ce3e"
    ],
    "case_file_refs": "[file--6ba0fce7-1ff9-44a4-9fbb-28760afc7827, file--83aee86d-1523-4111-938e-8edc8a6c804f]",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2021-04-06T20:03:00.000Z",
    "modified": "2021-04-06T20:03:00.000Z"
  },
  {
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--6598bf44-1c10-4218-af9f-75b5b71c23a7",
    "created": "2021-05-15T09:12:16.432Z",
    "modified": "2021-05-15T09:12:16.432Z",
    "relationship_type": "has",
    "source_ref": "x-timeline--5e54d8e8-1c4b-4a16-bb1b-7ab2acb06fff",
    "target_ref": "threat-actor-2485b844-4efe-4343-84c8-eb33312dd56f"
  }
]
```

---

## Disk Partition Object

**Type Name:** x-disk-partition

[Disk partitioning](https://en.wikipedia.org/wiki/Disk_partitioning) or disk slicing is the creation of one or more regions on secondary storage, so that each region can be managed separately. A Disk Partition object specifies the properties that are associated with the disk segment.

### ID Contributing Properties

- volume_serial_number

### Disk partition Specific Properties

| Property Name        | Type    | Description                                                                                                                  |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| type (required)      | string  | The value of this property MUST be x-disk-partition.                                                                         |
| partition_seq_num    | integer | Specifies the sequence number the a partition.                                                                               |
| start_sector         | integer | Specifies the start sector of the partition.                                                                                 |
| end_sector           | integer | Specifies the end sector of the partition.                                                                                   |
| bytes_per_sector     | integer | Specifies the number of bytes per sector.                                                                                    |
| is_bootable          | boolean | Specifies if a partition is bootable.                                                                                        |
| volume_serial_number | string  | Specifies the serial number of a partition.                                                                                  |
| partition_type       | string  | Specifies the type of a partition. It MUST come from a x-disk-partition-type-ov open vocabulary.                             |
| file_sys_type        | string  | Specifies the type of a file system. It MUST come from the [list](https://en.wikipedia.org/wiki/Comparison_of_file_systems). |
| drive_letter         | string  | Specifies the drive letter of the partition, e.g., "C", "D", "E", etc.                                                       |
| label                | string  | Specifies the label/volume name of the partition, e.g., "backup".                                                            |

### Relationships

| Source           | Relationship Type | Target       | Description                                                        |
| ---------------- | ----------------- | ------------ | ------------------------------------------------------------------ |
| x-disk-partition | part-of           | x-disk-image | This relationship describes that a disk is a part of a disk image. |

### Partition Type Vocabulary

Vocabulary Name: x-disk-partition-type-ov

| Vocabulary Value | Description                            |
| ---------------- | -------------------------------------- |
| doc              | DOS Partition Table                    |
| mac              | MAC Partition Map                      |
| bsd              | BSD Disk Label                         |
| sun              | Sun Volume Table of Contents (Solaris) |
| gpt              | GUID Partition Table (EFI)             |

### Example

Specify a partition with NTFS

```json
{
  "type": "x-disk",
  "spec_version": "2.1",
  "id": "x-disk--ac6e29f1-aa84-4066-961b-9e1f42acab8f",
  "partition_seq_num": 2,
  "start_sector": 512,
  "end_sector": 206848,
  "bytes_per_sector": 512,
  "is_bootable": false,
  "volume_serial_number": "c8ca0c8dca0c7a48",
  "partition_type": "dos",
  "file_sys_type ": "ntfs",
  "drive_letter  ": "C",
  "part-of": "x-disk-image-42eaa6d5-93ad-46f0-95f2-8343094abe52"
}
```

## Secondary Storage Object

**Type Name:** x-secondary-Storage

A Secondary Storage object represents a non-volatile and long-term storage.

### Secondary Storage Specific Properties

| Property Name   | Type       | Description                                                                                                            |
| --------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| type (required) | string     | The value of this property MUST be x-secondary-Storage.                                                                |
| manufacturer    | string     | Specifies the manufacturer of a secondary storage.                                                                     |
| brand           | string     | Specifies the brand of a secondary storage, e.g., "SanDisk".                                                           |
| model           | string     | Specifies the model of a secondary storage.                                                                            |
| serial_number   | string     | Specifies the serial number of a secondary storage.                                                                    |
| type            | open-vocab | Specifies the type of secondary storage. The value for this property SHOULD come from the x-secondary-Storage-type-ov. |
| size            | integer    | Specifies the size of a secondary storage in MB.                                                                       |

### ID Contributing Properties

- serial_number

### Secondary Storage Type Vocabulary

Vocabulary Name: x-secondary-Storage-type-ov

| Vocabulary Value | Description                        |
| ---------------- | ---------------------------------- |
| hdd              | Hard disk drives                   |
| ssd              | Solid State Drive                  |
| hhdd             | Laptop-use hybrid hard disk drives |
| emmc             | Embedded Multimedia Card           |
| usb              | USB flash drive                    |
| cd               | One of optical discs               |
| dvd              | One of optical discs               |
| tape             |                                    |

### Relationships

| Source | Relationship Type | Target | Description |
| ------ | ----------------- | ------ | ----------- |

### Example

Specify a partition with NTFS

```json
{
  "type": "x-secondary-storage",
  "spec_version": "2.1",
  "id": "x-secondary-storage--096e9478-2b7b-5bc9-a035-08464b16fc7b",
  "serial_number": "0000000012400917BA30",
  "brand": "SanDisk",
  "type": "hdd",
  "size": 20000,
  "drive_letter  ": "C"
}
```

## Computer Object

**Type Name:** x-computer

[A computer](https://en.wikipedia.org/wiki/Computer) is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. Modern computers have the ability to follow generalized sets of operations, called programs.

### ID Contributing Properties

- serial_number
- cpu

### Disk partition Specific Properties

| Property Name          | Type                        | Description                                                                                                                  |
| ---------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| type (required)        | string                      | The value of this property MUST be x-computer.                                                                               |
| serial_number          | string                      | Specifies the serial number of a computer.                                                                                   |
| type                   | string                      | Specifies the type of a computer. The value of this property MUST come from [Types](https://en.wikipedia.org/wiki/Computer). |
| model                  | string                      | Specifies the model of a computer.                                                                                           |
| cpu                    | StringS                     | Specifies the CUP of a computer. It MUST follow CUP naming conventions.                                                      |
| memory_size            | integer                     | Specifies the size of memory in MB.                                                                                          |
| input_devices          | list of type string         | Specifies a list of input devices.                                                                                           |
| output_device          | list of type string         | Specifies a list of output devices.                                                                                          |
| secondary_storage_refs | list of x-secondary-storage | Specifies a list of x-secondary-storage.                                                                                     |

### Relationships

| Source     | Relationship Type | Target    | Description                                                                            |
| ---------- | ----------------- | --------- | -------------------------------------------------------------------------------------- |
| x-computer | has               | ipv4-addr | The relationship specifies that a computer communicates with other PCs with ipv4-addr. |

### Example

Describe a computer with one hdd and one USB

```json
{
  "type": "x-computer",
  "spec_version": "2.1",
  "id": "x-computer--096e9478-2b7b-5bc9-a035-08464b16fc7b",
  "type": "Desktop computer",
  "cpu": "AMD Ryzen Threadripper 3970x 32-Core Processor, 3900 Mhz, 32 Core(s), 64 Logical Processor(s)",
  "secondary_storage_refs": [
    "x-secondary-storage--096e9478-2b7b-5bc9-a035-08464b16fc7b",
    "x-secondary-storage--5528432f-60ba-4a94-bc90-15d0c3fff3ea"
  ]
}
```

---

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
      "id": "x-extended-type--83aee86d-1523-4111-938e-8edc8a6c804f",
      "key": "value"
    }
  ]
}
```

---

## threat-actor-type-ov extension

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
| online-predators                     | An individual that makes sexual advances to minors.                                   |

### ani-forenisc-type-ov extension

| Vocabulary Value | Description                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| deletion         |                                                                                                                              |
| overwriting      |                                                                                                                              |
| encryption       |                                                                                                                              |
| steganography    |                                                                                                                              |
| tunneling        | Allow private communications to be exchanged over a public network.                                                          |
| onion-routing    | The process of sending messages which are encrypted in layers, denoting layers of an onion, is referred to as onion routing. |
| spoofing         |                                                                                                                              |
| obfuscation      | Hide the intended meaning of the contents of a file, making it ambiguous, confusing to read, and hard to interpret.          |
| anonymization    |                                                                                                                              |

# references:

- https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4608
- [Event Logging Structures](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-logging-structures?redirectedfrom=MSDN)
- https://github.com/libyal/libevt/blob/main/documentation/Windows%20Event%20Log%20(EVT)%20format.asciidoc
- https://github.com/williballenthin/python-evtx
- https://www.loggly.com/ultimate-guide/windows-logging-basics/#:~:text=The%20Windows%20event%20log%20contains,For%20example%2C%20IIS%20Access%20Logs.
- https://docs.microsoft.com/en-us/windows-hardware/drivers/install/format-of-a-text-log-section-body
- https://blog.eccouncil.org/6-anti-forensic-techniques-that-every-cyber-investigator-dreads/

```

```
