import requests
import json

url = "https://api.aicloud.sbercloud.ru/public/v1/public_inference/gpt3/predict"

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Origin': 'https://russiannlp.github.io',
    'Referer': 'https://russiannlp.github.io/',
}


def makeRequest(text):
    payload = json.dumps({
    "text": text,
})

    response = requests.request("POST", url, data=payload, headers=headers)
    return f"{text}{(json.loads(response.text)['predictions'])[len(text):]}"

