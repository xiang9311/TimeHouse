__author__ = '祥祥'

import time

NAME_TIME_FORMAT = '%Y-%m-%d%H%M%S'
SERVER_TIME_FORMAT = '%Y-%m-%d %X'

def getHtmlFileName(headName):
    return headName + time.strftime(NAME_TIME_FORMAT, time.localtime()) + '.html'

def getCurrentFileName():
    return time.strftime('%Y%m%d%H%M%S', time.localtime())

def getDatabaseTimeNow():
    return time.strftime(SERVER_TIME_FORMAT, time.localtime(time.time()))
