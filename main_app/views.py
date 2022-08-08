from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Stock, Crypto, Portfolio
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

#LoginRequiredMixin -- add this as a parameter for add, update, delete views once user signup is ready 


class AddStock(LoginRequiredMixin, CreateView):
  model = Stock
  fields = ['name', 'ticker', 'purchase_price', 'purchase_date', 'num_of_units']
  # This inherited method is called when a
  # valid stock form is being submitted

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the stock
    # Let the CreateView do its job as usual
    
    return super().form_valid(form)
  success_url = '/portfolio/'
  

class StockUpdate(LoginRequiredMixin, UpdateView):
  model = Stock
  fields = ['name', 'ticker', 'purchase_price', 'purchase_date', 'num_of_units']

class StockDelete(LoginRequiredMixin, DeleteView):
  model = Stock
  success_url = '/portfolio/'

class AddCrypto(LoginRequiredMixin, CreateView):
  model = Crypto
  fields = ['name', 'ticker', 'purchase_price', 'purchase_date', 'num_of_units']
  # This inherited method is called when a
  # valid stock form is being submitted

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the stock
    # Let the CreateView do its job as usual
    
    return super().form_valid(form)
  success_url = '/portfolio/'

class CryptoUpdate(LoginRequiredMixin, UpdateView):
  model = Crypto
  fields = ['name', 'ticker', 'purchase_price', 'purchase_date', 'num_of_units']

class CryptoDelete(LoginRequiredMixin, DeleteView):
  model = Crypto
  success_url = '/portfolio/'

def home(request):
  return render(request, 'home.html')
  
def about(request):
  return render(request, 'about.html')

@login_required
def index(request):
  stocks = Stock.objects.filter(user = request.user)
  crypto = Crypto.objects.filter(user = request.user)
  return render(request, 'portfolio/index.html', {'stocks': stocks, 'crypto': crypto})

@login_required
def add_to_portfolio(request):
  return render(request, 'portfolio/addStocks.html')

@login_required
def stock_detail(request, stock_id):
  # update for portfolio model once it gets going
  stock = Stock.objects.get(id=stock_id)

  return render(request, 'portfolio/stock_detail.html', {
    'stock': stock,
  })

@login_required
def crypto_detail(request, crypto_id):
  # update for portfolio model once it gets going
  crypto = Crypto.objects.get(id=crypto_id)

  return render(request, 'portfolio/crypto_detail.html', {
    'crypto': crypto,
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

