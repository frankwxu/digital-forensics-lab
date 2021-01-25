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

**Type Name:** windows-security-evt

## Properties

| Property Name   | Type       | Description                                              |
| --------------- | ---------- | -------------------------------------------------------- |
| type (required) | string     | The value of this property MUST be windows-security-evt. |
| id              | identifier | The ID of a secuity type                                 |
| level           | integer    |                                                          |
| task            | integer    |                                                          |
| opcode          | integer    |                                                          |
| created         | timestamp  |                                                          |
| record          | integer    |                                                          |
| process         | integer    |                                                          |
| thread          | integer    |                                                          |
| computer        | string     | The ID of the computer                                   |
| user            | string     | The security user ID                                     |

## Relationships

| Embedded Relationships |            |
| ---------------------- | ---------- |
| created_by_ref         | identifier |

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
  "Computer": "DC01.contoso.local"
}
```

references:

- https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4608
- [Event Logging Structures](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-logging-structures?redirectedfrom=MSDN)
