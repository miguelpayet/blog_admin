from django.contrib import admin
from django.urls import path

from app.views import admin_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_index, name="index"),
]
