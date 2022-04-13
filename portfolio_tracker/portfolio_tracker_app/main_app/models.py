from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
import requests, json, decimal, environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

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
        bv_unrounded = float(self.purchase_price) * self.num_of_units
        return bv_unrounded
        # print(type(bv_unrounded))

    @property 
    def market_value(self):            
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.ticker}&apikey={env('STOCK_API')}"
        r = requests.get(url)
        data = r.json()
        quote = data.get('Global Quote')
        if quote is None:
           return 0.00
        
        value_of_price = quote['05. price']
        float_data_value = float(value_of_price)
        mv_unrounded = float_data_value * self.num_of_units
        return '{:.2f}'.format(mv_unrounded)
        
    @property 
    def profit(self):
        return self.market_value - self.book_value
        
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
        bv_unrounded = self.purchase_price * self.num_of_units
        return decimal.Decimal(bv_unrounded)
        # add repr to display as 2 digits ? 

    @property 
    def market_value(self):       
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={self.ticker}&to_currency=USD&apikey={env('CRYPTO_API')}"
        r = requests.get(url)
        data = r.json()

        quote = data.get('Realtime Currency Exchange Rate')
        if quote is None:
            return 0.00

        value_of_price = quote['5. Exchange Rate']
        float_data_value = float(value_of_price)
        mv_unrounded = float_data_value * self.num_of_units
        return '{:.2f}'.format(mv_unrounded)

    @property 
    def profit(self):
        return self.market_value - self.book_value

    def get_absolute_url(self):
        return reverse('index', kwargs={'crypto_id': self.id})
    
class Portfolio(models.Model):
    stocks = models.ManyToManyField(Stock)
    crypto = models.ManyToManyField(Crypto)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

