import requests
import json

user_input = input('Введите ссылку: ')


def shorten_link(token, url):

    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": "17c09e22ad155405159ca1977542fecf00231da7",
        "Content-Type": "application/json",
    }
    data = {'long_url': user_input, "domain": "bit.ly"}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    short_link = response.json()
    return short_link['link']


try:
    bitlink = shorten_link("17c09e22ad155405159ca1977542fecf00231da7", user_input)
except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))
print(bitlink)






