from django.shortcuts import render
from django.shortcuts import render
import cleanWater

# Create your views here.
def index(request):
    return render(request, "cleanWater/index.html")