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


counter = 1

for y in list_of_links[:4]:
    resp_2 = requests.get(y, headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"})
    tree_2 = html.fromstring(html = resp_2.text)
    makor = tree_2.xpath('//h1[@id="firstHeading"]/text()')
    pitgamim = tree_2.xpath('//div[@id="mw-content-text"]/div/ul/li//text()')
    all = tree_2.xpath('//div[@class="mw-parser-output"]/*//text()')
    all_string="".join(all)
    all_string_list = all_string.split()


print (all_string_list)
print (all_string_list.index('ראו'))
