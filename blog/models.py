# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse 

class Blog(models.Model):
	title = models.CharField(max_length= 200)
	body = models.TextField()
	created_at = models.DateTimeField(default = datetime.now, blank = True)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post:detail', kwargs ={'pk: self.pk'})