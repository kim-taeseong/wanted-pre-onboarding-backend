from django.shortcuts import render

from django.http import JsonResponse

from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

def job(request):
    return JsonResponse({'data': 'Ok'})

@ensure_csrf_cookie
def csrf_cookie(request):
    msg = {'data': 'csrf cookie created'}
    return JsonResponse(msg)