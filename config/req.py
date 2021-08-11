import requests


# class HighRequest:

def get(url):
    c = requests.get(url)

    if c.status_code == 200:
        print(1000)

    return c
