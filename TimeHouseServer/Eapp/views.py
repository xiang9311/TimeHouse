from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http.response import HttpResponse
from .models import UserOption
from WebEditor.constant.constant import getDatabaseTimeNow
# Create your views here.

def getIp(request):
    """
    获取请求用户的ip地址
    :param request:
    :return:
    """
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip =  request.META['HTTP_X_FORWARDED_FOR']
        return ip
    else:
        ip = request.META['REMOTE_ADDR']
        return ip

def appDes(request):
    return render(request, 'Eapp/webapp.html')

@csrf_exempt
def choose(request):
    user_option = request.POST.get('option', '')
    if request.session.get('choose', '') == 'choosed':
        return HttpResponse("choosed")

    request.session['choose'] = 'choosed'

    if user_option:
        option = UserOption()
        option.ip = getIp(request)
        option.choose_time = getDatabaseTimeNow()
        if user_option == 'like':
            option.choise = True
            pass
        elif user_option == 'dislike':
            option.choise = False
            pass
        else:
            option.choise = True
            pass
        option.save()
    else:
        pass
    return HttpResponse("ok")