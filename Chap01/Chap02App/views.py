#encoding:UTF-8
from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core import serializers


from .createImage import generate
from django.urls.base import reverse

from django.views.decorators.http import etag
import hashlib
from .models import Person


def generate_etag(request,width,height):
    content = "{0}x{1}".format(width,height)
    return hashlib.sha1(content.encode(encoding='utf_8', errors='strict')).hexdigest()

def check(request):
    method = request.method
    username = ''
    password = ''
    if method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    if method == "GET":
        username = request.GET["username"]
        password = request.GET["password"]
    result = Person.objects.filter(username=username,password=password)
    print(result)
    if (len(result)>0):
        personData = []
        person = Person.objects.all()
        for p in person:
            personInfo = {}
            personInfo["username"] = p.username
            personInfo["password"] = p.password
            personInfo["id"] = p.id
            personData.append(personInfo)
        context = {'data':personData}
        return render(request, "list.html", context)
    else:
        return HttpResponse("登录失败")
    

#     return JsonResponse(dict(data = personData))
#     return HttpResponse(jsonData)
 

        
def userdelete(request):
    id = request.path.split('/')[-1]
    user = Person.objects.filter(id = id)
    user.delete()
    return HttpResponse("删除成功")  
#     HttpResponseRedirect("list.html")           
        

def login(request):
    return render(request,'login.html')    
# Create your views here.
def index(request):
    example = reverse('placeholder',kwargs={'width':50,'height':50})
    context = { 'example' : request.build_absolute_uri(example)}
    return render(request, 'home.html',context)

@etag(generate_etag)
def image(request,width,height):
    return HttpResponse(generate(int(width),int(height)),content_type="image/png")