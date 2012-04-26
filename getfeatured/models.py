from django.db import models
from django.utils import timezone
from django import forms
from django.core import validators
from django.forms import ModelForm

Lead_Type = (
	('Inbound','Inbound'),
	('Direct','Direct'),

	)

class Lead(models.Model):
	name = models.CharField(max_length=50)
	website = models.URLField()
	#zipcode = models.RegexField(max_length=5)
	#country = models.ChoiceField
	#leadType = models.CharField(max_length=7,choices=Lead_Type)
	def __unicode__(self):
		return self.name

	#def __init__(self, max_length=None, min_length=None, verify_exists=False,
		#validator_user_agent=validators.URL_VALIDATOR_USER_AGENT, *args, **kwargs):
		#super(URLField, self).__init__(max_length, min_length, *args,**kwargs)
		#self.validators.append(validators.URLValidator(verify_exists=verify_exists, validator_user_agent=validator_user_agent))

class Contact(models.Model):
	createDate = models.DateTimeField('Create Date')
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	title = models.CharField(max_length=20)
	#phone = models.PhoneNumberField
	email = models.EmailField()
	lead = models.ForeignKey(Lead)

	def __unicode__(self):
		return self.firstName
	def __unicode__(self):
		return self.lastName
	def __unicode__(self):
		return self.title
	def was_created_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ["createDate","firstName","lastName","title","email","lead"]

class LeadForm(ModelForm):
	class Meta:
		model = Lead

cForm = Contact()
c = Contact.objects.get(id=1)
c.save()

	

