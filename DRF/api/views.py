from django.shortcuts import render
from .serializers import UserSerialier
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework import status
class NewUserView(APIView):
    def post(self, request):
        serializer = UserSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DRF(APIView):

   
#     def get(self, request):
        
#         return Response({'data':UserSerialier.get_users(self)})
    
@csrf_exempt
def user_api(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            usr = User.objects.get(id=id)
            serializer = UserSerialier(usr)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        usr = User.objects.all()
        serializer = UserSerialier(usr,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = UserSerialier(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'user created successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        usr = User.objects.get(id=id)
        serializer = UserSerialier(usr,data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'user updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    if request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        usr = User.objects.get(id=id)
        serializer = UserSerialier(usr,data=py_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'user updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    if request.method == 'DELETE':
        json_data= request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        usr = User.objects.get(id=id)
        usr.delete()
        res = {'msg':'user deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data)
        


@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        if id is not None:
            usr = User.objects.get(id=id)
            serializer = UserSerialier(usr)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        usr = User.objects.all()
        serializer = UserSerialier(usr,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    @csrf_exempt
    def post(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = UserSerialier(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'user created successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    def put(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        usr = User.objects.get(id=id)
        serializer = UserSerialier(usr,data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'user updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    def patch(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        usr = User.objects.get(id=id)
        serializer = UserSerialier(usr,data=py_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'user updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    def delete(self, request, *args, **kwargs):
        json_data= request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        usr = User.objects.get(id=id)
        usr.delete()
        res = {'msg':'user deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data)
    
@api_view(['GET','POST'])
def user_data(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            std = User.objects.get(id=id)
            serializer = UserSerialier(std)
            return Response(serializer.data)
        
        std = User.objects.all()
        serializer = UserSerialier(std, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = UserSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'user created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='DELETE':
        id = request.data.get('id')
        std = User.objects.get(pk=id)
        std.delete()
        return Response({'msg':'user deleted'})