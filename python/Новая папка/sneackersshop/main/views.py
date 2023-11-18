from main.models import *
from urllib.request import HTTPRedirectHandler
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def main(request):
    card = Crosscard.objects.all()
    brand = Brand.objects.all()
    return render(request, 'index.html', {'brand': brand, 'card': card})

def more(request, id):
    try:
        more = Crosscard.objects.get(id=id)
        return render(request, 'base2.html', {'more': more})
    except:
        return render(request, 'a404.html')

def podrobno(request, id):
    # try:
        more = Crosscard.objects.get(id=id)
        return render(request, 'podrobno.html', {'more': more})
    # except:
    #     return render(request, 'a404.html')

def addCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    return HttpResponseRedirect('/')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    product_cart = Crosscard.objects.filter(id__in=cart_session)
    all_products_sum = 0
    for i in product_cart:
        i.count = cart_session.count(i.id)
        i.sum = i.count * i.price
        all_products_sum += i.sum

    return render(request, 'cart.html', {'count_of_product': count_of_product, 'product_cart': product_cart, 'all_products_sum': all_products_sum})

def removeCart(request, id):
    cart_session = request.session.get('cart_session', [])
    carts = cart_session
    carts.remove(id)
    request.session['cart_session'] = carts
    return HttpResponseRedirect('/basket')

def about(request):
    return render(request, 'about.html')

def signUp(request):
        if request.method == 'POST':
            user = UserCreationForm(request.POST)
            if user.is_valid():
                user.save()
                return HttpResponseRedirect('/')
        else:
            user = UserCreationForm()
        return render(request, 'auth.html', {'user': user})

def signin(request):
        try:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                form = AuthenticationForm()
            return render(request, 'auth.html', {'user': form})
        except UnboundLocalError:
            return render(request, 'a404.html')

def signout(request):
        logout(request)
        return HttpResponseRedirect('/')

def order(request):
    cart_session = request.session.get('cart_session', [])
    if request.method == 'POST':
        if len(cart_session) == 0:
            messages.error(request, 'Ваша корзина пуста', extra_tags='danger')
            return redirect('cart')
        else:
            customer = Crossc()
            customer.name = request.POST.get('c_name')
            customer.last_name = request.POST.get('c_lastname')
            customer.number = request.POST.get('c_number')
            customer.address = request.POST.get('c_addres')
            customer.message = request.POST.get('c_message')
            customer.save()
            for i in range(len(cart_session)):
                order= Order()
                cart_session = request.session.get('cart_session', [])
                cart_session_lst = cart_session
                set_list = set(cart_session_lst)
                product_names_add_counts = []
                for i in set_list:
                    product = Crosscard.objects.get(id = 1)
                    product_name = product.title
                    count = cart_session_lst.count(i)
                    products = f'{product_name} - {count}'
                    product_names_add_counts.append(products)
                products_cart = Crosscard.objects.filter(id__in = cart_session)
                all_products_sum = 0
                for i in products_cart:
                    i.count = cart_session.count(i.id)
                    i.sum = i.count * i.price
                    all_products_sum += i.sum
                order.product = product_names_add_counts
                order.customer = customer
                order.total_price = all_products_sum
                order.phone = customer.number
                order.address = customer.address
                order.save()

            request.session['cart_session'] = []
            messages.error(request, 'Заказ успешно отправлен!', extra_tags='success')
            return redirect('cart')


def basket(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    product_cart = Crosscard.objects.filter(id__in=cart_session)
    all_products_sum = 0
    for i in product_cart:
        i.count = cart_session.count(i.id)
        i.sum = i.count * i.price
        all_products_sum += i.sum

    return render(request, 'basket.html', {'count_of_product': count_of_product, 'product_cart': product_cart, 'all_products_sum': all_products_sum})