import requests
import json

url = "https://pelevin.gpt.dobro.ai/generate/"

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Origin': 'https://porfirevich.ru',
    'Referer': 'https://porfirevich.ru/',
}

variants = []


def makeRequest(text, length):
    global variants
    payload = json.dumps({
    "prompt": text,
    "length": length,
})

    response = requests.get("POST", url, data=payload, headers=headers)
    variants = response.text.split('{"replies":["')[1].replace('"]}', '').split('","')
    return f'{text}{max(variants, key=len)}'

