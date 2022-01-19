
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.



def shop(request,c_slug=None):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prod=products.objects.filter(category=c_page, available=True)
    else:


    # ct=categ.objects.all()
        prod=products.objects.all().filter( available=True)
    cat=categ.objects.all()
    paginator=Paginator(prod,2)
    try:
        page=int(request.GET.get('page','1'))
    except Exception:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)            
    return render(request,'index.html',{'pr':prod,'ct':cat,'pg':pro})


def prodDetails(request,c_slug,product_slug):
    try:
        prodt=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
         raise e
    return render(request,'item.html',{'pr':prodt})


def searching(request):
    prod=None
    seach=None
    if' q' in request.GET:
        seach=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=seach)|Q(desc_contains=seach))


    return render(request,'search.html',{'qr':seach,'pr':prod})    