from lxml.html import fromstring
import requests
from investpy.utils.extra import random_user_agent
def tryme():
    # params = {
    # "curr_id": id_,
    # "smlID": str(randint(1000000, 99999999)),
    # "header": header,
    # "st_date": date_interval['intervals'][index]['start'],
    # "end_date": date_interval['intervals'][index]['end'],
    # "interval_sec": interval.capitalize(),
    # "sort_col": "date",
    # "sort_ord": "DESC",
    # "action": "historical_data"
    # }
    head = {
        "User-Agent": random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }
    url='https://www.investing.com/equities/trident-ratios'
    req=requests.get(url,headers=head)
    if req.status_code!=200:
        raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")
    print(req.text)
    root_=fromstring(req.text)
    
    path_=root_.xpath('/html/body/div[6]/section/table/tbody')
    # for x in path_:
        # print(x.text)    
        # print(path_)
