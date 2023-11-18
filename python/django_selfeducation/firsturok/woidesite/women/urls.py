from django.urls import path, re_path

from women.views import *

urlpatterns = [
    path('home/', main, name='home'),
    path('cats/<int:catid>/', categories),
    path('slug/<slug:doggy>/', dog),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)

]
