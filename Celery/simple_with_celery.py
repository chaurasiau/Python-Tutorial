import requests
from time import perf_counter
from celery import Celery

app = Celery('simple_with_celery', broker='redis://localhost:6379/0')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(f"Response for {url} is -> {resp}")


def func(*urls):
    print(f"Started fetching URLS.")
    start = perf_counter()
    for url in urls:
        fetch_url.delay(url)
    end = perf_counter()
    print(f"Time take is {end - start} seconds!.")


if __name__ == "__main__":
    urls = ["http://google.com", "https://amazon.in",
            "https://facebook.com", "https://twitter.com", "https://alexa.com"]
    func(*urls)

# Run in ubuntu - "redis-server"
# cmd = celery -A simple_with_celery worker -l info -c 5 -P gevent -E
# celery -A <module> worker -l info -P gevent (pip install gevent)
# https://stackoverflow.com/questions/45744992/celery-raises-valueerror-not-enough-values-to-unpack
# cmd - python simple_with_celery.py
