# -*- coding:utf-8 -*-  

""" 

@author:CrackM5
@file: utils.py 
@time: 2017/11/10 17:14

"""

import sys
import os
import platform


def machine():
    """Return type ofmachine."""
    if os.name == 'nt' and sys.version_info[:2] < (2, 7):
        return os.environ.get("PROCESSOR_ARCHITEW6432",
                              os.environ.get('PROCESSOR_ARCHITECTURE', ''))
    else:
        return platform.machine()


def os_bits(machine=machine()):
    """Return bitness ofoperating system, or None if unknown."""
    machine2bits = {'AMD64': 64, 'x86_64': 64, 'i386': 32, 'x86': 32}
    return machine2bits.get(machine, None)


class LazyProperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value


def source_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    pwd = os.path.split(os.path.realpath(__file__))[0]
    return os.path.join(pwd, relative_path)
