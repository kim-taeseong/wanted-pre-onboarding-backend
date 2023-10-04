from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import *
# Create your views here.

def job(request):
    print(request)
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        position = request.POST.get('position')
        reward = request.POST.get('reward')
        content = request.POST.get('content')
        technology = request.POST.get('technology')

        job = Job(company_id=company_id, position=position, reward=reward, content=content, technology=technology)
        job.save()
        return JsonResponse({'data': 'job posted!'}, status=201)

@ensure_csrf_cookie
def csrf_cookie(request):
    msg = {'data': 'csrf cookie created'}
    return JsonResponse(msg)