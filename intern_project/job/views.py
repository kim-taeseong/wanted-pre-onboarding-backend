from django.shortcuts import render

from django.http import JsonResponse
# Create your views here.

def job(request):
    return JsonResponse({'data': 'Ok'})