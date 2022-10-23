from django.http import HttpResponse

# from django.shortcuts import render


def description(request):
    return HttpResponse('О проекте')
