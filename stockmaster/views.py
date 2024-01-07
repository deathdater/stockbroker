from django.shortcuts import render

# Create your views here.
def landing_page(request,*args,**kwargs):
    return render (request,'stockbrokerbase/base2.html')
    