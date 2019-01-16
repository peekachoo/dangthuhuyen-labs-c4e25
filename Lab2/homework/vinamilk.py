from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")
section = soup.find("table", id="tableContent")

tr_list = section.find_all("tr", {"class":["r_item", "r_item_a"]})

sec_list = []
keys = ["Section", "4/2016", "1/2017", "2/2017", "3/2017"]
sec = dict.fromkeys(keys)

for tr in tr_list:
    td_list = tr.find_all("td")
    for i, td in enumerate(td_list):
        if i < 5:
            yee = td.string
            sec[keys[i]] = str(yee).strip()
    sec_list.append(OrderedDict(sec))

pyexcel.save_as(records=sec_list, dest_file_name="vinamilk.xls")