import string, time, random
import requests, httplib2


def get_link(my_url):
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        'Host': 'prnt.sc'}
    try:
        r = requests.get(my_url, headers=my_headers)
    except AssertionError as error:
        print(error)
        time.sleep(20)
    text = r.content.decode('utf-8')
    ind_start_item = text.find('no-click') + 32
    ind_end_item = text.find('crossorigin', ind_start_item) - 2
    image_link = text[ind_start_item:ind_end_item]
    return image_link


def scrape_pictures(picture_url):
    filename = picture_url.rsplit('/', 1)[-1]
    h = httplib2.Http()
    response, content = h.request(picture_url)
    out = open(filename, 'wb')
    out.write(content)
    out.close()


# base_url = 'https://prnt.sc/m6lwrl'
url = "https://prnt.sc/m60"
url += ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))
link_url = (get_link(url))
scrape_pictures(link_url)
