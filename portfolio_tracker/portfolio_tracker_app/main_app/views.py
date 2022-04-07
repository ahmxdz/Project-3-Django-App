from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# @login_required <-- must be put above function to enable when logged in only
# def finches_index(request):
from .models import Stock, Crypto, Portfolio

# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

#LoginRequiredMixin -- add this as a parameter for add, update, delete views once user signup is ready 

class AddStock(CreateView):
  model = Stock
  fields = '__all__'
  # fields = ['name', 'ticker', 'purchase_price', 'purchase_date', 'num_of_units']
  # This inherited method is called when a
  # valid cat form is being submitted

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    
    return super().form_valid(form)
  success_url = '/portfolio/'
  

class StockUpdate(UpdateView):
  model = Stock
  fields = '__all__'

class StockDelete(DeleteView):
  model = Stock
  success_url = '/portfolio/'

def about(request):
  return render(request, 'about.html')

def index(request):
  stocks = Stock.objects.all()
  return render(request, 'portfolio/index.html', {'stocks': stocks})

def add_to_portfolio(request):
  return render(request, 'portfolio/addStocks.html')