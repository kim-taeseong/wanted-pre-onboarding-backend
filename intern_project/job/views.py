from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import *
# Create your views here.

def create_job(request):
    company_id = request.POST.get('회사_id')
    position = request.POST.get('채용포지션')
    reward = request.POST.get('채용보상금')
    content = request.POST.get('채용내용')
    technology = request.POST.get('사용기술')

    job = Job(company_id=company_id, position=position, reward=reward, content=content, technology=technology)
    job.save()
    return JsonResponse({'data': 'job posted!'}, status=201)

@ensure_csrf_cookie
def csrf_cookie(request):
    msg = {'data': 'csrf cookie created'}
    return JsonResponse(msg)