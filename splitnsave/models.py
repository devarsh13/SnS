from __future__ import unicode_literals
import json
from django.db import models
import datetime

def number():
		no=users.objects.count()
		if no==None:
			return 1
		else:
			return no+1
def institute_number():
		no1=institute_list.objects.count()
		if no1==None:
			return 1
		else:
			return no1+1
def city_number():
		no2=city_list.objects.count()
		if no2==None:
			return 1
		else:
			return no2+1
def profession_number():
		no3=profession_list.objects.count()
		if no3==None:
			return 1
		else:
			return no3+1
def product_number():
		no=products.objects.all().order_by("-product_id")[0]
		if no==None:
			return 1
		else:
			return no+1
# Create your models here
class city_list(models.Model):
	
	city_id=models.IntegerField(primary_key=True,default=city_number)
	CITIES=[('',''),('Ahmedabad','Ahmedabad'),('Gandhinagar','Gandhinagar')]
	city_name=models.CharField(default='',max_length=100,choices=CITIES)
	
	def __str__(self):
		return self.city_name
class institute_list(models.Model):
	institute_id=models.IntegerField(primary_key=True,default=institute_number)
	INSTITUTES=[('',''),('DA-IICT','DA-IICT'),('Nirma Institute of Technology','Nirma Institute of Technology')]
	institute_name=models.CharField(default='',max_length=100,choices=INSTITUTES,null=False)
	
	def __str__(self):
		return self.institute_name
class profession_list(models.Model):
	profession_id=models.IntegerField(primary_key=True,default=profession_number)
	PROFESSIONS=[('',''),('Student','Student'),('abc','abc')]
	profession_name=models.CharField(default='',max_length=100,choices=PROFESSIONS,null=True)

class users(models.Model):
	
	GENDER=[('M','Male'),('F','Female')]
	STATUS=[('-1','Not Active'),('0','Not Verified'),('1','Active')]
	user_id=models.IntegerField(default=number)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(primary_key=True,null=False)
	password=models.CharField(max_length=50,default='splitnsave')
	verified=models.BooleanField(default=False)
	contact_number=models.BigIntegerField(default=0)
	city=models.ForeignKey(city_list,on_delete=models.CASCADE)
	institute=models.ForeignKey(institute_list,on_delete=models.CASCADE,default=None)
	birthday=models.DateField(default=None)
	profession=models.ForeignKey(profession_list,on_delete=models.CASCADE,default=None)
	gender=models.CharField(max_length=1,choices=GENDER,default=None)
	status=models.IntegerField(default=0,null=False)
	verification_code=models.CharField(max_length=1000,default='asdfghjkl')
	rating=models.CharField(max_length=4,default='0')
	image_url=models.URLField(default=0)


	def __str__(self):
		return self.first_name+" "+self.last_name


class categories(models.Model):
	category_id=models.IntegerField(default=0,primary_key=True)
	CATEGORIES=[('',''),('Cabs','Cabs'),('Books','Books'),('Laundary','Laundary'),('Apartments','Apartments')]
	category_name=models.CharField(default='',max_length=100,choices=CATEGORIES,null=False)
	def __str__(self):
		return self.category_name

class products(models.Model):
	user_id=models.ForeignKey(users)
	product_name=models.CharField(default='',null=False,max_length=100)
	category_id=models.ForeignKey(categories)
	product_id=models.IntegerField(default=product_number,primary_key=True)
	number_of_sharers=models.IntegerField(default=1)
	number_of_sharers_left=models.IntegerField(default=0)
	GENDER=[('M','Male'),('F','Female')]
	gender=models.CharField(max_length=1000,default='')
	description=models.CharField(max_length=1000,default=None)
	status=models.IntegerField(default=0)
	image_url=models.URLField(default=0)
	price=models.IntegerField(default=0,null=False)
	confirm_date=models.DateField(null=True,blank=True,default=None)
	post_date=models.DateField(default=datetime.date.today(),null=True)
	location=models.CharField(max_length=100,default=None,null=True,blank=True)
	def __str__(self):
		return str(self.product_name)

class transaction_ratings(models.Model):
	product_id=models.ForeignKey(products,default=None)
	rater=models.ForeignKey(users,default=None,related_name='rater')
	ratee=models.ForeignKey(users,default=None,related_name='ratee')
	rating=models.IntegerField(default=0)
	def __str__(self):
		return str(self.rater.first_name)+"->"+str(self.ratee.first_name)

class transaction_history(models.Model):
	product_id=models.ForeignKey(products,default=None,primary_key=True)
	poster=models.ForeignKey(users,default=None,related_name='poster',primary_key=True)
	seeker=models.ForeignKey(users,default=None,related_name='seeker',primary_key=True)
	transact_status=models.IntegerField(default=0,primary_key=True)
	rating=models.ForeignKey(transaction_ratings,default=None)
	def __str__(self):
		return str(self.poster.first_name)+"->"+str(self.seeker.first_name)		

class post_reporting(models.Model):
	product_id=models.ForeignKey(products,default=None)
	reporter=models.ForeignKey(users,default=None)
	status=models.IntegerField(default=0)

class user_reporting(models.Model):
	reporter=models.ForeignKey(users,default=None,related_name='reporter')
	reportee=models.ForeignKey(users,default=None,related_name='reportee')
	status=models.IntegerField(default=0)

class car_service_list(models.Model):
	car_service_id=models.IntegerField(default=0,primary_key=True)
	CARSERIVCE=[('',''),('Uber','Uber')]
	car_service=models.CharField(default='',choices=CARSERIVCE,max_length=100)

class car_type_list(models.Model):
	car_type_id=models.IntegerField(default=0,primary_key=True)
	CARTYPE=[('',''),('Sedan','Sedan')]
	car_type=models.CharField(default='',choices=CARTYPE,max_length=100)

class car_name_list(models.Model):
	car_name_id=models.IntegerField(default=0,primary_key=True)
	CARNAME=[('',''),('ABC','ABC')]
	car_name=models.CharField(default='',choices=CARNAME,max_length=100)	

class cabs(models.Model):
	other_details=models.ForeignKey(products,default=None)
	startdate=models.DateField()
	starttime=models.CharField(max_length=100)
	enddate=models.DateField()
	endtime=models.CharField(max_length=100)
	smoking=models.BooleanField(default=False)
	car_type=models.CharField(max_length=100,default='')
	car_service=models.CharField(max_length=100,default='')
	car_name=models.CharField(max_length=100,default='')
	pet=models.BooleanField(default=False)
	music=models.BooleanField(default=False)
	luggage=models.BooleanField(default=False)
	kids=models.BooleanField(default=False)
	non_stop_journey=models.BooleanField(default=False)
	destination=models.CharField(default=None,max_length=1000)
	def __str__(self):
		return self.other_details.product_name
class laundary(models.Model):
	other_details=models.ForeignKey(products,default=None)
	startdate=models.DateField()
	starttime=models.CharField(max_length=100,default='')
	enddate=models.DateField()
	endtime=models.CharField(max_length=100,default='')
	weight=models.IntegerField(default=0)
	white_clothes=models.BooleanField(default=False)
	fabric_softner=models.BooleanField(default=False)
	steam_press=models.BooleanField(default=False)
	dry_cleaning=models.BooleanField(default=False)
	silk_clothes=models.BooleanField(default=False)
	cotton_clothes=models.BooleanField(default=False)
	light_clothes=models.BooleanField(default=False)

	def __str__(self):
		return self.other_details.product_name
class sub_category_list(models.Model):
	sub_category_id=models.IntegerField(default=0,primary_key=True)
	SUBCATEGORIES=[('',''),('ABC','ABC')]
	sub_category_name=models.CharField(max_length=100,choices=SUBCATEGORIES,default=None)

class keyword_list(models.Model):
	keyword_id=models.IntegerField(default=0,primary_key=True)
	KEYWORDS=[('',''),('ABC','ABC')]
	keyword_name=models.CharField(max_length=100,choices=KEYWORDS,default=None)	

class equipment(models.Model):
	other_details=models.ForeignKey(products,default=None)
	startdate=models.DateField()
	enddate=models.DateField()
	sub_category_id=models.ForeignKey(sub_category_list)
	keyword_id1=models.ForeignKey(keyword_list,related_name='keyword1')
	keyword_id2=models.ForeignKey(keyword_list,related_name='keyword2')
	keyword_id3=models.ForeignKey(keyword_list,related_name='keyword3')
	def __str__(self):
		return self.other_details.product_name
class apartments(models.Model):
	other_details=models.ForeignKey(products,default=None)
	rooms=models.IntegerField(default=1)
	number_of_bedrooms=models.IntegerField(default=1)
	number_of_bathrooms=models.IntegerField(default=1)
	bathroom_type=models.CharField(default=None,max_length=100)
	in_time=models.CharField(max_length=100,default='')
	out_time=models.CharField(max_length=100,default='')
	kitchen=models.BooleanField(default=False)
	television=models.BooleanField(default=False)
	heater=models.BooleanField(default=False)
	air_conditioner=models.BooleanField(default=False)
	internet=models.BooleanField(default=False)
	medical_aid=models.BooleanField(default=False)
	fire_alarm=models.BooleanField(default=False)
	washing_machine=models.BooleanField(default=False)
	parking=models.BooleanField(default=False)
	canteen=models.BooleanField(default=False)
	pets=models.BooleanField(default=False)
	suitable_for_events=models.BooleanField(default=False)
	smoking=models.BooleanField(default=False)
	wheelchair=models.BooleanField(default=False)
	elevator=models.BooleanField(default=False)
	laptop_friendly=models.BooleanField(default=False)
	pool=models.BooleanField(default=False)
	gym=models.BooleanField(default=False)
	location=models.CharField(max_length=100,default='')
	family_friends_kids_friendly=models.BooleanField(default=False)
	def __str__(self):
		return self.other_details.product_name
class tag_list(models.Model):
	tag_id=models.IntegerField(default=0,primary_key=True)
	TAGS=[('',''),('ABC','ABC')]
	tag_name=models.CharField(max_length=100,choices=TAGS,default=None)		

class books(models.Model):
	other_details=models.ForeignKey(products,default=None)
	startdate=models.DateField()
	enddate=models.DateField()
	author_first_name=models.CharField(default=0,max_length=100)
	author_last_name=models.CharField(default=0,max_length=100)
	tag1=models.CharField(max_length=100,default='')
	tag2=models.CharField(max_length=100,default='')
	tag3=models.CharField(max_length=100,default='')
	location=models.CharField(max_length=100,default='')
	college=models.CharField(max_length=100,default='')
	def __str__(self):
		return self.other_details.product_name
class user_interested(models.Model):
	user_id=models.ForeignKey(users,primary_key=True)
	product_id=models.ForeignKey(products,primary_key=True)
	status=models.IntegerField(default=0)

class user_report_post(models.Model):
	user_id=models.ForeignKey(users)
	product_id=models.ForeignKey(products)
	status=models.IntegerField(default=0)

class user_report_user(models.Model):
	user1=models.ForeignKey(users,related_name='user1')
	user2=models.ForeignKey(users,related_name='user2')
	status=models.IntegerField(default=0)

class chat_history(models.Model):
	sender=models.ForeignKey(users,default=None,related_name='sender')
	receiver=models.ForeignKey(users,default=None,related_name='receiver')
	message=models.CharField(max_length=100000,default=None)
	timestamp=models.DateTimeField()
