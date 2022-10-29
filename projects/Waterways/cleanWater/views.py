import email
from locale import currency
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.urls import reverse
from urllib3 import HTTPResponse
import cleanWater
from django.http import HttpResponseRedirect, JsonResponse
import stripe

stripe.api_key = "sk_test_51LyJ17BSE8CSa3qNLumX2XXGcoidGdc3sypq7xVE8sLhD2e8Oa7NAweBoNhDQdyVYHzdTWdDjmsvzuhXUhurgtvV008Np5GhjP" 

def index(request):
    list = (0, 1, 2)
    return render(request, "cleanWater/index.html", {
        "List": list
    })
    
def charge(request):
    amount = 5
    if request.method == 'POST':
        print("Data: ", request.POST)
        
        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['nickname'],
            source = request.POST['stripeToken']
        )
        
        charge = stripe.Charge.create(
            customer=customer,
            amount=500,
            currency="usd",
            description="Donation",
            
        )
        
    return HttpResponseRedirect(reverse("successMsg", args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, "cleanWater/success.html", {
        "amount": amount
    })