from django.db import models
from django.utils import timezone
from django import forms
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Gruser(models.Model):
	username = models.CharField(max_length=100, unique =True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(max_length=254, blank=False, unique=True)
#	mobile = PhoneNumberField(settings.PHONENUMBER_DB_FORMAT=E164, default=None)
	mobile = models.CharField(max_length=15, blank=True)
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
	password = models.CharField(max_length=128, editable=False, blank=False)
	# YESNO_CHOICES = (('male', 'male'), ('female', 'female'))
	join_date = models.DateTimeField(default=timezone.now)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = "username"

	REQUIRED_FIELDS = ['']

	def __str__(self):
		return self.email