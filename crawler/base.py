#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   jiehua233@gmail.com
# @site     http://chenjiehua.me
# @date     2015-12-15
#

import sys
import requests

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

"""
IP struct:
    ip = {
        "ip": "127.0.0.1",
        "port": "8888",
        "info": "XXXXX",
        "type": 1,     # type, 1: 透明, 2: 匿名, 3: 高匿名
    }

"""

class Base:
    """ Daily.py Hourly.py 公共基础类 """

    def crawl(self):
        """ 针对不同网站做特化 """
        pass

    def get(self, url, encoding=None, headers=None):
        print url
        try:
            r = requests.get(url)
            if encoding:
                r.encoding = encoding

            if r.status_code == requests.codes.ok:
                soup = BeautifulSoup(r.text, "html5lib")
                return self.parse(soup)
            else:
                raise Exception("HTTP Response Code: %s" % r.status_code)

        except Exception as e:
            print e

        return []

    def parse(self, soup):
        """ 针对不同网站做特化 """
        pass

