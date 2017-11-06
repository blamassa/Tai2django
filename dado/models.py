from django.db import models
from django.db.models import F 
from django.utils import timezone

# Create your models here.

class Dado(models.Model):
    	
	massa = models.FloatField(verbose_name = 'Massa de cafe(g)', blank = False)
	hexano = models.FloatField(verbose_name = 'Volume de hexano utilizado', blank = False)
	oleo = models.FloatField(verbose_name = 'Volume de oleo obtido(ml)', blank = False)
	relacao = models.FloatField(verbose_name = 'Eficiencia da extracao(%): (84.6*volume oleo/massa cafe)', blank = False)
	data = models.DateTimeField(verbose_name = 'Data da extracao', max_length = 100)


	def __str__(self):
    		return 'extracao'

	
	'''
	def get_massa(self):
    		return self.massa
	
	def get_hexano(self):
    		return self.massa
	
	def get_oleo(self):
    		return self.oleo

    #def __str__(self):
    #    return self.massa	
	
#relacao = Dado.objects.all().annotate(value = (84.6 * F('oleo'))/F('massa'))
	
'''