from django.db import models
from django.utils import timezone

# Create your models here.

class Dado(models.Model):
	massa = models.CharField(verbose_name = 'Massa de cafe(g)', max_length = 10)
	hexano = models.CharField(verbose_name = 'Volume de hexano utilizado', max_length = 10)
	oleo = models.CharField(verbose_name = 'Volume de oleo obtido(ml)', max_length = 10)
	data = models.DateTimeField(verbose_name = 'Data da extracao', null = True, default = timezone.now)

	def __str__(self):
		return self.massa

    #def __str__(self):
    #    return self.massa