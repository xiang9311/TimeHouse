__author__ = '祥祥'

from datetime import datetime

DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def TimeUtil(time_format):

    def dataToStr(date):
        return date.strftime(time_format)

    return dataToStr