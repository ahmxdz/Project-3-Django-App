from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
import requests
import json
import math

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

    @property 
    def market_value(self):            
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.ticker}&apikey=L22HS18QYQG1MIMD'
        r = requests.get(url)
        data = r.json()
        quote = data['Global Quote']
        value_of_price = quote['05. price']
        int_data_value = json.loads(value_of_price)
        mv_unrounded = float(int_data_value) * self.num_of_units
        return format(mv_unrounded, '.2f')
        
    # @property 
    # def profit(self):
    #     return math(self.market_value) - math(self.book_value)
        
    def get_absolute_url(self):
        return reverse('index', kwargs={'stock_id': self.id})

    

    
class Crypto(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField('Purchase Date')
    num_of_units = models.DecimalField(max_digits=14, decimal_places=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    @property # allows book value to be called similar to other model variables
    def book_value(self):
        return self.purchase_price * self.num_of_units
        # add repr to display as 2 digits ? 
    
    def get_absolute_url(self):
        return reverse('index', kwargs={'crypto_id': self.id})
    
class Portfolio(models.Model):
    stocks = models.ManyToManyField(Stock)
    crypto = models.ManyToManyField(Crypto)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

