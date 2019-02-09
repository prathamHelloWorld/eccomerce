from django.shortcuts import render,get_object_or_404,Http404
from .models import Product

# Create your views here.
def productPage(request):
    product=Product
    context={
        'objects':product.objects.all().filter(active=True)
    }
    return render(request,'products.html',context)

def detailPage(request,slug,*args, **kwargs):
    product=get_object_or_404(Product,slug=slug,active=True)
    context={
        'object':product
    }
    return render(request,'details.html',context)


def featuredProducts(request):
    product=Product.objects.all().filter(featured=True,active=True)
    context={
        'objects':product
    }
    return render(request,'featured.html',context)

def featuredProduct(request,slug,*args, **kwargs):
    product=get_object_or_404(Product,slug=slug,featured=True,active=True)
    context={
        'object':product
    }
    return render(request,'featured_products.html',context)