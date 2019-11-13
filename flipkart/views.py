from django.shortcuts import render,redirect,Http404
from django.http import HttpResponseRedirect,HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import PriceDrop
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from decimal import *
import math
import time 

# Create your views here.

def home(request):
  
    return render(request,'index.html',{})
       
@login_required
def dashboard(request):
    try:

        all = PriceDrop.objects.filter(user = request.user) # Getting user data
    #global prices
    except PriceDrop.DoesNotExist:
        raise Http404("Page doesn't Exist")

    prices =[]
    
    # Grab the current price from DB links/urls of added products
    #def check_price(all):
    for i in range(len(all)):        
        response = requests.get(all[i].url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find('div',class_="_1vC4OE _3qQ9m1")
        price = price.text
        price = price.replace(',','')
        price = float(price[1:])
        prices.append(price)
        
        old_price = all[i].curr_price
        price_change = old_price - Decimal(price) # calculating price change
        pct_10 = math.ceil(old_price*Decimal((10/100))) # Calculating 10%

        # Price Coomparision 
        if pct_10 <= price_change:

        # sending emails
            subject = 'Alert: Price Dropped To 10%'
            message = "Hey, "+ request.user.username +" \nYou added a product from flipkart in Price Drop website, Now its time to Grab your product. "+'\nProduct Title :'+all[i].title+'\n Current price: '+'₹'+str(price)+'\n Old Price: '+'₹'+str(old_price) + "\n Check The product, Link is Here: "+ all[i].url
            to_email = [request.user.email]
            send_mail(subject,message,settings.EMAIL_HOST_USER,to_email,fail_silently=False)   
    
    #while True: # Refresh Time
       # check_price(all) 
        #time.sleep(5) 

    

    return render(request,'dashboard.html',{'all':zip(all,prices)})


@login_required
def add_url(request):
    try:
        if request.method =='POST':
            url = request.POST['url']
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('span',class_="_35KyD6").getText()
            price = soup.find('div',class_="_1vC4OE _3qQ9m1").getText()
            price = price.replace(',','')
            price = float(price[1:])
            #user = request.user
            data = PriceDrop(title=title,url=url,curr_price=price)   
            data.user = request.user
            data.save()
    except PriceDrop.DoesNotExist:
        raise Http404("Page doesn't Exist")

    return redirect('dashboard')


@login_required
def delete(request,id):

    item = PriceDrop.objects.get(id=id)
    try:
        item.delete()
    except:
        return HttpResponseRedirect('Item not found')
    return redirect('dashboard')


