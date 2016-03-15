__author__ = '祥祥'

import time

NAME_TIME_FORMAT = '%Y%m%d%H%M%S'

def getHtmlFileName(headName):
    return headName + time.strftime(NAME_TIME_FORMAT, time.localtime()) + '.html'
