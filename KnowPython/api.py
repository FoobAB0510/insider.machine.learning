# Xử lý API trong Python (Kiểu Fetch trong JavaScript)

# Fetch API trong Python
import requests
import json
import urllib.parse
from urllib.parse import urlparse, parse_qs

# Hàm gửi yêu cầu GET
async def send_get_request(url, params=None):
    if params:
        url += '?' + urllib.parse.urlencode(params)
        print(url)
    response = await requests.get(url)
    return response.json()

send_get_request("https://lyrics.lewdhutao.my.eu.org/musixmatch/lyrics", "title=Say!fanfare")