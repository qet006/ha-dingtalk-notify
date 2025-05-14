import json
import requests
from .utils import generate_sign

class DingTalkRobot:
    def __init__(self, access_token, secret=None):
        self.base_url = "https://oapi.dingtalk.com/robot/send"
        self.access_token = access_token
        self.secret = secret

    def _build_url(self):
        if self.secret:
            timestamp, sign = generate_sign(self.secret)
            return f"{self.base_url}?access_token={self.access_token}&timestamp={timestamp}&sign={sign}"
        return f"{self.base_url}?access_token={self.access_token}"

    def _send_request(self, data):
        headers = {"Content-Type": "application/json"}
        url = self._build_url()
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def send_text(self, content, at_all=False, at_mobiles=None):
        """发送文本消息"""
        payload = {
            "msgtype": "text",
            "text": {"content": content},
            "at": {"isAtAll": at_all, "atMobiles": at_mobiles or []}
        }
        return self._send_request(payload)

    def send_markdown(self, title, text, at_all=False, at_mobiles=None):
        """发送Markdown消息"""
        payload = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            },
            "at": {"isAtAll": at_all, "atMobiles": at_mobiles or []}
        }
        return self._send_request(payload)
