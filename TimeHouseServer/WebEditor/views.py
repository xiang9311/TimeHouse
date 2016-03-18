from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from . import settings as USettings
import os
import json
from django.views.decorators.csrf import csrf_exempt
import datetime,random
from urllib import parse
from urllib import request as urlRequest
from importlib import import_module
from qiniu import Auth, put_file
from TimeHouseServer import logger, settings
from .constant import constant

# service is here
from .service import organizationService, articleService

# Create your views here.

KEY_USER_ID = 'userid'

SUCCESS = 'SUCCESS'
ERROR = 'ERROR'
# KEYS = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
#         'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
#         '1','2','3','4','5','6','7','8','9','0']
# keys_length = len(KEYS)
# max_length = 7
#
# def generatorKey():
#     """
#     获取随机生成的图片名
#     :return:
#     """
#     import random
#     data = constant.getCurrentFileName()
#     for i in range(0, max_length):
#         data += KEYS[int(random.uniform(0, keys_length))]
#     return data


def getToken(request):
    """
    获取七牛token
    :param request:
    :return:
    """
    token = USettings.getQiniuTokenWithoutKey()
    tokenDict = {}
    tokenDict['uptoken'] = token
    return HttpResponse(json.dumps(tokenDict, ensure_ascii=False))

def editorPage(request):
    """
    获取编辑内容页
    :param request:
    :return:
    """
    pageType = request.GET.get('type','textEditor')
    return render(request, 'WebEditor/'+pageType+'.html')


def userDetail(request):
    """
    用户详情
    :param request:
    :return:
    """
    if not request.session.get(KEY_USER_ID, ''):
        return render(request, 'WebEditor/login.html')
    else:
        return render(request, 'WebEditor/userDetail.html')


@csrf_exempt
def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 注册成功后跳转
        # 获取注册内容
        logger.debug(str(request.POST))
        avatar_url = request.POST.get('avatar', '')
        invite_code = request.POST.get('code', '')
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        espassword = request.POST.get('espassword', '')
        wx_number = request.POST.get('wxNumber', '')
        wb_name = request.POST.get('wbName', '')

        if organizationService.addOrganization(avatar_url, user_name, password, wx_number, wb_name):
            return HttpResponseRedirect('/web/login/')
        else:
            # 名字已被使用
            return HttpResponse('名字已被使用')


    else:
        return render(request, 'WebEditor/register.html')

def login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        suc, userid = organizationService.checkOrganizationPassword(username, password)
        if suc:
            request.session[KEY_USER_ID] = userid
            return HttpResponseRedirect('/web/userDetail/')
        else:
            return render(request, 'WebEditor/login.html', {'passworderror':True})


    else:
        return render(request, 'WebEditor/login.html')

@csrf_exempt
def postTextContent(request):
    userId = request.session.get(KEY_USER_ID, '')
    if not userId:
        return HttpResponse('你还未登录或登录已过期')

    print(str(request.POST))

    articleType = 2  # 普通文章

    cover = request.POST.get('cover', '')
    title = request.POST.get('title')
    subContent = request.POST.get('subContent')
    category = request.POST.get('category')
    contentType = request.POST.get('contentType')
    content = request.POST.get('content')
    print('cover is ', cover)
    if not (content and title and cover):
        return HttpResponse('还未填写内容或title或未选择cover图')

    if articleService.addTextArticle(userId, cover, title, subContent, category, contentType, articleType, content):
        return HttpResponse(SUCCESS)
    else:
        return HttpResponse(ERROR)



@csrf_exempt
def postContent(request):
    """
    提交最后的编辑内容  web内容
    :param request:
    :return:
    """
    userId = request.session.get(KEY_USER_ID, '')
    if not userId:
        return HttpResponse('你还未登录或登录已过期')

    user_name = organizationService.getOrganizationNameById(userId)

    if not user_name:
        return HttpResponse('未找到对应组织名')

    print(str(request.POST))

    articleType = 1  # web

    cover = request.POST.get('cover', '')
    title = request.POST.get('title')
    subContent = request.POST.get('subContent')
    category = request.POST.get('category')
    contentType = request.POST.get('contentType')
    content = request.POST.get('content')

    # 插入 <meta charset="UTF-8">
    # replace 方法不会改变原字符串，会返回替换后的内容。学java的表示呵呵呵
    content = content.replace('<head>', '<head><title>'+title+
                              '</title><meta charset="UTF-8">' +
                              '<script type="text/javascript" src="http://101.200.84.75:8999/static/WebEditor/Adaptive.js"></script>'
                              , 1)
    content = content.replace('<body >', '<body><div class="box">', 1)  # 使用<body >因为h5就只这么生成的啊啊啊
    body_last_index = content.rfind('</body>')
    content = content[:body_last_index] + '</div>' + content[body_last_index:]

    #创建文件 settings.STATIC_ROOT + filename
    file_name = constant.getHtmlFileName(category)
    path = settings.STATIC_ROOT + '/' + user_name
    file = path + '/' + file_name
    if not os.path.exists(path):
        os.mkdir(path)
    html = open(file, 'w', encoding='utf-8')
    html.write(content)
    html.close()

    contentUrl = "http://101.200.84.75:8999/static/" + user_name + '/' + file_name

    if articleService.addWebArticle(userId, cover, title, subContent, category, contentType, articleType, content, contentUrl):
        return HttpResponse(json.dumps({'status':SUCCESS, 'contentUrl':contentUrl}, ensure_ascii=False))
    else:
        return HttpResponse(json.dumps({'status':ERROR, 'message' :'失败啦，请重试或者联系工程师'}, ensure_ascii=False))



def editor(request):
    return render(request, 'WebEditor/index.html')

def get_path_format_vars():
    return {
        "year":datetime.datetime.now().strftime("%Y"),
        "month":datetime.datetime.now().strftime("%m"),
        "day":datetime.datetime.now().strftime("%d"),
        "date": datetime.datetime.now().strftime("%Y%m%d"),
        "time":datetime.datetime.now().strftime("%H%M%S"),
        "datetime":datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        "rnd":random.randrange(100,999)
    }

#保存上传的文件
def save_upload_file(PostFile,FilePath):
    try:
        f = open(FilePath, 'wb')
        for chunk in PostFile.chunks():
            f.write(chunk)
    except Exception as E:
        f.close()
        return u"写入文件错误:"+ E.message
    f.close()
    return u"SUCCESS"

#保存上传文件到七牛
def save_upload_file_to_qiniu(upload_file,key):
    try:
        from qiniu import Auth,put_file,put_data
        token = USettings.getQiniuToken(key)
        # ret, info = put_file(token, key, upload_file)
        ret, info = put_data(token, key, upload_file)
        if ret.get('key',None) == None:
            raise Exception('upload error')
        else:
            return "SUCCESS"
    except Exception as e:
        print(str(e))


@csrf_exempt
def get_ueditor_settings(request):
    return HttpResponse(json.dumps(USettings.UEditorUploadSettings,ensure_ascii=False), content_type="application/javascript")
@csrf_exempt
def get_ueditor_controller(request):
    """获取ueditor的后端URL地址    """

    action=request.GET.get("action","")
    reponseAction={
        "config":get_ueditor_settings,
        "uploadimage":UploadFile,
        "uploadscrawl":UploadFile,
        "uploadvideo":UploadFile,
        "uploadfile":UploadFile,
        "catchimage":catcher_remote_image,
        "listimage":list_files,
        "listfile":list_files
    }
    return reponseAction[action](request)


@csrf_exempt
def list_files(request):
    """列出文件"""
    if request.method!="GET":
        return  HttpResponse(json.dumps(u"{'state:'ERROR'}") ,content_type="application/javascript")
    #取得动作
    action=request.GET.get("action","listimage")

    allowFiles={
        "listfile":USettings.UEditorUploadSettings.get("fileManagerAllowFiles",[]),
        "listimage":USettings.UEditorUploadSettings.get("imageManagerAllowFiles",[])
    }
    listSize={
        "listfile":USettings.UEditorUploadSettings.get("fileManagerListSize",""),
        "listimage":USettings.UEditorUploadSettings.get("imageManagerListSize","")
    }
    listpath={
        "listfile":USettings.UEditorUploadSettings.get("fileManagerListPath",""),
        "listimage":USettings.UEditorUploadSettings.get("imageManagerListPath","")
    }
    #取得参数
    list_size=int(request.GET.get("size",listSize[action]))
    list_start=int(request.GET.get("start",0))

    files=[]
    root_path=os.path.join(USettings.gSettings.MEDIA_ROOT,listpath[action]).replace("\\","/")
    files=get_files(root_path,root_path,allowFiles[action])

    if (len(files)==0):
        return_info={
            "state":u"未找到匹配文件！",
            "list":[],
            "start":list_start,
            "total":0
        }
    else:
        return_info={
            "state":"SUCCESS",
            "list":files[list_start:list_start+list_size],
            "start":list_start,
            "total":len(files)
        }

    return HttpResponse(json.dumps(return_info),content_type="application/javascript")


def get_files(root_path,cur_path, allow_types=[]):
    files = []
    items = os.listdir(cur_path)
    for item in items:
        # item=unicode(item)
        item_fullname = os.path.join(root_path,cur_path, item).replace("\\", "/")
        if os.path.isdir(item_fullname):
            files.extend(get_files(root_path,item_fullname, allow_types))
        else:
            ext = os.path.splitext(item_fullname)[1]
            is_allow_list= (len(allow_types)==0) or (ext in allow_types)
            if is_allow_list:
                files.append({
                    "url":parse.urljoin(USettings.gSettings.MEDIA_URL ,os.path.join(os.path.relpath(cur_path,root_path),item).replace("\\","/" )),
                    "mtime":os.path.getmtime(item_fullname)
                })

    return files


@csrf_exempt
def UploadFile(request):
    """上传文件"""
    if not request.method=="POST":
        return  HttpResponse(json.dumps(u"{'state:'ERROR'}"),content_type="application/javascript")

    state="SUCCESS"
    action=request.GET.get("action")
    #上传文件
    upload_field_name={
        "uploadfile":"fileFieldName","uploadimage":"imageFieldName",
        "uploadscrawl":"scrawlFieldName","catchimage":"catcherFieldName",
        "uploadvideo":"videoFieldName",
    }
    UploadFieldName=request.GET.get(upload_field_name[action],USettings.UEditorUploadSettings.get(action,"upfile"))

    #上传涂鸦，涂鸦是采用base64编码上传的，需要单独处理
    if action=="uploadscrawl":
        upload_file_name="scrawl.png"
        upload_file_size=0
    else:
        #取得上传的文件
        file=request.FILES.get(UploadFieldName,None)
        if file is None:return  HttpResponse(json.dumps(u"{'state:'ERROR'}") ,content_type="application/javascript")
        upload_file_name=file.name
        upload_file_size=file.size

    #取得上传的文件的原始名称
    upload_original_name,upload_original_ext=os.path.splitext(upload_file_name)

    #文件类型检验
    upload_allow_type={
        "uploadfile":"fileAllowFiles",
        "uploadimage":"imageAllowFiles",
        "uploadvideo":"videoAllowFiles"
    }
    if action in upload_allow_type:
        allow_type= list(request.GET.get(upload_allow_type[action],USettings.UEditorUploadSettings.get(upload_allow_type[action],"")))
        if not upload_original_ext.lower()  in allow_type:
            state=u"服务器不允许上传%s类型的文件。" % upload_original_ext

    #大小检验
    upload_max_size={
        "uploadfile":"filwMaxSize",
        "uploadimage":"imageMaxSize",
        "uploadscrawl":"scrawlMaxSize",
        "uploadvideo":"videoMaxSize"
    }
    max_size=int(request.GET.get(upload_max_size[action],USettings.UEditorUploadSettings.get(upload_max_size[action],0)))
    if  max_size!=0:
        from .utils import FileSize
        MF=FileSize(max_size)
        if upload_file_size > MF.size:
            state=u"上传文件大小不允许超过%s。" % MF.FriendValue

    #检测保存路径是否存在,如果不存在则需要创建
    upload_path_format={
        "uploadfile":"filePathFormat",
        "uploadimage":"imagePathFormat",
        "uploadscrawl":"scrawlPathFormat",
        "uploadvideo":"videoPathFormat"
    }

    path_format_var=get_path_format_vars()
    path_format_var.update({
        "basename":upload_original_name,
        "extname":upload_original_ext[1:],
        "filename":upload_file_name,
    })
    #取得输出文件的路径
    OutputPathFormat,OutputPath,OutputFile=get_output_path(request,upload_path_format[action],path_format_var)

    #所有检测完成后写入文件
    if state=="SUCCESS":
        if action=="uploadscrawl":
            state=save_scrawl_file(request, os.path.join(OutputPath,OutputFile))
        else:
            #保存到文件中，如果保存错误，需要返回ERROR
            upload_module_name = USettings.UEditorUploadSettings.get("upload_module", None)
            if upload_module_name:
                mod = import_module(upload_module_name)
                state = mod.upload(file, OutputPathFormat)
            else:
                state = save_upload_file_to_qiniu(file, OutputPathFormat)

    #返回数据
    return_info = {
        'url': parse.urljoin(USettings.BUCKEY_DOMAIN , OutputPathFormat) ,                # 保存后的文件名称
        'original': upload_file_name,                  #原始文件名
        'type': upload_original_ext,
        'state': state,                         #上传状态，成功时返回SUCCESS,其他任何值将原样返回至图片上传框中
        'size': upload_file_size
    }
    return HttpResponse(json.dumps(return_info,ensure_ascii=False),content_type="application/javascript")

@csrf_exempt
def catcher_remote_image(request):
    """远程抓图，当catchRemoteImageEnable:true时，
        如果前端插入图片地址与当前web不在同一个域，则由本函数从远程下载图片到本地
    """
    if not request.method=="POST":
        return  HttpResponse(json.dumps( u"{'state:'ERROR'}"),content_type="application/javascript")

    state="SUCCESS"

    allow_type= list(request.GET.get("catcherAllowFiles",USettings.UEditorUploadSettings.get("catcherAllowFiles","")))
    max_size=int(request.GET.get("catcherMaxSize",USettings.UEditorUploadSettings.get("catcherMaxSize",0)))

    remote_urls=request.POST.getlist("source[]",[])
    catcher_infos=[]
    path_format_var=get_path_format_vars()

    for remote_url in remote_urls:
        #取得上传的文件的原始名称
        remote_file_name=os.path.basename(remote_url)
        remote_original_name,remote_original_ext=os.path.splitext(remote_file_name)
        #文件类型检验
        if remote_original_ext  in allow_type:
            path_format_var.update({
                "basename":remote_original_name,
                "extname":remote_original_ext[1:],
                "filename":remote_original_name
            })
            #计算保存的文件名
            o_path_format,o_path,o_file=get_output_path(request,"catcherPathFormat",path_format_var)
            o_filename=os.path.join(o_path,o_file).replace("\\","/")
            #读取远程图片文件
            try:
                remote_image=urlRequest.urlopen(remote_url)
                 #将抓取到的文件写入文件
                try:
                    f = open(o_filename, 'wb')
                    f.write(remote_image.read())
                    f.close()
                    state="SUCCESS"
                except Exception as E:
                    state=u"写入抓取图片文件错误:%s" % E.message
            except Exception as E:
                state=u"抓取图片错误：%s" % E.message

            catcher_infos.append({
                "state":state,
                "url":parse.urljoin(USettings.gSettings.MEDIA_URL , o_path_format),
                "size":os.path.getsize(o_filename),
                "title":os.path.basename(o_file),
                "original":remote_file_name,
                "source":remote_url
            })

    return_info={
        "state":"SUCCESS" if len(catcher_infos) >0 else "ERROR",
        "list":catcher_infos
    }

    return HttpResponse(json.dumps(return_info,ensure_ascii=False),content_type="application/javascript")


def get_output_path(request,path_format,path_format_var):
    #取得输出文件的路径
    OutputPathFormat=(request.GET.get(path_format,USettings.UEditorSettings["defaultPathFormat"]) % path_format_var).replace("\\","/")
    #分解OutputPathFormat
    OutputPath,OutputFile=os.path.split(OutputPathFormat)
    print('OutputPath : %s, OutputFile : %s, OutputPathFormat : %s' % (OutputPath, OutputFile, OutputPathFormat))
    OutputPath=os.path.join(USettings.gSettings.MEDIA_ROOT,OutputPath)
    if not OutputFile:#如果OutputFile为空说明传入的OutputPathFormat没有包含文件名，因此需要用默认的文件名
        OutputFile=USettings.UEditorSettings["defaultPathFormat"] % path_format_var
        OutputPathFormat=os.path.join(OutputPathFormat,OutputFile)
    if not os.path.exists(OutputPath):
        print('OutputPath is %s' % OutputPath)
        os.makedirs(OutputPath)
    return ( OutputPathFormat,OutputPath,OutputFile)

#涂鸦功能上传处理
@csrf_exempt
def save_scrawl_file(request,filename):
    import base64
    try:
        content=request.POST.get(USettings.UEditorUploadSettings.get("scrawlFieldName","upfile"))
        f = open(filename, 'wb')
        f.write(base64.decodestring(content))
        f.close()
        state="SUCCESS"
    except Exception as E:
        state="写入图片文件错误:%s" % E.message
    return state
