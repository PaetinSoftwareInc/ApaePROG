from django.shortcuts import render


def index(request):
    return render(request, 'bpaeapp/index.html', {'section': 'index'})


def mission(request):
    return render(request, 'bpaeapp/mission.html', {'section': 'mission'})


def contact(request):
    return render(request, 'bpaeapp/contact.html', {'section': 'contact'})


def service(request):
    return render(request, 'bpaeapp/service.html', {'section': 'contact'})



