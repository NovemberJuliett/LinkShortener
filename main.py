import requests
import json

user_input = input('Введите ссылку: ')


def shorten_link(token, url):

    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": "734f9ab8129ff9477ad1a2d86d4bdab5270e30cf",
        "Content-Type": "application/json",
    }
    data = {"long_url": f"{user_input}", "domain": "bit.ly"}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    short_link = response.json()
    return short_link['link']


print('Битлинк', shorten_link("734f9ab8129ff9477ad1a2d86d4bdab5270e30cf", user_input))

try:
    bitlink = shorten_link("734f9ab8129ff9477ad1a2d86d4bdab5270e30cf", user_input)
    print("Все хорошо")
except requests.exceptions.HTTPError as error:
    # exit("Can't get data from server:\n{0}".format(error))
    print("Все плохо")





