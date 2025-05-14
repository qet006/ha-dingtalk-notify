import time
import hmac
import hashlib
import base64
from urllib.parse import quote_plus

def generate_sign(secret):
    timestamp = str(round(time.time() * 1000))
    string_to_sign = f"{timestamp}\n{secret}"
    sha256 = hmac.new(secret.encode(), string_to_sign.encode(), digestmod=hashlib.sha256).digest()
    sign = quote_plus(base64.b64encode(sha256))
    return timestamp, sign
