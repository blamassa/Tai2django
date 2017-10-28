from django.shortcuts import render
from .models import Dado
import datetime

# Create your views here.

def dado(request):
	dado = Dado.objects.order_by('data')
	#oleo = dado.objects.all().oleo
	#massa = dado.objects.all().massa
	#relacao = (84.6*oleo)/(massa)
	#dado.append(relacao)
	return render(request, 'index.html',{'dado':dado})