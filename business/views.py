from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')


