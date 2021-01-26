# Cyber-observable Objects for Digital Forensics

### The goal of the project is to create a list of customized STIX™ Cyber-observable Objects for facilitating digital forensic investigations. We follow the STIX specification for [customizing objects] (https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_p2sz1mp7z524). The most important rule to create a new object type is:

- The value of the type property in a Custom Object SHOULD start with “x-” followed by a source unique identifier (like a domain name with dots replaced by hyphens), a hyphen and then the name. For example, x-example-com-customobject.

---

## Table of Contents (updating)

- Case Study
  - [Investigating NIST Data Leakage](#Investigating-NIST-Data-Leakage)
  - [Investigating Illegal Possession of Images](#Investigating-Illegal-Possession-of-Images)
  - [Investigating Email Harassment](#Investigating-Email-Harassment)
- [Tools Used](#Tools-Used)

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

## Windows Event Object

**Type Name:** x-windows-evt

## Properties

| Property Name             | Type       | Description                                                                            |
| ------------------------- | ---------- | -------------------------------------------------------------------------------------- |
| type (required)           | string     | The value of this property MUST be windows-security-evt.                               |
| id (required)             | identifier | The ID of a secuity type.                                                              |
| log_name (required)       | enum       | The value of this property MUST come from the log-nam-enum enumeration.                |
| logged_time (required)    | timestamp  |                                                                                        |
| source                    | string     |                                                                                        |
| event_id                  | integer    |                                                                                        |
| task_category             | string     |                                                                                        |
| computer                  | string     | The name of the computer.                                                              |
| user_account_ref          | identifier | The user account that is associated with the evewnt.                                   |
| belongs_to_ref (required) | identity   | The relation describes that event is a part of file or artifact (e.g., cache, memory). |

## Relationships

| Source | Relationship Type | Target | Description |
| ------ | ----------------- | ------ | ----------- |

## Log Name Enumeration

**Enumeration Name:** log-name-enum

| Vocabulary Value | Description |
| ---------------- | ----------- |
| application      |             |
| security         |             |
| setup            |             |
| system           |             |
| forwarded-events |             |

```json
{
  "type": "x-windows-evt",
  "spec_version": "2.1",
  "id": "x-windows-evt--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "log_name": "security",
  "logged_time": "2021-01-06T20:03:00.000Z",
  "source": "Microsoft Windows security auditing.",
  "event_id": "4624",
  "task_category ": "Logon",
  "computer": "ryzen3790-xu",
  "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
  "belongs_to_ref": "file--9460a8a8-6351-40bb-b5ad-18f3265bbf7a"
}
```

## Browser History Event Object

**Type Name:** x-browser-history-evt

## Properties

| Property Name             | Type       | Description                                                                            |
| ------------------------- | ---------- | -------------------------------------------------------------------------------------- |
| type (required)           | string     | The value of this property MUST be browser-history.                                    |
| id (required)             | identifier | The ID of a browser history record.                                                    |
| url                       | string     |                                                                                        |
| title                     | string     | The title of a web page has been visited.                                              |
| visit_time                | timestamp  | The last time visited.                                                                 |
| visit_count               | integer    | The number of times visited                                                            |
| browser_name              | string     | The values for this property SHOULD come from the browser-name-ov open vocabulary.     |
| browser_ref               | identifier | The value type for this property SHOULD software.                                      |
| file_requested_ref        | identifier | The ID of the file the http requested.                                                 |
| user_account_ref          | identifier | The user account that is associated with record.                                       |
| belongs_to_ref (required) | identifier | The relation describes that event is a part of file or artifact (e.g., cache, memory). |

## Relationships

| Source | Relationship Type | Target | Description |
| ------ | ----------------- | ------ | ----------- |

```json
{
  "type": "x-browser-history-evt",
  "spec_version": "2.1",
  "id": "x-browser-history-evt--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "url": "https://www.ubalt.edu/cpa/undergraduate-majors-and-minors/majors/cyber-forensics/",
  "title": "B.S. in Cyber Forensics | University of Baltimore",
  "visit-time": "2021-01-06T20:03:22.000Z",
  "visit-count": 2,
  "browser_name": "chrome",
  "browser_ref": "software--db997c40-458d-4da6-a339-6eef90cf325e",
  "file_requested_ref ": "file--10624790-0e43-4498-89da-8979ab4215ae",
  "user_account_ref ": "user-account--68f0b7d5-f7ab-47d2-8773-739ceb1c11bb",
  "belongs_to_ref": "file--843f6a43-0603-4e0d-84a4-198386eecf4f"
}
```

## Browser Name Open Vocabulary

Vocabulary Name: browser-name-ov

| ocabulary Value | Description                    |
| --------------- | ------------------------------ |
| chrome          | Google chrome browser          |
| ie              | Internet explore               |
| edge            | Microsoft Edge                 |
| firefox         | Mozilla Firefox                |
| safari          | Apple Safari                   |
| chromium        | Open source Chrome alternative |
| opera           |                                |
| maxthon         |                                |
| brave           |                                |
| 360-secure      | 360 Secure Browser             |
| tor             |                                |
| other           |                                |

# references:

- https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4608
- [Event Logging Structures](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-logging-structures?redirectedfrom=MSDN)
- https://github.com/libyal/libevt/blob/main/documentation/Windows%20Event%20Log%20(EVT)%20format.asciidoc
- https://github.com/williballenthin/python-evtx
- https://www.loggly.com/ultimate-guide/windows-logging-basics/#:~:text=The%20Windows%20event%20log%20contains,For%20example%2C%20IIS%20Access%20Logs.
