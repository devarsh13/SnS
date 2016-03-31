from __future__ import unicode_literals

from django.db import models


# Create your models here.
class city_list(models.Model):
	
	city_id=models.IntegerField(default=0,primary_key=True)
	CITIES=[('',''),('Ahmedabad','Ahmedabad'),('Gandhinagar','Gandhinagar')]
	city_name=models.CharField(default='',max_length=100,choices=CITIES,null=False)
	
	def __str__(self):
		return self.city_name
class institute_list(models.Model):
	institute_id=models.IntegerField(default=0,primary_key=True)
	INSTITUTES=[('',''),('DA-IICT','DA-IICT'),('Nirma Institute of Technology','Nirma Institute of Technology')]
	institute_name=models.CharField(default='',max_length=100,choices=INSTITUTES,null=False)
	
	def __str__(self):
		return self.institute_name
class profession_list(models.Model):
	profession_id=models.IntegerField(default=0,primary_key=True)
	PROFESSIONS=[('',''),('abc','abc')]
	profession_name=models.CharField(default='',max_length=100,choices=PROFESSIONS,null=True)

class users(models.Model):
	
	GENDER=[('M','Male'),('F','Female')]
	STATUS=[('-1','Not Active'),('0','Not Verified'),('1','Active')]

	user_id=models.IntegerField(primary_key=True,default=0)

	first_name=models.CharField(max_length=50)
	
	last_name=models.CharField(max_length=50)
	
	email=models.EmailField(unique=True)
	
	password=models.CharField(max_length=50,default='splitnsave')
	
	verified=models.BooleanField(default=False)
	
	contact_number=models.BigIntegerField(default=0)
	
	city=models.ForeignKey(city_list,on_delete=models.CASCADE)
	
	institute=models.ForeignKey(institute_list,on_delete=models.CASCADE,default=None)

	birthday=models.DateField(default=None)

	profession=models.ForeignKey(profession_list,on_delete=models.CASCADE,default=None)
	
	gender=models.CharField(max_length=1,choices=GENDER,default=None)

	status=models.IntegerField(default=0,null=False)

	verification_link=models.URLField(max_length=1000,default=None)

	rating=models.CharField(max_length=4,default='0')

	image_url=models.URLField(default=0)

	def __str__(self):
		return self.first_name+" "+self.last_name


class chat_history(models.Model):
	sender=models.ForeignKey(users,default=None,related_name='sender')

	receiver=models.ForeignKey(users,default=None,related_name='receiver')

	message=models.CharField(max_length=3000)

	timestamp=models.DateTimeField(default=None)

	delivered_status=models.BooleanField(default=False)

class categories(models.Model):
	category_id=models.IntegerField(default=0,primary_key=True)
	CATEGORIES=[('',''),('Cabs','Cabs'),('Books','Books')]
	category_name=models.CharField(default='',max_length=100,choices=CATEGORIES,null=False)

class products(models.Model):
	user_id=models.ForeignKey(users)
	
	category_id=models.ForeignKey(categories)

	product_id=models.IntegerField(default=0,primary_key=True)

	number_of_sharers=models.IntegerField(default=1)

	number_of_sharers_left=models.IntegerField(default=0)

	GENDER=[('M','Male'),('F','Female')]
	gender=models.CharField(max_length=1,choices=GENDER,default=None)

	description=models.CharField(max_length=1000,default=None)

	status=models.IntegerField(default=0)

	image_url=models.URLField(default=0)

	price=models.IntegerField(default=0,null=False)

	def __str__(self):
		return self.product_id

class transaction_history(models.Model):
	product_id=models.ForeignKey(products,default=None)

	poster=models.ForeignKey(users,default=None,related_name='poster')

	seeker=models.ForeignKey(users,default=None,related_name='seeker')

	transact_status=models.IntegerField(default=0)

class transaction_ratings(models.Model):
	product_id=models.ForeignKey(products,default=None)

	rater=models.ForeignKey(users,default=None,related_name='rater')

	ratee=models.ForeignKey(users,default=None,related_name='ratee')

	rating=models.IntegerField(users,default=None)

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

	starttime=models.TimeField()

	enddate=models.DateField()

	endtime=models.TimeField()

	smoking=models.BooleanField(default=False)

	car_type_id=models.ForeignKey(car_type_list,default=None)

	car_service_id=models.ForeignKey(car_service_list,default=None)

	car_name_id=models.ForeignKey(car_name_list,default=None)

	pet=models.BooleanField(default=False)

	Music=models.BooleanField(default=False)

	luggage=models.BooleanField(default=False)

	kids=models.BooleanField(default=False)

	non_stop_journey=models.BooleanField(default=False)

	destination=models.CharField(default=None,max_length=1000)

class laundary(models.Model):
	other_details=models.ForeignKey(products,default=None)

	startdate=models.DateField()

	starttime=models.TimeField()

	enddate=models.DateField()

	endtime=models.TimeField()

	weight=models.IntegerField(default=0)


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

class apartments(models.Model):
	other_details=models.ForeignKey(products,default=None)

	rooms=models.IntegerField(default=1)

	number_of_bedrooms=models.IntegerField(default=1)

	number_of_bathrooms=models.IntegerField(default=1)

	bathroom_type=models.CharField(default=None,max_length=100)

	in_time=models.TimeField()

	out_time=models.TimeField()

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

	family_friends_kids_friendly=models.BooleanField(default=False)

class tag_list(models.Model):
	tag_id=models.IntegerField(default=0,primary_key=True)
	TAGS=[('',''),('ABC','ABC')]
	tag_name=models.CharField(max_length=100,choices=TAGS,default=None)		

class books(models.Model):
	other_details=models.ForeignKey(products,default=None)

	startdate=models.DateField()

	enddate=models.DateField()

	bookname=models.CharField(default=None,max_length=100)

	author_first_name=models.CharField(default=0,max_length=100)

	author_last_name=models.CharField(default=0,max_length=100)

	sharing_type=models.CharField(default=0,max_length=100)

	tag1=models.ForeignKey(tag_list,default='',related_name='tag1')

	tag2=models.ForeignKey(tag_list,default='',related_name='tag2')

	tag3=models.ForeignKey(tag_list,default='',related_name='tag3')

