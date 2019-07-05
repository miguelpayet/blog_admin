from django.shortcuts import render


def admin_index(request):
    context = {}
    response = render(request, 'app/index.html', context)
    return response
