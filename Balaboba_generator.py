import json
import urllib.request

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Origin': 'https://yandex.ru',
    'Referer': 'https://yandex.ru/',
}

API_URL = 'https://zeapi.yandex.net/lab/api/yalm/text3'


def makeRequest(text):
    payload = {"query": text, "intro": 0, "filter": 1}
    params = json.dumps(payload).encode('utf8')
    req = urllib.request.Request(API_URL, data=params, headers=headers)
    response = urllib.request.urlopen(req)
    request = json.loads(response.read().decode('utf8'))
    return f'{text} {request["text"]}'

