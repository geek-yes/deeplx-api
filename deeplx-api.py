import random

import gevent
from gevent.pool import Pool
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

import requests

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)
from flask import Flask, request
import json

app = Flask(__name__)

valid_urls = []


def check_url_availability(url):
    global valid_urls
    try:
        headers = {"Content-Type": "application/json"}
        payload = {
            "text": "Hello, world!",
            "source_lang": "EN",
            "target_lang": "ZH"
        }
        response = requests.post(url, verify=False, timeout=5, headers=headers,
                                 data=json.dumps(payload))
        if "你好，世界" in response.text:
            valid_urls.append(url)
    except Exception as e:
        print('%s: %s' % (url, type(e).__name__))


def get_valid_urls():
    with open(R"urls.txt", "r") as f:
        urls = f.read().splitlines()

    urls = list(set(urls))
    p = Pool(200)
    jobs = [p.spawn(check_url_availability, _url) for _url in urls]

    gevent.joinall(jobs)


get_valid_urls()
print("available urls count: {}".format(len(valid_urls)))

def single_translate(text, source_lang, target_lang):
    for i in range(10):
        urls = random.choice(valid_urls)
        try:
            headers = {"Content-Type": "application/json"}
            payload = {
                "text": text,
                "source_lang": source_lang,
                "target_lang": target_lang
            }
            response = requests.post(urls, verify=False, timeout=5, headers=headers,
                                     data=json.dumps(payload))
            data = response.json()
            if data["code"] == 200:
                return response.text
        except Exception as e:
            print('%s' % (type(e).__name__))

def get_translate_data(text, source_lang, target_lang):
    tasks = [gevent.spawn(single_translate, text, source_lang, target_lang) for _ in range(3)]
    done = gevent.wait(tasks, count=1)
    for t in tasks:
        t.kill()
    return done.pop().value


@app.route('/translate', methods=['POST'])
def translate():  # put application's code here
    data = json.loads(request.get_data())
    text = data['text']
    source_lang = data['source_lang']
    target_lang = data['target_lang']
    return get_translate_data(text, source_lang, target_lang)


if __name__ == '__main__':
    http_server = WSGIServer(("127.0.0.1", 5000), app)
    http_server.serve_forever()
