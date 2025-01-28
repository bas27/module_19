from django.urls import path
from .views import sign_up_by_django, shop, get_buyers
from django.views.generic import TemplateView


urlpatterns = [
    path('sign/', sign_up_by_django, name='sign_up_by_django'),
    path('shop/', shop, name='shop'),
    path('', TemplateView.as_view(template_name='first_task/main.html')),
    path('basket/', TemplateView.as_view(template_name='first_task/basket.html')),
    path('buyers/', get_buyers, name='get_buyers'),
]
