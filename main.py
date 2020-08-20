import json
import os
import sys
import time

import random
import requests
from bs4 import BeautifulSoup
from requests import RequestException

cookie = os.environ.get("cookie")
pages = int(os.environ.get("pages"))


def get_soup_from_page(url):
    global cookies
    cookies = {'PHPSESSID': cookie}
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')

    return soup


def get_page():
    global xsrf_token, points

    try:
        soup = get_soup_from_page('https://www.steamgifts.com')

        xsrf_token = soup.find('input', {'name': 'xsrf_token'})['value']
        points = soup.find('span', {'class': 'nav__points'}).text  # storage points
    except RequestException:
        print('Cant connect to the site')
        print('Waiting 2 minutes and reconnect...')
        time.sleep(120)
        get_page()
    except TypeError:
        print('Cant recognize your cookie value.')
        time.sleep(30)
        sys.exit(0)


# get codes of the games
def get_games(list):
    global game_name
    global pages
    print(f'Going through {list}.')

    n = 1
    while n <= pages:
        print('Proccessing games from %d page.' % n)

        soup = get_soup_from_page('https://www.steamgifts.com/giveaways/search?page=' + str(n) + str(f'&type={list}'))

        try:
            gifts_list = soup.find_all(
                lambda tag: tag.name == 'div' and tag.get('class') == ['giveaway__row-inner-wrap'])

            for item in gifts_list:

                game_cost = item.find_all('span', {'class': 'giveaway__heading__thin'})

                last_div = None
                for last_div in game_cost:
                    pass
                if last_div:
                    game_cost = last_div.getText().replace('(', '').replace(')', '').replace('P', '')

                game_name = item.find('a', {'class': 'giveaway__heading__name'}).text

                if int(points) - int(game_cost) < 0:
                    print('Not enough points to enter: ' + game_name)
                    continue
                elif int(points) - int(game_cost) > 0:
                    entry_gift(item.find('a', {'class': 'giveaway__heading__name'})['href'].split('/')[2])

            n = n + 1
        except AttributeError as e:
            break


def entry_gift(code):
    payload = {'xsrf_token': xsrf_token, 'do': 'entry_insert', 'code': code}
    entry = requests.post('https://www.steamgifts.com/ajax.php', data=payload, cookies=cookies)
    json_data = json.loads(entry.text)

    get_page()
    # updating points after entered a giveaway
    if json_data['type'] == 'success':
        print('> Bot has entered giveaway: ' + game_name)
        time.sleep(random.uniform(3, 8))


def loop():
    get_page()
    get_games("wishlist")
    if int(points) > 80:
        print('Wishlist complete. Some score left so going through all list... ')
        get_games("all")
    print('List complete.')


if __name__ == '__main__':
    loop()
