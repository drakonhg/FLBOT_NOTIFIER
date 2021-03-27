import os
import requests as req
from bs4 import BeautifulSoup as bs

HEADERS = {
    'authority': 'www.fl.ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'dnt': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not\\"A\\\\Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'referer': 'https://www.fl.ru/projects/',
    'accept-language': 'ru-RU,ru;q=0.9',
    'cookie': '__ddg1=x2JF9yDrLhmOw5DqVQ4s; PHPSESSID=01d373826b6840a68e6001a52525a51b; _ga=GA1.2.1269193950.1616787796; _gid=GA1.2.682418418.1616787796; _ga_cid=1269193950.1616787796; user_unic_ac_id=170f325e-f168-e909-69a2-346e3fdc8e8b; advcake_trackid=81ba2456-b23f-9668-cdaa-d0dd71d67ea3; _ym_uid=1616787797904039157; _ym_d=1616787797; _fbp=fb.1.1616787796705.1258820415; __gads=ID=46b44d0a92a3b173-22035847e3ba001a:T=1616787796:RT=1616787796:S=ALNI_MaB2JJDMZqujJo_eC8goK9Vh90uEA; _ym_isad=2; new_pf0=1; new_pf10=1; hidetopprjlenta=0; cookies_accepted=1; __ddg2=21aIWAnwY0T19UO1; uechat_3_first_time=1616828334859; uechat_3_pages_count=2; uechat_3_disabled=true; new_pf0=1',}

URL = "https://www.fl.ru"

URL_PROJECT = "https://www.fl.ru/projects/"

def check_result():
    HOME_PAGE = req.get(URL_PROJECT, headers=HEADERS)

    content = bs(HOME_PAGE.content, 'html.parser')

    dict_values = {}

    result = content.find('a', class_="b-post__link")

    dict_values['title'] = result.text
    dict_values['link'] =  URL + result['href']

    with open("results.txt", "r+") as file:
        value = file.read().split()

        if len(value) == 0:
            file.write(f"{dict_values['title']}: {dict_values['link']}")
            return dict_values

        elif value[-1] != dict_values['link']:
            file.truncate(0)
            file.write(f"{dict_values['title']}: {dict_values['link']}")
            return dict_values

        else:
            return

