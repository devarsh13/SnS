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
	Email=input1['Email']
	institute=institute_list.objects.get(institute_name=input1['Institute_Name'])
	profession=profession_list.objects.get(profession_name=input1['Profession_Name'])
	city=city_list.objects.get(city_name=input1['CityName'])
	birthdate=strptime(input1['Birthdate'],'%Y-%m-%d')
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
	u.save()
	return JsonResponse({'status':'0'})
@csrf_exempt
def userprofile(request):
	input1=json.loads(request.body)
	user_id=input1['User_Id']
	Email=input1['Email']
	u=users.objects.get(user_id=user_id)
	
	u1=users.objects.get(email=Email)
	ui=user_interested.objects.filter(user_id=user_id)
	temp=users.objects.get(email=Email)
	p=products.objects.filter(user_id=temp)
	status=0
	for i in p:
		for j in ui:

			if i.product_id==j.product_id.product_id and j.status==1:
				status=1
				break
	try:
		ur=user_reporting.objects.get(reporter=u1,reportee=u)
		status=2
	except:
		pass
	d={'details':{'User_Id':u.user_id,'First_Name':u.first_name,'Last_Name':u.last_name,'Email':u.email,'Password':u.password,'Verified':u.verified,'ContactNumber':u.contact_number,'CityName':u.city.city_name,'Institute':u.institute.institute_name,'Birthdate':u.birthday,'Profession_Name':u.profession.profession_name,'Gender':u.gender,'Status':status,'Institute_Name':u.institute.institute_name}}
	return JsonResponse(d)

@csrf_exempt
def settings(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	d={'Old_Password':u.password}
	return JsonResponse(d)

@csrf_exempt
def change_password(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	u.password=input1['New_Password']
	u.save()
	return JsonResponse({'status':0})
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
		details={'Product_Name':temp.product_name,'Product_Image':temp.image_url,'Product_Id':temp.product_id,'Confirm_Date':temp.confirm_date,'Price':temp.price,'Location':temp.location}
		details['Sharer']=[]
		sharers=[]
		aaa=transaction_history.objects.filter(product_id=temp)
		for j in aaa:
			if j.poster not in sharers:
				sharers.append(j.poster)
			if j.seeker not in sharers:
				sharers.append(j.seeker)
		sharers.remove(users.objects.get(email=Email))
		for k in sharers:
			rater=users.objects.get(email=Email)
			rating=transaction_ratings.objects.get(rater=rater,ratee=k)
			user_details={'First_Name':k.first_name,'Last_Name':k.last_name,'User_Id':k.user_id,'User_Image':k.image_url,'Rating':rating.rating}
			details['Sharer'].append(user_details)
		products.append(details)
	d={'products':products}
	return JsonResponse(d)

@csrf_exempt
def change_rating(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	User_Id=input1['User_Id']
	rating=input1['Rating']
	Product_Id=input1['Product_Id']
	u=users.objects.get(email=Email)
	u1=users.objects.get(user_id=User_Id)
	p=products.objects.get(product_id=Product_Id)
	t=transaction_ratings.objects.get(product_id=p,rater=u,ratee=u1)
	t.rating=rating
	t.save()

	return JsonResponse({'status':0})
@csrf_exempt
def my_posts(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	all_products=products.objects.all()
	my_products=[]
	for i in all_products:
		if(i.user_id.email==Email):
			my_products.append(i)
	d={'Products':[]}
	for i in my_products:
		temp={}
		temp['Product_Name']=i.product_name
		temp['Product_Image']=i.image_url
		temp['Product_Id']=i.product_id
		temp['Location']=i.location
		temp['Post_Date']=i.post_date
		temp['Price']=i.price
		temp['Sharer']=[]
		u=user_interested.objects.filter(product_id=i)
		for j in u:
			temp_user={}
			temp_user['First_Name']=j.user_id.first_name
			temp_user['Last_Name']=j.user_id.last_name
			temp_user['User_Id']=j.user_id.user_id
			temp_user['User_Image']=j.user_id.image_url
			temp_user['Status']=j.status
			temp['Sharer'].append(temp_user)
		d['Products'].append(temp)
	return JsonResponse(d)
@csrf_exempt
def delete_my_posts(request):
	input1=json.loads(request.body)
	Product_Id=input1['Product_Id']
	p=products.objects.get(product_id=Product_Id)
	p.delete()
	return JsonResponse({'status':0})
@csrf_exempt
def update_my_posts(request):
	input1=json.loads(request.body)
	Product_Id=input1['Product_Id']
	Email=input1['Email']
	User_Id=input1['User_Id']
	Status=input1['Status']
	u=users.objects.get(user_id=User_Id)
	p=products.objects.get(product_id=Product_Id)
	ui=user_interested.objects.get(user_id=u,product_id=p)
	ui.status=Status
	ui.save()
	if(ui.status=='2' or ui.status==2):
		ui.delete()
	return JsonResponse({'status':0})
@csrf_exempt
def delete_account(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	u.delete()
	return JsonResponse({'status':0})

@csrf_exempt
def report_a_user(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	User_Id=input1['User_Id']
	u=users.objects.get(email=Email)
	u1=users.objects.get(user_id=User_Id)
	user_reporting.objects.create(reporter=u,reportee=u1,status=1)
	return JsonResponse({'status':0})

@csrf_exempt
def create_post():
	input1=json.loads(request.body)
	Email=input1['Email']
	category=""
	Category_Id=input1['Category_Id']
	if(Category_Id==1):
		category='Apartments'
	else if(Category_Id==2):
		category='Cabs'
	else if(Category_Id==3):
		category='Books'
	else:
		category='Laundary'
	price=input1['product']['Price']
	description=input1['product']['Description']
	product_name=input1['product']['Title']
	image_url=input1['product']['Image_Link']
	number_of_sharers=input1['product']['Sharers']
	number_of_sharers_left=input1['product']['Sharers']
	gender=input1['product']['Gender']
	p=products.objects.create(
		price=price,
		description=description,
		product_name=product_name,
		image_url=image_url,
		number_of_sharers=number_of_sharers,
		number_of_sharers_left=number_of_sharers_left,
		gender=gender
		)
