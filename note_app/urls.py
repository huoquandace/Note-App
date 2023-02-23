
from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('note/add/', views.add_note, name='add'),
]
