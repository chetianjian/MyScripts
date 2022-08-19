import akshare as ak
import time
import datetime as dt


def get_price(code=None, name=None, frequency=6, source="em"):
    """
    code: list object, can be str while searching for single stock.
    name: list object, can be str while searching for single stock.
    frequency: int object, the frequency of requesting data, default for 6 seconds.
    sourse: "em" or "tx", default for "em", request data from eastmoney or tencent.
    """
    if not (code and name):
        code = input("Please enter a single code number:")
    if code:
        while True:
            beijing_time = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc).astimezone(
                dt.timezone(dt.timedelta(hours=8), name="Asia/shanghai")).time()
            if (dt.time(11, 30, 0) < beijing_time < dt.time(13, 0, 0)) or \
                    (beijing_time > dt.time(15, 0, 0)):
                return "Not available now!"
            else:
                df = ak.stock_zh_a_spot_em()
                print(df.set_index("代码").loc[code][["名称", "最低", "最高", "最新价", "涨跌幅"]])
                time.sleep(frequency)
    else:
        while True:
            beijing_time = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc).astimezone(
                dt.timezone(dt.timedelta(hours=8), name="Asia/shanghai")).time()
            if (dt.time(11, 30, 0) < beijing_time < dt.time(13, 0, 0)) or \
                    (beijing_time > dt.time(15, 0, 0)):
                return "Not available now!"
            else:
                df = ak.stock_zh_a_spot_em()
                print(df.set_index("代码").loc[code][["名称", "最低", "最高", "最新价", "涨跌幅"]])
                time.sleep(frequency)