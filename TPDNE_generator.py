from io import BytesIO

import requests
# from PIL import Image
import json

url = "https://thispersondoesnotexist.com/"

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.222 '
                  'Safari/537.36',
    'Origin': 'https://thispersondoesnotexist.com/',
    'Referer': 'https://pikabu.ru/',
}
def makeRequest():
    response = requests.get("https://thispersondoesnotexist.com/image", headers={'User-Agent': 'My User Agent 1.0'}).content
    return response
    # return Image.open(BytesIO(response))