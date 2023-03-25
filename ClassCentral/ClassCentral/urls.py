from django.contrib import admin
import os
from django.urls import path
from hindi import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<slug:s1>/',views.myview, name='myview'),
    path('<slug:s1>/<slug:s2>/',views.myview2, name='myview2'),
    path('<slug:s1>/<slug:s2>/<slug:s3>/',views.myview3, name='myview3'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

