---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-microsoft-outlook-emails/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-microsoft-outlook-emails/README.md
---
# Microsoft Outlook Email Reader

```bash
pip install llama-index-readers-microsoft-outlook-emails
```

The loader retrieves emails from an Outlook mailbox and indexes the subject and body of the emails.

## Prerequisites

### App Authentication using Microsoft Entra ID (formerly Azure AD)

1. You need to create an App Registration in Microsoft Entra ID. Refer here
2. API Permissions for the created app:
   1. Microsoft Graph --> Application Permissions --> Mail.Read (**Grant Admin Consent**)

More info on Microsoft Graph APIs - Refer here

## Usage

To use this loader, `client_id`, `client_secret`, and `tenant_id` of the registered app in Microsoft Azure Portal are required.

This loader fetches emails from a specified folder in an Outlook mailbox.

```python
from llama_index.readers.outlook_emails import OutlookEmailReader

loader = OutlookEmailReader(
    client_id="",
    client_secret="",
    tenant_id="",
    user_email="",
    folder="Inbox",
    num_mails=10,
)

documents = loader.load_data()
```

The loader retrieves the subject and body of the emails from the specified folder in Outlook.
