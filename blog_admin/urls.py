from django.contrib import admin
from django.urls import include
from django.urls import path

from app.views import admin_index

urlpatterns = [
    path('', admin_index, name="index"),
    path('admin/', admin.site.urls, name="admin"),
    path('grappelli/', include('grappelli.urls'), name="grappelli"),
]
