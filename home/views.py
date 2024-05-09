from django.shortcuts import render,HttpResponse
from product.models import Product
# Create your views here.
def index(request):
    # return HttpResponse("<h1>hello world</h1>")
     return render(request, 'home/index.html')

def aboutus(request):
    # return HttpResponse("<h2>about us</h2>")
    
    return render(request, 'home/about.html')

def search_results(request):
    search_query = request.GET.get('search_query')

    if search_query:
        results = Product.objects.filter(name__icontains=search_query)
    else:
        results = []

    return render(request, 'home/search_results.html', {'results': results})
