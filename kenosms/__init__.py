import requests
import json

class KenoSMS:
    def __init__(self, api_token):
        self.api_token = api_token
        self.api_url = "https://sms.kenosis.co.tz/api/http/sms"

    def send_sms(self, recipient, sender_id, message, type="plain", schedule_time=None, dlt_template_id=None):
        data = {
            "api_token": self.api_token,
            "recipient": recipient,
            "sender_id": sender_id,
            "type": type,
            "message": message
        }
        if schedule_time:
            data['schedule_time'] = schedule_time
        if dlt_template_id:
            data['dlt_template_id'] = dlt_template_id

        response = requests.post(self.api_url, headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps(data))
        return response.json()

    def get_sms(self, uid):
        url = f"{self.api_url}/{uid}"
        response = requests.get(url, headers={"Content-Type": "application/json", "Accept": "application/json"}, params={"api_token": self.api_token})
        return response.json()

    def list_sms(self):
        response = requests.get(self.api_url, headers={"Content-Type": "application/json", "Accept": "application/json"}, params={"api_token": self.api_token})
        return response.json()