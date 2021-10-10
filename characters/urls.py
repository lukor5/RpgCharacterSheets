from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('diceroll', views.diceroll, name='diceroll'),
    path('mycharacters', views.mycharacters, name='mycharacters'),
    path('mycharacters/new/', views.newcharacter, name='new'),
    path('mycharacters/<int:pk>/', views.editcharacter, name='editcharacter'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)