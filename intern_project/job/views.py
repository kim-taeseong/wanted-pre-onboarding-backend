from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import *

import json
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

def update_job(request, id):
    job = Job.objects.get(id=id)

    data = json.loads(request.body.decode('utf-8'))

    job.position = data.get('채용포지션')
    job.reward = data.get('채용보상금')
    job.content = data.get('채용내용')
    job.technology = data.get('사용기술')

    job.save()

    return JsonResponse({'data': 'job updated!'}, status=200)

@ensure_csrf_cookie
def csrf_cookie(request):
    msg = {'data': 'csrf cookie created'}
    return JsonResponse(msg)