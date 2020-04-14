import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin
import time
import re

url = 'http://blog.nogizaka46.com/manatsu.akimoto/'
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
     "AppleWebKit/537.36 (KHTML, like Gecko)" \
     "Chrome/60.0.3112.113"
r = requests.get(url, headers={"User-Agent": ua})
soup = BS(r.text, 'html.parser')
aTag = soup.find_all("div",class_="unit")

array=[]
for link in aTag:
    #print(link)

    hTag=link.find("a")
    #print(hTag)
    #print(hTag.get('href'))
    res=hTag.get('href')
    array.append(urljoin(url,res))
#print(array)

dict={}
count=0
for url in array:
    r = requests.get(url, headers={"User-Agent": ua})
    soup = BS(r.text, 'html.parser')
    aTag = soup.find_all("div",class_="entrybottom")

    #name
    name=soup.find("div",id="blogmaintitle")
    nameT=name.get_text().strip("OFFICIAL BLOG")

    #coments=[]
    sum=0
    for link in aTag:
        come=(link.get_text().split('｜'))
        num = int(re.sub("\\D", "", come[2]))

        sum+=num
        #coments.append(num)
    count+=1
    print(count)

    dict[nameT]=sum
    time.sleep(5)
    """
    if count==5:
        break
    """

print()

f=open("test.txt","w")
f.write("insert into comments(name,countCome) values")

first=True
for mykey, myvalue in dict.items():
    #print("{0}:{1}".format(mykey,myvalue))
    if(first):
        f.write('("{0}",{1})'.format(mykey,myvalue))
        first=False
    else:
        f.write(',("{0}",{1})'.format(mykey,myvalue))
f.write(";")
f.close()
