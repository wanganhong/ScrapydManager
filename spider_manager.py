# -*- coding:utf-8 -*-  

""" 

@author:CrackM5
@file: spider_manager.py 
@time: 2017/11/15 9:56

"""

from scrapyd_manager import srapyd_manager as sm


def get_spiders():
    """
    获取全部已部署爬虫（含其对应project映射）
    :return: {"spider1":"project1","spider2":"project2"}
    """
    spiders_dic = dict()
    projects = sm.list_projects()
    for project in projects:
        spiders = sm.list_spiders(project)
        for spider in spiders:
            spiders_dic[spider] = project
    return spiders_dic


def get_jobs():
    """
    获取全部正在运行的爬虫任务（含其对应project映射）
    :return: {"job1":"project1","job2":"project2"}
    """
    jobs_dic = dict()
    projects = sm.list_projects()
    for project in projects:
        jobs = sm.list_jobs(project)
        for job in jobs:
            jobs_dic[job] = project
    return jobs_dic


def stop_spiders():
    for job, project in get_jobs().items():
        print "To stop job: project={},job={}".format(project, job)
        sm.cancel(job, project)
    print "Finished!"


def start_spiders():
    for spider, project in get_spiders().items():
        print "To start spider: project={},spider={}".format(project, spider)
        sm.schedule(project, spider)
    print "Finished!"


if __name__ == '__main__':
    start_spiders()
