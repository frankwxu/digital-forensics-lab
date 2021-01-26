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
| illegal-possessor                    | An individual that owns, produces, distributes illegal information and device         |
| online- predators                    | An individual that makes sexual advances to minors.                                   |

## Windows Security Event Object

**Type Name:** x-windows-security-evt

## Properties

| Property Name      | Type       | Description                                              |
| ------------------ | ---------- | -------------------------------------------------------- |
| type (required)    | string     | The value of this property MUST be windows-security-evt. |
| id (required)      | identifier | The ID of a secuity type                                 |
| level              | integer    |                                                          |
| task               | integer    |                                                          |
| opcode             | integer    |                                                          |
| created (required) | timestamp  |                                                          |
| record             | integer    |                                                          |
| process            | integer    |                                                          |
| thread             | integer    |                                                          |
| computer           | string     | The name of the computer                                 |
| user               | string     | The security user ID                                     |
| belongs_to_ref     | identity   | The relation describes that the source is a part of file |

## Relationships

| Source | Relationship Type | Target | Description |
| ------ | ----------------- | ------ | ----------- |

```json
{
  "type": "x-windows-security-evt",
  "spec_version": "2.1",
  "id": "campaign--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
  "created": "2016-04-06T20:03:00.000Z",
  "level": 0,
  "opcode": 0,
  "record": 1101704,
  "proces": 58,
  "thread": 511,
  "Computer": "DC01.contoso.local",
  "belongs_to_ref": "file--9460a8a8-6351-40bb-b5ad-18f3265bbf7a"
}
```

## Browser History Record Object

**Type Name:** x-browser-history-record

## Properties

| Property Name      | Type                    | Description                                                                                                       |
| ------------------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| type (required)    | string                  | The value of this property MUST be browser-history                                                                |
| id (required)      | identifier              | The ID of a browser history record                                                                                |
| url                | string                  |                                                                                                                   |
| title              | string                  | The title of a web page has been visited                                                                          |
| visit-time         | timestamp               |                                                                                                                   |
| visit-count        | integer                 | The number of times visited                                                                                       |
| browser-type       | identifier              | The values for this property SHOULD come from the browser-type-ov open vocabulary.                                |
| file-requested_ref | identifier              | The ID of the file the requst requested                                                                           |
| computer           | string                  | The name of the computer                                                                                          |
| user-account       | identifier              | The user-account that is associated with record                                                                   |
| belongs_to_ref     | list of type identifier | The source of object. The objects referenced in this list MUST be of type file or artifact (e.g., cache, memory). |

## Relationships

| Source | Relationship Type | Target | Description |
| ------ | ----------------- | ------ | ----------- |

```json
{
  "type": "windows-security-evt",
  "spec_version": "2.1",
  "id": "campaign--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
  "created": "2016-04-06T20:03:00.000Z",
  "level": 0,
  "opcode": 0,
  "record": 1101704,
  "proces": 58,
  "thread": 511,
  "Computer": "DC01.contoso.local",
  "belongs_to_ref": "file--9460a8a8-6351-40bb-b5ad-18f3265bbf7a"
}
```

## Browser Type Open Vocabulary

Vocabulary Name: browser-type-ov

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
