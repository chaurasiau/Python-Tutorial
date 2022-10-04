from urllib import request
import requests
from celery_config import app
from celery_add import add


@app.task
def fetch_url(url):
    resp = request.get(url)
    print(f"The Response for {url} is -> {resp}")


def func(*urls, a=1, b=2):
    for url in urls:
        fetch_url.delay(url)  # this line serializes and put in to redis queue
        sum1 = add.delay(a, b)
        print(f"func -> sum is {sum1}")


if __name__ == "__main__":
    urls = ["http://google.com", "https://amazon.in",
            "https://facebook.com", "https://twitter.com", "https://alexa.com"]

    func(*urls)

    # Run in ubuntu - "redis-server"
# cmd = celery -A celery_config worker -l info -c 5 -P gevent -E
# celery -A <module/celery-config> worker -l info -P gevent (pip install gevent)
# https://stackoverflow.com/questions/45744992/celery-raises-valueerror-not-enough-values-to-unpack
# cmd - python simple_with_celery.py
