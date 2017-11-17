# -*- coding:utf-8 -*-  

""" 

@author:CrackM5
@file: config_parser.py 
@time: 2017/11/10 17:28

"""

import ConfigParser

from utils import LazyProperty, source_path


class ConfigParse(object):
    def __init__(self, config_file='config.ini'):
        self.parser = ConfigParser.ConfigParser()
        self.parser.read(source_path(config_file))
        self.__host = None

    @LazyProperty
    def host(self):
        return self.parser.get("SCRAPYD", "host")

    @LazyProperty
    def port(self):
        return self.parser.getint("SCRAPYD", "port")


config = ConfigParse()

