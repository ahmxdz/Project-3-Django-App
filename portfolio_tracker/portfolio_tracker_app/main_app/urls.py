from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('portfolio/', views.index, name='index'),
    # path('portfolio/add', views.add_to_portfolio, name='addStocks'),
    path('portfolio/add', views.AddStock.as_view(), name='addStocks'),
    path('portfolio/update/', views.StockUpdate.as_view(), name='stocks_update'),
    path('portfolio/delete/', views.StockDelete.as_view(), name='stocks_delete'),
]