import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


def shorten_link(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    long_url = {'long_url': url, "domain": "bit.ly"}
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
    load_dotenv()
    user_token = os.environ["BITLY_TOKEN"]
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
            bitlink = shorten_link(user_token, user_input)
            print(bitlink)
        except requests.exceptions.HTTPError as error:
            exit("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()
