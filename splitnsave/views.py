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
	d={'details':{'User_Id':u.user_id,'First_Name':u.first_name,'Last_Name':u.last_name,'Email':u.email,'Password':u.password,'Verified':u.verified,'ContactNumber':u.contact_number,'CityName':u.city.city_name,'Institute':u.institute.institute_name,'Birthdate':u.birthday,'Profession_Name':u.profession.profession_name,'Gender':u.gender,'Status':u.status,'Image_Link':u.image_url,'Institute_Name':u.institute.institute_name}}
	return JsonResponse(d)

@csrf_exempt
def edit_profile_change(request):
	input1=json.loads(request.body)
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
	user_id=input1['User_Id']
	u=users.objects.get(user_id=user_id)
	d={'details':{'User_Id':u.user_id,'First_Name':u.first_name,'Last_Name':u.last_name,'Email':u.email,'Password':u.password,'Verified':u.verified,'ContactNumber':u.contact_number,'CityName':u.city.city_name,'Institute':u.institute.institute_name,'Birthdate':u.birthday,'Profession_Name':u.profession.profession_name,'Gender':u.gender,'Status':u.status,'Institute_Name':u.institute.institute_name}}
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
	u.password=input1['New_Password']

@csrf_exempt
def dashboard(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u1=users.objects.get(email=Email)
	u=users.objects.all()
	data={'users':[],'notifications':[{'Message':'aaaaa','Type':1}],'details':[]}
	for i in u:
		temp_dict={'First_Name':i.first_name,'Last_Name':i.last_name,'User_Id':i.user_id,'Image_Link':i.image_url}
		data['users'].append(temp_dict)
	data['details']={'First_Name':u1.first_name,'Last_Name':u1.last_name,'User_Id':u1.user_id,'Image_Link':u1.image_url}
	return JsonResponse(data)

@csrf_exempt	
def transactions(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	t=transaction_history.objects.all()
	transaction_list=[]
	for i in t:
		if(i.poster.email==Email or i.seeker.email==Email) :
			transaction_list.append(i)
	products=[]
	for i in transaction_list:
		temp=i.product_id
		details={'Product_Name':temp.product_name,'Product_Image':temp.image_url,'Product_Id':temp.product_id,'Confirm_Date':temp.confirm_date,'Price':temp.price}
		details['Sharer']=[]
		sharers=[]
		for i in transaction_history.objects.get(product_id=temp):
			if i.poster not in sharers:
				sharers.append(i)
			if i.seeker not in sharers:
				sharers.append(i)
		for i in sharers:
			user_details={'First_Name':i.First_Name,'Last_Name':i.Last_Name,'User_Id':i.user_id,'User_Image':i.image_url}
			details['sharer'].append(user_details)
		products.append(details)
	d={'products':products}
	return JsonResponse(d)
