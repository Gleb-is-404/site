"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news.views import index, add_data, signup, handle_request, main_page, login, handle
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('handle/', handle, name='handle'),
    path('handle_request/', handle_request, name='handle_request'),
    path('admin/', admin.site.urls),
    path('news/', index, name='news'),
    path('add_data/', add_data, name='add_data'),
    path('signup/',signup, name='signup'),
    path('main_page/',main_page, name='main_page'),
    path('login/',login, name='login'),


]
