# tpm.py

[![CI](https://github.com/peshay/tpm/actions/workflows/ci.yml/badge.svg)](https://github.com/peshay/tpm/actions/workflows/ci.yml)
[![Python version](https://img.shields.io/pypi/pyversions/tpm.svg)](https://pypi.org/project/tpm/)
[![license](https://img.shields.io/github/license/peshay/tpm.svg)](https://github.com/peshay/tpm/blob/master/LICENSE)

Python client for the TeamPasswordManager API.

Official API documentation: <https://teampasswordmanager.com/docs/api/>

## Supported API versions

- `TpmApiv3`
- `TpmApiv4`
- `TpmApiv5`
- `TpmApiv6` (recommended)

## Install

```bash
pip install tpm
```

## Quick start (API v6)

```python
import tpm

URL = "https://mypasswordmanager.example.com"
USER = "MyUser"
PASS = "Secret"

client = tpm.TpmApiv6(URL, username=USER, password=PASS)

for item in client.list_passwords():
    print(item.get("name"))
```

## Authentication

### Username/password

```python
client = tpm.TpmApiv6(URL, username=USER, password=PASS)
```

### API keys

```python
client = tpm.TpmApiv6(
    URL,
    public_key="your_public_key",
    private_key="your_private_key",
)
```

## Client options

You can pass transport and behavior options when creating a client:

```python
import requests
import tpm

session = requests.Session()
client = tpm.TpmApiv6(
    URL,
    username=USER,
    password=PASS,
    timeout=30,          # default: 30 seconds
    verify_ssl=True,     # default: True
    unlock_reason="Routine access",
    session=session,     # optional injected requests.Session
)
```

## v6 header features

API v6 supports extra request headers for list/show endpoints:

- `X-Metadata-Only`
- `X-Permissions`
- `X-Page-Size`

Examples:

```python
client = tpm.TpmApiv6(URL, username=USER, password=PASS)

projects = client.list_projects(metadata_only=True, permissions=True, page_size=50)
password = client.show_password(14, metadata_only=True)
```

## Notable v6 methods

In addition to previous API methods, `TpmApiv6` includes:

- `list_projects_all()`
- `list_passwords_all()`
- `copy_password(ID, PROJECT_ID)`
- `duplicate_password(ID, NEW_NAME)`
- `list_users_search(searchstring)`
- `list_passwords_of_user(ID)`
- `list_projects_of_user(ID)`
- `list_mypasswords_archived()`
- `list_mypasswords_favorite()`
- `update_custom_fields_of_mypassword(ID, data)`
- `archive_mypassword(ID)`
- `unarchive_mypassword(ID)`
- `list_mypassword_files(ID)`
- `upload_mypassword_file(ID, file, notes=...)`
- `copy_mypassword(ID, PROJECT_ID)`
- `duplicate_mypassword(ID, NEW_NAME)`
- `set_favorite_mypassword(ID)`
- `unset_favorite_mypassword(ID)`
- `list_log()`
- `search_log(searchstring)`

## Existing method groups

The client also covers:

- Projects
- Passwords
- My Passwords
- Favorites
- Users
- Groups
- Files
- Password generator
- API version checks

For endpoint-level behavior and payload details, use the official TeamPasswordManager docs.

## Logging

The library uses Python `logging`. Configure your own handlers/levels in your app:

```python
import logging

logging.basicConfig(
    filename="tpm.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
```

## Development

Install dev dependencies:

```bash
python -m pip install -e .[dev]
```

Run tests:

```bash
python -m pytest
```

