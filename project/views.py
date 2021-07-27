from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.models import Signup
from .serializers import *
import bcrypt

@api_view(['POST'])
def register(request):
    if request.method=='POST':
        name=request.POST.get("name")
        username=request.POST.get("username")
        password=request.POST.get("password")
    password=password.encode('utf-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    check=Signup.objects.filter(username=username)
    if len(check)==0:
        print(name)
        obj=Signup(name=name, username=username,password=password)
        obj.save()
        return Response({'Success':True,'msg':'account created'})
    else:
        return Response({"msg":'check your information'})

@api_view(['GET'])
def show(request):
    all=Signup.objects.all()
    all=SignupSerializer(all,many=True)
    
    return Response({"data":all.data})

@api_view(['POST'])
def login(request):
    username=request.POST.get("username")
    passw=request.POST.get("password")
    checklen=0

    check=Signup.objects.filter(username=username)
    hashpassword=bytes(check[0].password,encoding = 'utf-8')
    passenc=passw.encode('utf-8')
    print(list(check))

    if len(check)>0:
        checklen=1
    
    if checklen==1:

        if (bcrypt.checkpw(passenc, hashpassword)):
            

            return Response({'Success':True,'msg':('User Id '+str(check[0].id))})
        else:
            return Response({'Success':False,'msg':'Failed'})

    
    return Response({"msg":'Failed'})

# Create your views here.
