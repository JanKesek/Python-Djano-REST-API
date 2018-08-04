# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fleet (models.Model):
	id_number = models.IntegerField()
	registration_number = models.BigIntegerField()
	max_passangers_numb = models.IntegerField()
	manufacture_year = models.IntegerField()
	producer = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	category = models.TextField()
	is_Hybrid = models.BooleanField(default=True)

def __str__(self):
	return '%s %s %s %s %s %s %s %s' % (self.id_number, self.registration_number, self.max_passanger_numb, self.manufacture_year, self.producer, self.model, self.category, self.is_Hybrid)
	
