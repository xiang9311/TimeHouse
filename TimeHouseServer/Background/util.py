__author__ = '祥祥'

from datetime import datetime

DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def TimeUtil(time_format):

    def dataToStr(date):
        return date.strftime(time_format)

    return dataToStr

def getImageUrl200_200(imageName):
    return 'http://7xo9gq.com1.z0.glb.clouddn.com/' + imageName + '?imageView2/1/w/200/h/200/q/90'

def getImageUrl(imageName):
    return 'http://7xo9gq.com1.z0.glb.clouddn.com/' + imageName + ''