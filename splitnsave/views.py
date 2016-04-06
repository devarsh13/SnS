from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from models import *
from django.views.decorators.csrf import csrf_exempt
import json
import ast
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
		city=city,
		birthday=birthdate.year+'-'+birthdate.month+'-'+birthdate.day,
		gender=input1['Gender'],
		institute=institute,
		profession=profession,
		image_url=input1['Image_Link'])	


	return JsonResponse({status:'0'})
@csrf_exempt
def editprofile(request):
	userid=request.POST.get('input','')
	userid=userid['User_id']
	u=users.objects.get(user_id=userid)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)

@csrf_exempt
def edit_profile_change(request):
	data_json=request.POST.get('input','')
	u=users.objects.get(user_id=data_json['User_id'])
	u.first_name=input1['First_Name'],
	u.last_name=input1['Last_Name'],
	u.contact_number=input1['ContactNumber'],
	u.password=input1['Password'],
	u.city_name=input1['CityName'],
	u.birthday=input1['Birthdate'],
	u.gender=input1['Gender'],
	u.institute=input1['Institute_Name'],
	u.profession=input1['Profession_Name'],
	u.image_url=input1['Image_Link']

@csrf_exempt
def userprofile(request):
	userid='0'
	u=users.objects.get(user_id=userid)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)

@csrf_exempt
def settings(request):
	userid='0'
	u=users.objects.get(user_id=userid)
	d={'old_password':u.password}
	return JsonResponse(d)

@csrf_exempt
def change_password(request):
	userid=request.POST.get('userid','')
	new_password=request.POST.get('new_password','')
	u=user.objects.get(user_id=userid)
	u.password=new_password

@csrf_exempt
def dashboard(request):
	#Coded in /SEN
	pass

@csrf_exempt	
def products(request):
	#Coded in /SEN
	pass