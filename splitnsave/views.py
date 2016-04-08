from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from models import *
from django.views.decorators.csrf import csrf_exempt
import json
import ast
from time import strptime
# Create your views here.
def index(request):
	return render(request,'index.html')
@csrf_exempt
def signup_check(request):
	Email=json.loads(request.body)
	exists=False
	msg={'status':'0'}
	try:
		print "Asdsad"
		users.objects.get(email=Email['Email'])
		exists=True
	except:
		pass
	if(exists==True):
		msg['status']='-1'

	
	msg['email']=Email
	return JsonResponse(msg)
@csrf_exempt
def signup(request):
	input1=json.loads(request.body)
	institute=institute_list.objects.get(institute_name=input1['Institute_Name'])
	profession=profession_list.objects.get(profession_name=input1['Profession_Name'])
	city=city_list.objects.get(city_name=input1['CityName'])
	birthdate=strptime(input1['Birthdate'],'%d/%m/%Y')
	u=users.objects.create(first_name=input1['First_Name'],
		last_name=input1['Last_Name'],
		contact_number=input1['ContactNumber'],
		password=input1['Password'],
		email=input1['Email'],
		city=city,
		birthday=str(birthdate.tm_year)+'-'+str(birthdate.tm_mon)+'-'+str(birthdate.tm_mday),
		gender=input1['Gender'],
		institute=institute,
		profession=profession,
		image_url=input1['Image_Link'])	


	return JsonResponse({status:'0'})
@csrf_exempt
def editprofile(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)

@csrf_exempt
def edit_profile_change(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	institute=institute_list.objects.get(institute_name=input1['Institute_Name'])
	profession=profession_list.objects.get(profession_name=input1['Profession_Name'])
	city=city_list.objects.get(city_name=input1['CityName'])
	birthdate=strptime(input1['Birthdate'],'%d/%m/%Y')
	u=users.objects.get(email=Email)
	u.first_name=input1['First_Name']
	u.last_name=input1['Last_Name']
	u.contact_number=input1['ContactNumber']
	u.password=input1['Password']
	u.city_name=city
	u.birthday=str(birthdate.tm_year)+'-'+str(birthdate.tm_mon)+'-'+str(birthdate.tm_mday)
	u.gender=input1['Gender']
	u.institute=institute
	u.profession=profession
	u.image_url=input1['Image_Link']

	return JsonResponse({status:'0'})
@csrf_exempt
def userprofile(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)

@csrf_exempt
def settings(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	d={'old_password':u.password}
	return JsonResponse(d)

@csrf_exempt
def change_password(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=user.objects.get(email=Email)
	u.password=new_password

@csrf_exempt
def dashboard(request):
	u=users.objects.all()
	data=[]
	for i in u:
		temp_dict={'First_Name':i.first_name,'Last_Name':i.last_name,'User_Id':i.user_id,'Image_Link':i.image_url}
		data.append(temp_dict)
	return JsonResponse(data)

@csrf_exempt	
def products(request):
	#Coded in /SEN
	pass
