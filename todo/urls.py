from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("todo-admin/", admin.site.urls),
    path("", include("main.urls")),
]
