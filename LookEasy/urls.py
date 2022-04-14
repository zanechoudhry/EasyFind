"""LookEasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Core import views as core_views
from food import views as food_views
from flights import views as flight_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('join/', core_views.join, name='join'),
    path('login/', core_views.user_login, name='user_login'),
    path('logout/', core_views.user_logout, name='user_logout'),
    path('save_res/', food_views.saved_res, name='saved_res'),
    path('settings/', core_views.settings, name='settings'),
    path('restaurants/', food_views.home, name='food_home'),
    path('flights/', flight_views.home, name='flight_home'),
    path('restaurants/results', food_views.results, name='food_results'),
    path('flights/results', flight_views.results, name='flight_results'),
    path("save_res/<int:id>", food_views.save, name='save_res'),
    path("unsave_res/<int:id>", food_views.unsave, name='unsave_res')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
