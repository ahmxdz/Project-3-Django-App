from django.contrib import admin
from . models import Stock, Crypto, Portfolio
# Register your models here.

admin.site.register(Stock)
admin.site.register(Crypto)
admin.site.register(Portfolio)