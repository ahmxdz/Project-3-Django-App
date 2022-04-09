from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    purchase_price = models.DecimalField('Purchase Price', max_digits=10, decimal_places=2)
    purchase_date = models.DateField('Purchase Date')
    num_of_units = models.IntegerField('# of Units')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # alternatively to do it directly in the template: https://stackoverflow.com/questions/18350630/multiplication-in-django-template-without-using-manually-created-template-tag
    @property # allows book value to be called similar to other model variables
    def book_value(self):
        return self.purchase_price * self.num_of_units
    
    def get_absolute_url(self):
        return reverse('index', kwargs={'stock_id': self.id})

    
class Crypto(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField('Purchase Date')
    num_of_units = models.DecimalField(max_digits=10, decimal_places=10)
    
class Portfolio(models.Model):
    stocks = models.ManyToManyField(Stock)
    crypto = models.ManyToManyField(Crypto)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=true, null=True))

