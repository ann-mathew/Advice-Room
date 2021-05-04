"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from advisors.views import add_advisor, list_advisor
from users.views import register_user, login_user
from bookings.views import create_booking, list_booking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advisor/', add_advisor),
    path('user/register/', register_user),
    path('user/login/', login_user),
    path('user/<str:user_id>/advisor/', list_advisor),
    path('user/<str:user_id>/advisor/<str:advisor_id>/', create_booking),
    path('user/<str:user_id>/advisor/booking', list_booking),
]
