
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from careerIn import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
]
