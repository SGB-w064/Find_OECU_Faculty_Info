import requests
import urllib
import pprint
from bs4 import BeautifulSoup as BS

def getInfo(teacher_name, find_info):
    url = "https://research.osakac.ac.jp/index.php?" + urllib.parse.quote(teacher_name)
    site = requests.get(url)
    data = BS(site.text, "html.parser")

    print(data.title.text)
    tab_data = data.select(".list1")

    select_data = [i.text for i in tab_data if find_info in i.text]
    if select_data is None:
        select_data = data.find_all(text = find_info)[0].string
    #print([i for i in select_data if find_info in i])
    #pprint.pprint(tab_data)
    #pprint.pprint(select_data[0])
    return select_data[0]

def main():
    teacher_name = input("教員の名前をフルネームで入力: ")
    find_info = input("探したい情報を入力: ")
    print(getInfo(teacher_name, find_info))

if __name__ == "__main__":
    main()