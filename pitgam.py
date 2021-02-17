import requests
from lxml import html
import xlsxwriter
from time import sleep
import re

resp = requests.get("https://he.wikiquote.org/wiki/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%94:%D7%A4%D7%AA%D7%92%D7%9E%D7%99%D7%9D", headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"})
tree = html.fromstring(html = resp.text)
list_of_links=[]
half_links = tree.xpath('//div[@class="mw-category-group"]/ul/li/a/@href')

for x in half_links:
    link= "https://he.wikiquote.org" + x
    list_of_links.append(link)

pitgamfile = xlsxwriter.Workbook("pitgamfile.xlsx")
outsheet = pitgamfile.add_worksheet()
counter = 1

for y in list_of_links[:2]:
    print (counter, len(list_of_links), y)
    resp_2 = requests.get(y, headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"})
    tree_2 = html.fromstring(html = resp_2.text)
    pitgamim = tree_2.xpath('//div[@id="mw-content-text"]/div/ul/li//text()')
    makor = tree_2.xpath('//h1[@id="firstHeading"]/text()')
    for broke_pitgam in pitgamim:
        pitgamim_string="".join(pitgamim)
    for pitgam in re.split('[״"]+', pitgamim_string):
        if tree_2.xpath('//div[@id="mw-content-text"]/div/ul/li//text()//following::*[text()]') = 'ראו גם':
            outsheet.write(counter, 0, pitgam)
            outsheet.write(counter, 1, makor[0])
            counter +=1
        else:
            break


pitgamfile.close()
