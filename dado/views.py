from django.shortcuts import render
from .models import Dado

# Create your views here.

def dado(request):
	dado = Dado.objects.order_by('data')
	return render(request, 'index.html',{'dado':dado})
