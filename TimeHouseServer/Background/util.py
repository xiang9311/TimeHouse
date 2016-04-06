__author__ = '祥祥'

from datetime import datetime
from WebEditor.settings import BUCKEY_DOMAIN

DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def TimeUtil(time_format):

    def dataToStr(date):
        return date.strftime(time_format)

    return dataToStr

def getImageUrl200_200(imageName):
    return BUCKEY_DOMAIN + '/' + imageName + '?imageView2/1/w/200/h/200/q/90'

def getImageUrl(imageName):
    return BUCKEY_DOMAIN + '/' + imageName