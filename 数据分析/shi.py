# coding=utf-8
import re
import requests
from lxml import etree
import random
from pymongo import MongoClient
from multiprocessing import pool


class Page(object):
    def __init__(self):

        self.url = "http://www.zhzyw.org/zygjyd/book_show.php?id=0&name=%C9%F1%C5%A9%B1%BE%B2%DD%BE%AD&pian=0"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '

                                      + 'Chrome/55.0.2883.87 Safari/537.36'}


    def parse_url(self,url):
        response = requests.get(url,headers = self.headers).text
        print(response)
        return response

    def get_con_list(self,con):
        html = etree.HTML(con)
        dict = {}
        dict["title"]=html.xpath("//u[1]/text()")[0]
        print(dict["title"])
        print(dict)



    def run(self):
        response = self.parse_url(self.url)
        self.get_con_list(response)





if __name__ == '__main__':
    page=Page()
    page.run()
