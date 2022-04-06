from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('portfolio/', views.index, name='index'),
    # path('portfolio/add', views.add_to_portfolio, name='addStocks'),
    path('portfolio/add', views.AddStock.as_view(), name='addStocks'),

]