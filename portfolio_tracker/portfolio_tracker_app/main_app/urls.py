from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.index, name='index'),
    path('portfolio/addstock', views.AddStock.as_view(), name='add_stocks'),
    path('portfolio/s/<int:stock_id>/', views.stock_detail, name='stock_detail'),
    path('portfolio/s/<int:pk>/update/', views.StockUpdate.as_view(), name='stock_update'),
    path('portfolio/s/<int:pk>/delete/', views.StockDelete.as_view(), name='stock_delete'),
    path('portfolio/addcrypto', views.AddCrypto.as_view(), name='add_crypto'),
    path('portfolio/c/<int:crypto_id>/', views.crypto_detail, name='crypto_detail'),
    path('portfolio/c/<int:pk>/update/', views.CryptoUpdate.as_view(), name='crypto_update'),
    path('portfolio/c/<int:pk>/delete/', views.CryptoDelete.as_view(), name='crypto_delete'),
]