import os
import requests as req
from bs4 import BeautifulSoup as bs

HEADERS = {
    'authority': 'www.fl.ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.fl.ru/projects/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ym_uid=157468517432521403; _ga=GA1.2.618592098.1598959650; cookies_accepted=1; __ddg1=AqnvAKyGodtcxFnIgy0O; user_device_id=ul8q7rkoxn01epr30deahs1vnwq05tzj; __ddg2=xcZ0qqRwnFBir2L4; _fbp=fb.1.1612353850421.1271460300; __ddg4=6d6eb3f7074457e7c1c5e4fb06f73661; take-care-showed=%5B4676579%5D; _ym_d=1616152983; _ga_cid=618592098.1598959650; user_unic_ac_id=b3414462-bae6-fbfc-2ef1-ec4a72027912; advcake_trackid=17417063-e725-7a7b-1845-79efe9f9e6f0; new_pf0=1; new_pf10=1; PHPSESSID=df7940df9b450054b5af8ebc7375aaad; id=4538514; name=drakonhg%40gmail.com; pwd=4e7fd36de61295c3bf225ac9e2347eb4; __ddgid=1EE9BsVTyoeQVG3D; _gid=GA1.2.798844382.1617445642; __ddgmark=gPTCnT1xH3qerzJr; ue_sso_token=HacYqhWnCCs%252BUviJwLRrciuwN26lf%252FJCGaoePBC79udM9d%252FwzvrewSrHPEuQcci6w5e66dF80521FvXDG2VeZK1pTaX%252B1GZr9qm4R44kDDBBVCCKgAqksDPn1K1Ve2eYaExWaBHIAvtoGwPIOJc31uvw7%252FQN2SiXbUBXvjChM8E1vXL2URsGD6wGsEmLRTg2KBvmxtuS9rY58bu8uOmYRTVOtVKk6KgxzrsfIKMh23slhU8gGja3Vk%252Fqa6wftZ00Vv9tJq4lMsAL8WC5tc4iuK%252BPpEXwJaeeHrFr0LrJAqdb61sJVpGuaSh%252BEc%252BFwDLNq0Zb94kXQmoZ4XgmlpBbENvbdT%252FXrCf5i7zt9kznVc%252BPVhQMeNW4%252Fq6Q9x%252FolUDJtXSKmExA6wtCik2RsQ1d%252B7NKYeWDbDABvHRnS5DgmxniOjwBmy%252FPJWNSYyqc4FkTY7OrNis5A6s5WOCNiLnmaJkRz8RqImSKXlU6neeFfUbB3zLKZFYIl2Frd0BQy9YP5WwhVxYQaaeDWBrrB3%252B2wJDrUPMJQZaXMRB%252FVWXU8rM%253D; XSRF-TOKEN=FwwPCP42Ai8NgXANVDXdbezDfS6E7sAw1DruCHem; hidetopprjlenta=1; hidetopprjlenta_time=1617819820; mobapp=1617868855; _ym_isad=1; uechat_3_first_time=1617876121805; uechat_3_pages_count=49; uechat_3_disabled=true',
}

URL = "https://www.fl.ru"

URL_PROJECT = "https://www.fl.ru/projects/"

def check_result():
    HOME_PAGE = req.get(URL_PROJECT, headers=HEADERS)

    content = bs(HOME_PAGE.content, 'html.parser')

    dict_values = {}

    for post in content.find_all('h2', class_="b-post__title"):
        if 'b-post__pin' in post['class']:
            result = content.find_all('a', class_="b-post__link")[2]
            print(result)
            dict_values['title'] = result.text
            dict_values['link'] = URL + result['href']

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
        else:
            result = content.find('a', class_="b-post__link")
            print(result)
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



check_result()