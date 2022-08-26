from multiprocessing import context
from django.shortcuts import render
from .models import Product
from .forms import ApplyForm
from django.core.paginator import Paginator
# from .filters import ProductFilter
# Create your views here.


def productlist(request):
    product_list=Product.objects.all()
    
    # myfilter=ProductFilter(request.GET,queryset=product_list)
    # product_list= myfilter.qs
    
    paginator = Paginator(product_list, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    context={'product_list':product_list }
    # context={'product_list':product_list ,'myfilter':myfilter}
    return render(request,'Product/product_list.html',context)



def productdetail(request,slug):
    productdetail= Product.objects.get(proslug=slug)
    
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        print('test')
        if form.is_valid():
            myform = form.save(commit=False)
            myform.Product=productdetail
            myform.save()
            # form_test.created_by = request.user
            # form_test.save()
            print('done')
    else:
        form= ApplyForm()
    
    
    context={'productdetail':productdetail}
    return render(request,'Product/product_detail.html',context)
