# -*- coding:utf-8 -*-  

""" 

@author:CrackM5
@file: main.py 
@time: 2017/11/15 9:24

"""

import argparse

from spider_manager import start_spiders, stop_spiders

__version__ = 20171115


def sub_cmd(args):
    if args.mode == 'startSpiders':
        start_spiders()
    else:
        stop_spiders()


def main():
    parser = argparse.ArgumentParser(description='Scrapy manager:' + str(__version__))
    parser.add_argument('-v', '--version', action='version', version=str(__version__))

    parser.add_argument('-m', '--mode', choices=['startSpiders', 'stopSpiders'], required=True, action='store',
                        help='Start or stop spiders in scrapyd!')
    parser.set_defaults(func=sub_cmd)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
