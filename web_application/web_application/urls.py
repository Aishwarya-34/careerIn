from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from web_application.app_core import views

urlpatterns = [
    path("", views.homepage, name="homepage"), #made by ash
    path("register", views.register_request, name="register"), #made by ash
    path('admin/', admin.site.urls),
    path('',views.homepage,name="home"),
    path('/upload', views.upload_resume, name = 'upload_resume'),
    path('resumes/', views.resume_list, name = 'resume_list'),
    path('resumes/<int:pk>/', views.delete_resume, name='delete_resume'),
   

    #path('', views.search_results, name='search_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


