from django.shortcuts import render
from django.http import HttpResponse
from drop.models import Note
import datetime
from django.utils import timezone
import time

import json
import hashlib  
import qrcode
from django.utils.six import BytesIO
import binascii
import base64
# Create your views here.
def index(request):
    #question='kdkdkkdkdkdkkd'
    return render(request, 'drop/index.html')
    #return HttpResponse("Hello, world. You're at the drop index.")

def submit(request):
    NoteId = str(request.GET.get('a'))
    timenow=str(time.time())
    print(timenow)
    if NoteId=="isEmpty":
        NoteId = hashlib.md5(timenow.encode(encoding='gb2312')).hexdigest()[8:-8]
        NoteContent=str(request.GET.get('b'))
        q = Note(NoteId=NoteId,NoteContent=NoteContent)
        q.save()
        return_json = {'cmd':"write",'NoteId':NoteId}
    else:
        try:
            noteinfo = Note.objects.get(NoteId = NoteId)
            return_json = {'cmd':"load",'NoteContent':noteinfo.NoteContent}
        except:
            NoteId =hashlib.md5(timenow.encode(encoding='gb2312')).hexdigest()[8:-8]
            NoteContent=str(request.GET.get('b'))
            if NoteContent != "isEmpty":
                NoteContent =  NoteContent.replace("\\r\\n","<br>")
                NoteContent =  NoteContent.replace("\\s"," ")
                q = Note(NoteId=NoteId,NoteContent=NoteContent)
                q.save()
                return_json = {'cmd':"write",'NoteId':NoteId}
    return HttpResponse(json.dumps(return_json), content_type='application/json')

def genqrcode(request):
        website=str(request.GET.get('a'))
        print("url",request.get_host())
        if(len(website) != 0):
                img = qrcode.make(request.get_host()+"/drop/raw/"+str(website))
                buf = BytesIO()
                img.save(buf)
                image_stream = buf.getvalue()
                #print("imagestream",image_stream)
                image_stream = base64.b64encode(image_stream) #transfer byte to base64
                #print(image_stream)
                response = HttpResponse(image_stream,content_type="image/png")
                #print("response",response)
                return response
        return HttpResponse(u"网址不能为空！")

def raw(request,NoteId):
    try:
        noteinfo =Note.objects.get(NoteId = NoteId)
        result=noteinfo.NoteContent
        print("result",result)
        result=result.replace(  "\n", "<br>");
        result=result.replace(  " ", "&nbsp");
    except:
        result="Not exist!"
    return HttpResponse(result)

def genrawlink(request):
        noteinfo=str(request.GET.get('a'))
        rawlink="http://"+request.get_host()+"/drop/raw/"+str(noteinfo)
        return HttpResponse(rawlink)

# def add(request,NoteId,NoteContent):
#     q = Note(NoteId=NoteId,NoteContent=NoteContent, pub_date=timezone.now())
#     q.save()
#     return HttpResponse("Note Content  %s saved." % q.NoteContent)

# def add(request):
#     NoteId = str(request.GET.get('a'))
#     NoteContent=str(request.GET.get('b'))
#     q = Note(NoteId=NoteId,NoteContent=NoteContent)
#     q.save()
#     return_json = {'cmd':"succeed"}
#     return HttpResponse(json.dumps(return_json), content_type='application/json')

# def read(request,NoteId):
#     q = Note.objects.get(NoteId=NoteId)
#     return HttpResponse("Note Content: %s."  %q.NoteContent)

# def read(request):
#     NoteId = str(request.GET.get('a'))
#     q = Note.objects.get(NoteId=NoteId)
#     return_json = {'content':q.NoteContent}
#     #print(return_json)
#     return HttpResponse(json.dumps(return_json), content_type='application/json')