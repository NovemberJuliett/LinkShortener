import requests
import json
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

load_dotenv()
your_token = os.environ["TOKEN"]


def shorten_link(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": your_token,
        "Content-Type": "application/json",
    }
    data = {'long_url': url, "domain": "bit.ly"}
    response = requests.post(bitly_url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    short_link = response.json()
    return short_link['link']


def count_clicks(url):
    headers = {
        "Authorization": your_token
    }

    params = (
        ('unit', 'month'),
        ('units', '-1'),
    )
    parsed_link = urlparse(url)
    netloc = parsed_link.netloc
    path = parsed_link.path
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{netloc}"
                            f"{path}/clicks/summary",
                            headers=headers, params=params)
    response.raise_for_status()
    click_link = response.json()
    return click_link['total_clicks']


def is_bitlink(url):
    parsed_link = urlparse(url)
    netloc = parsed_link.netloc
    if netloc == 'bit.ly':
        return True
    else:
        return False


def main():
    user_input = input('Введите ссылку: ')
    link_is_bitlink = is_bitlink(user_input)
    if link_is_bitlink is True:
        try:
            check_clicks = count_clicks(user_input)
            print(check_clicks)
        except requests.exceptions.HTTPError as error:
            exit("Can't get data from server:\n{0}".format(error))

    elif link_is_bitlink is False:
        try:
            bitlink = shorten_link(your_token, user_input)
            print(bitlink)
        except requests.exceptions.HTTPError as error:
            exit("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()
