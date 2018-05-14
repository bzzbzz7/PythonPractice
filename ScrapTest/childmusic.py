#-*-coding=utf-8-*-
import requests
from lxml import etree
import subprocess
import requests

session = requests.Session()
def getContent(url):
    # url='http://www.iqiyi.com/v_19rrkwcx6w.html'
    try:
        ret = session.get(url)
    # except Exception,e:
    except:
        # print e
        return None
    if ret.status_code==200:
        return ret.text
    else:
        return None

def getUrl():
    url='http://www.iqiyi.com/v_19rrkwcx6w.html'
    url2='http://www.iqiyi.com/v_19rrl2td7g.html' # 31-61
    content = getContent(url)
    root = etree.HTML(content)
    elements=root.xpath('//div[@data-current-count="1"]//li/a/@href')
    for items in elements[:2]:
        song_url = items.replace('//','')
        song_url=song_url.strip()
        print(song_url)
        # p=subprocess.Popen('python you-get -d --format=HD {}'.format(song_url),stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        # output,error = p.communicate()
        # print(output)
        # print(error)
        # p.wait()
        name = song_url.split(r"/")[-1]
        print(name)
        downloadfile(song_url, name)

def downloadfile(url,name):
    if not url.startswith('http://'):
        url = "http://" + url
    r = requests.get(url)
    with open(name, "wb") as code:
        code.write(r.content)


def main():
    getUrl()

if __name__ == '__main__':
    main()