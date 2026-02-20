

# KenoSMS Python SDK

Official Python SDK for sending and managing SMS via the KenoSMS HTTP API.

This SDK allows you to:

* Send SMS messages
* Schedule SMS for later delivery
* Retrieve a single SMS by UID
* List all sent SMS messages

---

## Installation

Install the package using pip:

```bash
pip install kenosms
```

---

## Requirements

* Python 3.8+
* `requests` (installed automatically as a dependency)

---

## Getting Started

### 1. Import the Class

```python
from kenosms import KenoSMS
```

### 2. Initialize the Client

```python
sms = KenoSMS(api_token="YOUR_API_TOKEN")
```

Replace `YOUR_API_TOKEN` with your actual API token provided by KenoSMS.

---

## Send SMS

```python
response = sms.send_sms(
    recipient="2557XXXXXXXX",
    sender_id="KENOSMS",
    message="Hello from KenoSMS Python SDK!"
)

print(response)
```

### Parameters

| Parameter       | Type   | Required | Description                                        |
| --------------- | ------ | -------- | -------------------------------------------------- |
| recipient       | string | Yes      | Recipient phone number (e.g., 2557XXXXXXXX)        |
| sender_id       | string | Yes      | Registered Sender ID                               |
| message         | string | Yes      | SMS message content                                |
| type            | string | No       | SMS type (default: `plain`)                        |
| schedule_time   | string | No       | Schedule date/time (format: `YYYY-MM-DD HH:MM:SS`) |
| dlt_template_id | string | No       | DLT Template ID if required                        |

---

## Send Scheduled SMS

```python
response = sms.send_sms(
    recipient="2557XXXXXXXX",
    sender_id="KENOSMS",
    message="This message is scheduled",
    schedule_time="2026-02-25 10:00:00"
)

print(response)
```

---

## Get a Single SMS

Retrieve SMS details using its unique ID (UID):

```python
response = sms.get_sms(uid="SMS_UNIQUE_ID")

print(response)
```

---

## List All SMS

```python
response = sms.list_sms()

print(response)
```

---

## API Endpoint

This SDK uses the following API endpoint:

```
https://sms.kenosis.co.tz/api/http/sms
```

---

## Full Example

```python
from kenosms import KenoSMS

sms = KenoSMS(api_token="YOUR_API_TOKEN")

response = sms.send_sms(
    recipient="2557XXXXXXXX",
    sender_id="KENOSMS",
    message="Test message from Python SDK"
)

print(response)
```

---

## Error Handling Example

```python
try:
    response = sms.send_sms(
        recipient="2557XXXXXXXX",
        sender_id="KENOSMS",
        message="Testing error handling"
    )
    print(response)
except Exception as e:
    print("Error:", str(e))
```

---

## License

MIT License

---

## Author
Fortunatus Chrispin Rwekiti
KenoSMS
Website: [https://sms.kenosis.co.tz](https://sms.kenosis.co.tz)

---

