from django.http import HttpResponse

# from django.shortcuts import render


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, pk):
    return HttpResponse('Подробно про элемент {}'.format(pk))
