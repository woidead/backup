from django.contrib import admin
from django.urls import path
from main.views import *
from fileapp.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('search', search, name='search'),
    path('more/<int:id>', more, name = 'more'),
    path('cart/', cart, name = 'cart'),
    path('addCart/<int:pk>', addCart, name='addCart'),
    path('removeCart/<int:id>', removeCart, name ='removeCart'),
    path('aboutus', about, name='about'),
    path('signup', signUp, name='signup'),
    path('signin', signin, name='signin'), 
    path('signout', signout, name='logout'),
    path('order/', order, name = 'order'),

]
urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
