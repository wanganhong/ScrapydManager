# -*- coding:utf-8 -*-  

""" 

@author:CrackM5
@file: scrapyd_manager.py
@time: 2017/11/10 15:56

"""

import os
import json
import subprocess

from config_parser import config
from utils import os_bits, source_path


class ScrapydManager(object):
    def __init__(self, curlpath, host="localhost", port=6800):
        self.__curlpath = curlpath
        self.__host = host
        self.__port = port

    def _execute_api(self, api):
        cmd_line = "{curl} http://{host}:{port}/{api}".format(
            curl=self.__curlpath,
            host=self.__host,
            port=self.__port,
            api=api)
        return subprocess.Popen(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    def daemon_status(self):
        pass

    def list_projects(self):
        api = "listprojects.json"
        stdout, _ = self._execute_api(api).communicate()
        results = json.loads(stdout)
        return results['projects']

    def list_spiders(self, project):
        api = "listspiders.json?project={project}".format(project=project)
        stdout, _ = self._execute_api(api).communicate()
        results = json.loads(stdout)
        return results['spiders']

    def list_jobs(self, project):
        api = "listjobs.json?project={project}".format(project=project)
        stdout, _ = self._execute_api(api).communicate()
        results = json.loads(stdout)
        return [item['id'] for item in results['running']] + [item['id'] for item in results['pending']]

    def schedule(self, project, spider):
        api = "schedule.json -d project={project} -d spider={spider}".format(project=project, spider=spider)
        stdout, _ = self._execute_api(api).communicate()
        return json.loads(stdout)

    def cancel(self, jobid, project=None):
        if project:
            api = "cancel.json -d project={project} -d job={job}".format(project=project, job=jobid)
        else:
            api = "cancel.json -d job={job}".format(job=jobid)
        stdout, _ = self._execute_api(api).communicate()
        return json.loads(stdout)


relativepath = source_path(r"libs\curl.exe") if os_bits() == 32 else source_path(r"libs\curl64.exe")
os.path.realpath(relativepath)
srapyd_manager = ScrapydManager(curlpath=os.path.realpath(relativepath), host=config.host, port=config.port)
