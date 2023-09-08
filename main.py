import requests
import json
import urllib.parse
from urllib.parse import urlparse

user_input = input('Введите ссылку: ')


def shorten_link(token, url):

    bitly_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    data = {'long_url': url, "domain": "bit.ly"}
    response = requests.post(bitly_url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    short_link = response.json()
    return short_link['link']


try:
    bitlink = shorten_link("17c09e22ad155405159ca1977542fecf00231da7", user_input)
except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))
# print(bitlink)


def count_clicks(url):

    headers = {
        "Authorization": "17c09e22ad155405159ca1977542fecf00231da7"
    }

    params = (
        ('unit', 'month'),
        ('units', '-1'),
    )
    parsed_link = urlparse(url)
    netloc = parsed_link.netloc
    path = parsed_link.path
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}/clicks/summary", headers=headers, params=params)
    response.raise_for_status()
    click_link = response.json()
    return click_link['total_clicks']


try:
    check_clicks = count_clicks(bitlink)
except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))
# print(check_clicks)


def is_bitlink(user_input):
    headers = {
        'Authorization': "17c09e22ad155405159ca1977542fecf00231da7",
    }

    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{bitlink}', headers=headers)
    parsed_link = urlparse(user_input)
    netloc = parsed_link.netloc
    path = parsed_link.path
    print(netloc)

    link, long url (bitlink info)
    if netloc == 'bit.ly':
        print(check_clicks)
    else:
        print(bitlink)

count_clicks(bitlink)
is_bitlink(user_input)





