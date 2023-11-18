from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def shopdetails(request):
    return render(request,'shop-details.html')
def shopingcard(request):
    return render(request,'shoping-cart.html')