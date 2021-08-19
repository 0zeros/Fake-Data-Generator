from dataGenerator.data_generator import data_generator
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from dataGenerator.test5 import test
from dataGenerator.middleware import middleware


# Create your views here.


@csrf_exempt
def dataGeneratorApi(request,id=0):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        print(data)
        return JsonResponse(middleware(data),safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        return JsonResponse(middleware(data),safe=False)
