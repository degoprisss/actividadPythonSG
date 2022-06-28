from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def customers(request):
    return render(request, 'customers.html')

def contact(request):
    return render(request, 'contact.html')