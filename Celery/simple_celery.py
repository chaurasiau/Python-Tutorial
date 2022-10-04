import requests
from time import perf_counter


def func(urls):
    start = perf_counter()
    for url in urls:
        resp = requests.get(url=url)
        print(f"Response is {resp}")
    end = perf_counter()
    print(f"It took {end - start} seconds to execute.")


if __name__ == "__main__":
    urls = ["http://google.com", "https://amazon.in",
            "https://facebook.com", "https://twitter.com", "https://alexa.com"]

    func(urls)
