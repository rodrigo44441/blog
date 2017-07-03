from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	description = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length = 200, unique = True)
	summary = models.CharField(max_length = 200, unique = True, blank = True)
	slug = models.SlugField(blank=False, null=False, unique = True)
	content = models.TextField(blank = True)
	created = models.DateTimeField(auto_now_add = True, editable = True)
	modified = models.DateTimeField(auto_now = True, editable = True)
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to = 'posts', blank = True)
	video = models.FileField(upload_to = 'posts', blank = True)
	attached = models.ImageField(upload_to = 'posts', blank = True)
	numero = models.PositiveIntegerField(default=1)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = '-'.join((slugify(self.title), slugify(self.numero)))
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

