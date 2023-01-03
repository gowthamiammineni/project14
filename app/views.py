from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'name':'ashu'}
    return render(request,'operations.html',d)