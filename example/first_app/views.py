from django.shortcuts import render

def index(request):
    my_dict = {'insert':'some content'}
    return render(request, 'first_app/index.html', context=my_dict)

def first(request):
    diction = {'yes':'there it is'}
    return render(request, 'first_app/first.html', context=diction)
