from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from models import *
# Create your views here.
def index(request):
	return render(request,'index.html')
@csrf_exempt
def signup_check(request):
	Email=request.POST.get('Email','')
	
	
	exists=False
	msg={'status':'0'}
	try:
		print "Asdsad"
		users.objects.get(email=Email)
		exists=True
	except:
		pass
	if(exists==True):
		msg['status']='-1'

	return JsonResponse(msg)
def signup(request):
	input_=request.POST.get('input','')
	u=users.objects.create(user_id=1,
		first_name=input_['First_Name'],
		last_name=input_['Last_Name'],
		contact_number=input_['ContactNumber'],
		password=input_['Password'],
		city_name=input_['CityName'],
		birthday=input_['Birthdate'],
		gender=input_['Gender'],
		institute=input_['Institute_Name'],
		profession=input_['Profession_Name'],
		image_url=input_['Image_Link'])
	

def editprofile(request):
	userid=request.POST.get('input','')
	userid=userid['User_id']

	u=users.objects.get(user_id=userid)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)

def edit_profile_change(request):
	data_json=request.POST.get('input','')
	u=users.objects.get(user_id=data_json['User_id'])


def userprofile(request):
	userid='0'
	u=users.objects.get(user_id=userid)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)

def settings(request):
	userid='0'
	u=users.objects.get(user_id=userid)
	d={'old_password':u.password}
	return JsonResponse(d)

def change_password(request):
	userid=request.POST.get('userid','')
	new_password=request.POST.get('new_password','')
	u=user.objects.get(user_id=userid)
	u.password=new_password

def dashboard(request):
	#Coded in /SEN
	pass
	
def products(request):
	#Coded in /SEN
	pass