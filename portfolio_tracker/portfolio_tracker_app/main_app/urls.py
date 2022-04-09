from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.index, name='index'),
    path('portfolio/add', views.AddStock.as_view(), name='addStocks'),
    path('portfolio/<int:stock_id>/', views.portfolio_detail, name='detail'),
    path('portfolio/<int:pk>/update/', views.StockUpdate.as_view(), name='stock_update'),
    path('portfolio/<int:pk>/delete/', views.StockDelete.as_view(), name='stock_delete'),
]