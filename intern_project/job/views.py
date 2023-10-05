from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import *

import json
# Create your views here.

def job(request):
    if request.method == 'GET':
        search = request.GET.get('search')

        if search:
            filter_job = Job.objects.filter(Q(company__name__icontains=search) | Q(position__icontains=search) | Q(reward__icontains=search) | Q(content__icontains=search) | Q(technology__icontains=search))
            data_job = [{"채용공고_id": job.id, "회사명": job.company.name, "국가": job.company.country, "지역": job.company.region, "채용포지션": job.position, "채용보상금": job.reward, "사용기술": job.technology} for job in filter_job]

            return JsonResponse(data_job, safe=False)

        else:
            all_job = Job.objects.all()
            data_job = [{"채용공고_id": job.id, "회사명": job.company.name, "국가": job.company.country, "지역": job.company.region, "채용포지션": job.position, "채용보상금": job.reward, "사용기술": job.technology} for job in all_job]

            return JsonResponse(data_job, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        company_id = data.get('회사_id')
        position = data.get('채용포지션')
        reward = data.get('채용보상금')
        content = data.get('채용내용')
        technology = data.get('사용기술')

        job = Job(company_id=company_id, position=position, reward=reward, content=content, technology=technology)
        job.save()

        return JsonResponse({'data': 'job posted!'}, status=201)

def job_id(request, id):
    if request.method == 'GET':
        job = Job.objects.get(id=id)
        company_job = Job.objects.filter(company_id=job.company.id)
        other_job = []
        for temp_job in company_job:
            if temp_job.id == job.id:
                continue
            other_job.append(temp_job.id)
        data_job = {"채용공고_id": job.id, "회사명": job.company.name, "국가": job.company.country, "지역": job.company.region, "채용포지션": job.position, "채용보상금": job.reward, "사용기술": job.technology, "채용내용": job.content, "회사가올린다른채용공고": other_job}

        return JsonResponse(data_job, safe=False)
    
    elif request.method == 'PUT':
        job = Job.objects.get(id=id)

        data = json.loads(request.body.decode('utf-8'))

        job.position = data.get('채용포지션')
        job.reward = data.get('채용보상금')
        job.content = data.get('채용내용')
        job.technology = data.get('사용기술')

        job.save()

        return JsonResponse({'data': 'job updated!'}, status=200)

    elif request.method == 'DELETE':
        job = Job.objects.get(id=id)
        job.delete()

        return JsonResponse({'data': 'job deleted!'}, status=204)

@ensure_csrf_cookie
def csrf_cookie(request):
    msg = {'data': 'csrf cookie created'}
    return JsonResponse(msg)