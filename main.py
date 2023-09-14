import requests
from urllib.parse import urlparse, urlunparse
from dotenv import load_dotenv
import os


def shorten_link(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    long_url = {'long_url': url}
    response = requests.post(bitly_url, headers=headers, json=long_url)
    response.raise_for_status()
    short_link = response.json()
    return short_link['link']


def count_clicks(url, token):
    headers = {
        "Authorization": token
    }

    params = (
        ('unit', 'month'),
        ('units', '-1'),
    )
    parsed_link = urlparse(url)
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}"
                            f"{parsed_link.path}/clicks/summary",
                            headers=headers, params=params)
    response.raise_for_status()
    click_link = response.json()
    return click_link['total_clicks']


def is_bitlink(url, token):
    headers = {
        "Authorization": token
    }
    parsed_url = urlparse(url)
    new_bitlink = parsed_url.hostname + parsed_url.path
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{new_bitlink}", headers=headers)
    if response.ok:
        return True
    else:
        return False


def main():
    load_dotenv()
    user_token = os.environ["BITLY_TOKEN"]
    user_input = input('Введите ссылку: ')
    if is_bitlink(user_input, user_token):
        try:
            check_clicks = count_clicks(user_input, user_token)
            print(check_clicks)
        except requests.exceptions.HTTPError as error:
            print("Can't get data from server:\n{0}".format(error))

    else:
        try:
            bitlink = shorten_link(user_token, user_input)
            print(bitlink)
        except requests.exceptions.HTTPError as error:
            print("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()
