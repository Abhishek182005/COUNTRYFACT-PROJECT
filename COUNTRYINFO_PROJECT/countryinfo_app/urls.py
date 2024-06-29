from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('country/', views.country_info, name='country_info'),
    path('compare/', views.country_compare, name='country_compare'),
    path('capitals/', views.country_and_capitals, name='country_and_capitals'),
    path('error/', views.error, name='error'),
    path('', views.landing_page, name='landing_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
