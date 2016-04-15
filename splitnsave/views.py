from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from models import *
from django.views.decorators.csrf import csrf_exempt
import json
import ast
from time import strptime
import smtplib
from datetime import datetime
# Create your views here.
def index(request):
	return render(request,'index.html')
@csrf_exempt
#Check Whether the email already exists in the database or not
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
#Get the user data upon signup from frontend and store it into database
@csrf_exempt
def signup(request):
	input1=json.loads(request.body)
	
	u=users.objects.create(first_name=input1['First_Name'],
		last_name=input1['Last_Name'],
		contact_number=input1['ContactNumber'],
		password=input1['Password'],
		email=input1['Email'],
		city=input1['City_Name'],
		birthday=input1['Birthdate'],
		gender=input1['Gender'],
		institute=input1['Institute_Name'],
		profession=input1['Profession_Name'],
		image_url=input1['Image_Link'])	


	return JsonResponse({'status':0,'First_Name':u.first_name})
#Send data for a given user from database to the frontend
@csrf_exempt
def editprofile(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	d={'details':{'User_Id':u.user_id,'First_Name':u.first_name,'Last_Name':u.last_name,'Email':u.email,'Password':u.password,'Verified':u.verified,'ContactNumber':u.contact_number,'CityName':u.city,'Institute_Name':u.institute,'Birthdate':u.birthday,'Profession_Name':u.profession,'Gender':u.gender,'Status':u.status,'Image_Link':u.image_url}}
	return JsonResponse(d)
#Update user data after the profile has changed
@csrf_exempt
def edit_profile_change(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	
	
	u=users.objects.get(email=Email)
	u.first_name=input1['First_Name']
	u.last_name=input1['Last_Name']
	u.contact_number=input1['ContactNumber']
	u.password=input1['Password']
	u.city=input1['CityName']
	u.birthday=input1['Birthdate']
	u.gender=input1['Gender']
	u.institute=input1['Institute_Name']
	u.profession=input1['Profession_Name']
	u.image_url=input1['Image_Link']
	u.save()
	return JsonResponse({'status':'0'})
#Send data for a given user from database to the frontend
@csrf_exempt
def userprofile(request):
	input1=json.loads(request.body)
	user_id=input1['User_Id']
	Email=input1['Email']
	u=users.objects.get(user_id=user_id)
	u1=users.objects.get(email=Email)
	temp=users.objects.get(email=Email)
	
	ui=user_interested.objects.filter(user_id=u)
	p=products.objects.filter(user_id=temp)
	status=0
	for i in p:

		for j in ui:

			if i.product_id==j.product_id.product_id and (j.status=='2' or j.status==2):
				status=1
				break
	
	ui1=user_interested.objects.filter(user_id=temp)
	p1=products.objects.filter(user_id=u)
	for i in p1:

		for j in ui1:

			if i.product_id==j.product_id.product_id and (j.status=='2' or j.status==2):
				status=1
				break
	try:
		ur=user_reporting.objects.get(reporter=u1,reportee=u)
		report_status=1
	except:
		report_status=0
		pass
	d={'details':{'User_Id':u.user_id,'First_Name':u.first_name,'Last_Name':u.last_name,'Email':u.email,'Password':u.password,'Verified':u.verified,'ContactNumber':u.contact_number,'CityName':u.city,'Institute':u.institute,'Birthdate':u.birthday,'Profession_Name':u.profession,'Gender':u.gender,'Status_Confirm':status,'Status_Report':report_status,'Institute_Name':u.institute,'Rating':u.rating,'Image_Link':u.image_url}}
	return JsonResponse(d)
#Send old password to frontend
@csrf_exempt
def settings(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	d={'Old_Password':u.password}
	return JsonResponse(d)
#update the old password
@csrf_exempt
def change_password(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	u.password=input1['New_Password']
	u.save()
	return JsonResponse({'status':0})
#Send Dashboard details to frontend
@csrf_exempt
def dashboard(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u1=users.objects.get(email=Email)
	p=products.objects.filter(user_id=u1)
	abc=user_interested.objects.filter(user_id=u1)

	u=[]
	for i in p:

		ui=user_interested.objects.filter(product_id=i,status=2)
		for j in ui:
			if j not in u:
				u.append(j.user_id)

	for i in abc:
		if(i.status==2):
			if i.product_id.user_id not in u:
				u.append(i.product_id.user_id)
	output = []
	seen = set()
	for value in u:
		if value not in seen:
			output.append(value)
			seen.add(value)
    

# Remove duplicates from this list.

	data={'users':[],'notifications':[{'Message':'aaaaa','Type':1}],'details':[]}
	for i in output:
		temp_dict={'First_Name':i.first_name,'Last_Name':i.last_name,'User_Id':i.user_id,'Image_Link':i.image_url}
		data['users'].append(temp_dict)

	data['details']={'First_Name':u1.first_name,'Last_Name':u1.last_name,'User_Id':u1.user_id,'Image_Link':u1.image_url}
	return JsonResponse(data)
#Send transaction history to the frontend
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
			rating=transaction_ratings.objects.get(product_id=temp,rater=rater,ratee=k)
			Status=0
			if(rating!=0):
				Status=1
			user_details={'First_Name':k.first_name,'Last_Name':k.last_name,'User_Id':k.user_id,'User_Image':k.image_url,'Rating':str(rating.rating),'Status':Status,'Image_Link':k.image_url}
			details['Sharer'].append(user_details)
		products.append(details)
	d={'products':products}
	return JsonResponse(d)
#update rating of a given user
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
	u1.rating=int(u1.rating)*u1.rated_by
	u1.rated_by=u1.rated_by+1

	u1.rating=str((int(u1.rating)+int(rating))/u1.rated_by)
	u1.save()
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
		if i.status==3:
			continue
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
	i.delete()
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
		p.number_of_sharers_left=p.number_of_sharers_left-1

	if(ui.status=='3' or ui.status==3):
		p.number_of_sharers_left=p.number_of_sharers_left+1
		ui.delete()
	
	
	return JsonResponse({'status':0})
@csrf_exempt	
def confirm_post(request):
	input1=json.loads(request.body)
	Product_Id=input1['Product_Id']
	p=products.objects.get(product_id=Product_Id)
	i=p
	u=user_interested.objects.filter(product_id=p,status=2)
	p.status=3
	p.save()
	for i in u:
		r=transaction_ratings.objects.create(product_id=p,rater=p.user_id,ratee=i.user_id,rating=0)
		r=transaction_ratings.objects.create(product_id=p,rater=i.user_id,ratee=p.user_id,rating=0)
		transaction_history.objects.create(seeker=i.user_id,product_id=p,poster=p.user_id,rating=r,transact_status=0)
		
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
	u1.reported_by=u1.reported_by+1
	u1.save()
	return JsonResponse({'status':0})

@csrf_exempt
def create_post(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	category=""
	Category_Id=input1['Category_Id']
	u=users.objects.get(email=Email)

	if(Category_Id=='1'):
		category='Apartments'
	elif(Category_Id=='2'):
		category='Cabs'
	elif(Category_Id=='3'):
		category='Books'
	else:
		category='Laundary'
	price1=input1['product']['Price']
	description1=input1['product']['Description']
	product_name1=input1['product']['Title']
	image_url1=input1['product']['Image_Link']
	number_of_sharers1=input1['product']['Sharers']
	number_of_sharers_left1=input1['product']['Sharers']
	gender1=input1['product']['Gender']
	
	ci=categories.objects.get(category_name=category)
	p=products.objects.create(
		category_id=ci,
		user_id=u,
		price=price1,
		description=description1,
		product_name=product_name1,
		image_url=image_url1,
		number_of_sharers=number_of_sharers1,
		number_of_sharers_left=number_of_sharers_left1,
		gender=gender1,
		
		)
	options=input1['options']
	ed=input1['subproduct']
	if(category=='Apartments'):

		a=apartments.objects.create(
			kitchen=options[0]['Option_Value'],
			internet=options[1]['Option_Value'],
			television=options[2]['Option_Value'],
			air_conditioner=options[3]['Option_Value'],
			heater=options[4]['Option_Value'],
			washing_machine=options[5]['Option_Value'],
			parking=options[6]['Option_Value'],
			smoking=options[7]['Option_Value'],
			wheelchair=options[8]['Option_Value'],
			elevator=options[9]['Option_Value'],
			gym=options[10]['Option_Value'],
			pool=options[11]['Option_Value'],
			fire_alarm=options[12]['Option_Value'],
			medical_aid=options[13]['Option_Value'],
			other_details=p,
			address=ed['Address'],
			rooms=ed['Rooms'],
			number_of_bedrooms=ed['Bed_Rooms'],
			number_of_bathrooms=ed['Bath_Rooms'],
			bathroom_type=ed['BathRoom_Type'],
			startdate=ed['Start_Date'],
			enddate=ed['End_Date'],
			in_time=ed['IN_Time_Value'],
			out_time=ed['OUT_Time_Value'],
			location=ed['Location']
		)
	elif(category=='Cabs'):
		
		
		
		c=cabs.objects.create(
			other_details=p,
			startdate=ed['Start_Date'],
			
			starttime=ed['Start_Time'],
			
			car_type=ed['CarType'],
			car_name=ed['CarName'],
			car_service=ed['CarService'],
			smoking=options[0]['Option_Value'],
			kids=options[1]['Option_Value'],
			luggage=options[2]['Option_Value'],
			pet=options[3]['Option_Value'],
			music=options[4]['Option_Value'],
			
			destination=ed['Location']
			)

	elif(category=='Books'):
		
		b=books.objects.create(
			other_details=p,
			startdate=ed['Start_Date'],
			enddate=ed['End_Date'],
			author_first_name=ed['Author_First_Name'],
			author_last_name=ed['Author_Last_Name'],
			location=ed['Location'],
			tag1=ed['Tag1'],
			tag2=ed['Tag2'],
			tag3=ed['Tag3'],
			college=ed['College']
			)
	else:
		
		l=laundary.objects.create(
			other_details=p,
			startdate=ed['Start_Date'],
			
			starttime=ed['Start_Time'],
			
			weight=ed['Weights'],
			white_clothes=options[0]['Option_Value'],
			light_clothes=options[1]['Option_Value'],
			dry_cleaning=options[2]['Option_Value'],
			steam_press=options[3]['Option_Value'],
			fabric_softner=options[4]['Option_Value'],
			)
	return JsonResponse({'status':0})

@csrf_exempt
def edit_post(request):
	input1=json.loads(request.body)
	Product_Id=input1['Product_Id']
	p=products.objects.get(product_id=Product_Id)
	i=p
	si=None
	d={'Category_Id':0,'product':{},'options':[],'subproduct':{}}
	if(i.category_id.category_name=='Books'):
		si=books.objects.get(other_details=p)
		d["Category_Id"]='3'
	elif(i.category_id.category_name=='Apartments'):
		si=apartments.objects.get(other_details=p)
		d["Category_Id"]='1'
	elif(i.category_id.category_name=='Laundary'):
		si=laundary.objects.get(other_details=p)
		d["Category_Id"]='4'
	else:
		si=cabs.objects.get(other_details=p)
		d["Category_Id"]='2'
	d['product']['Price']=i.price
	d['product']['Description']=i.description
	d['product']['Title']=i.product_name
	d['product']['Image_Link']=i.image_url
	d['product']['Sharers']=i.number_of_sharers
	d['product']['Sharers_Left']=i.number_of_sharers_left
	d['product']['Gender']=i.gender
	d['product']['Post_Date']=i.post_date
	d['product']['Location']=i.location
	d['Product_Id']=Product_Id
	if(d["Category_Id"]=='3'):
		d['subproduct']['Start_Date']=si.startdate
		d['subproduct']['End_Date']=si.enddate
		d['subproduct']['Author_First_Name']=si.author_first_name
		d['subproduct']['Author_Last_Name']=si.author_last_name
		d['subproduct']['Tag1']=si.tag1
		d['subproduct']['Tag2']=si.tag2
		d['subproduct']['Tag3']=si.tag3
		d['subproduct']['Location']=si.location
		d['subproduct']['College']=si.college

	if(d['Category_Id']=='1'):
		d['options'].append({'Option_Name':'Kitchen','Option_Value':si.kitchen})
		d['options'].append({'Option_Name':'Internet','Option_Value':si.internet})
		d['options'].append({'Option_Name':'Television','Option_Value':si.television})
		d['options'].append({'Option_Name':'A.C','Option_Value':si.air_conditioner})
		d['options'].append({'Option_Name':'Heater','Option_Value':si.heater})
		d['options'].append({'Option_Name':'Washing Machine','Option_Value':si.washing_machine})
		d['options'].append({'Option_Name':'Parking Space','Option_Value':si.parking})
		d['options'].append({'Option_Name':'No Smoking','Option_Value':si.smoking})
		d['options'].append({'Option_Name':'Wheelchair Support','Option_Value':si.wheelchair})
		d['options'].append({'Option_Name':'Elevator','Option_Value':si.elevator})
		d['options'].append({'Option_Name':'Gym','Option_Value':si.gym})
		d['options'].append({'Option_Name':'Pool','Option_Value':si.pool})
		d['options'].append({'Option_Name':'Fire exit alarm','Option_Value':si.fire_alarm})
		d['options'].append({'Option_Name':'First-Aid-Kit','Option_Value':si.medical_aid})
		d['subproduct']['Rooms']=si.rooms
		d['subproduct']['Bed_Rooms']=si.number_of_bedrooms
		d['subproduct']['Bath_Rooms']=si.number_of_bathrooms
		d['subproduct']['IN_Time_Value']=si.in_time
		d['subproduct']['OUT_Time_Value']=si.out_time
		d['subproduct']['Location']=si.location
		d['product']['Address']=si.address
		d['product']['Start_Date']=si.startdate
		d['product']['End_Date']=si.enddate
		d['product']['BathRoom_Type']=si.bathroom_type

	if(d['Category_Id']=='2'):
		d['options'].append({'Option_Name':'No Smoking','Option_Value':si.smoking})
		d['options'].append({'Option_Name':'No Kids','Option_Value':si.kids})
		d['options'].append({'Option_Name':'No Luggage','Option_Value':si.luggage})
		d['options'].append({'Option_Name':'No Pets','Option_Value':si.pet})
		d['options'].append({'Option_Name':'No Music','Option_Value':si.music})
		d['options'].append({'Option_Name':'Non Stop Journey','Option_Value':si.non_stop_journey})
		d['subproduct']['Location']=si.destination
		d['subproduct']['Start_Date']=si.startdate
		
		d['subproduct']['End_Date']=si.enddate
		
		d['subproduct']['CarService']=si.car_service
		d['subproduct']['CarName']=si.car_name
		d['subproduct']['CarType']=si.car_type

	if(d['Category_Id']=='4'):
		d['options'].append({'Option_Name':'White Clothes','Option_Value':si.white_clothes})
		d['options'].append({'Option_Name':'Light Clothes','Option_Value':si.light_clothes})
		d['options'].append({'Option_Name':'Cotton Clothes','Option_Value':si.cotton_clothes})
		d['options'].append({'Option_Name':'Silk Clothes','Option_Value':si.silk_clothes})
		d['options'].append({'Option_Name':'Dry Cleaning','Option_Value':si.dry_cleaning})
		d['options'].append({'Option_Name':'Steam Press','Option_Value':si.steam_press})
		d['options'].append({'Option_Name':'Fabric Softner','Option_Value':si.fabric_softner})
		d['subproduct']['Start_Date']=si.startdate
		d['subproduct']['End_Date']=si.enddate
	
		d['subproduct']['Weights']=si.weight

	return JsonResponse(d)

@csrf_exempt
def edit_data(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	category=""
	Category_Id=input1['Category_Id']
	u=users.objects.get(email=Email)
	Product_Id=input1['Product_Id']
	p=products.objects.get(product_id=Product_Id)
	i=p
	if(Category_Id=='1'):
		category='Apartments'
	elif(Category_Id=='2'):
		category='Cabs'
	elif(Category_Id=='3'):
		category='Books'
	else:
		category='Laundary'
	price1=input1['product']['Price']
	description1=input1['product']['Description']
	product_name1=input1['product']['Title']
	image_url1=input1['product']['Image_Link']
	number_of_sharers1=input1['product']['Sharers']
	number_of_sharers_left1=input1['product']['Sharers']
	gender1=input1['product']['Gender']
	ci=categories.objects.get(category_name=category)
	
	i.category_id=ci
	i.user_id=u
	i.price=price1
	i.description=description1
	i.product_name=product_name1
	i.image_url=image_url1
	i.number_of_sharers=number_of_sharers1
	i.number_of_sharers_left=number_of_sharers_left1
	i.gender=gender1
	i.save()
	options=input1['options']
	ed=input1['subproduct']

	if(category=='Apartments'):
		a=apartments.objects.get(other_details=p)
		c.startdate=ed['Start_Date']
		c.enddate=ed['End_Date']
		a.kitchen=options[0]['Option_Value']
		a.internet=options[1]['Option_Value']
		a.television=options[2]['Option_Value']
		a.air_conditioner=options[3]['Option_Value']
		a.heater=options[4]['Option_Value']
		a.washing_machine=options[5]['Option_Value']
		a.parking=options[6]['Option_Value']
		a.smoking=options[7]['Option_Value']
		a.wheelchair=options[8]['Option_Value']
		a.elevator=options[9]['Option_Value']
		a.gym=options[10]['Option_Value']
		a.pool=options[11]['Option_Value']
		a.fire_alarm=options[12]['Option_Value']
		a.medical_aid=options[13]['Option_Value']
		a.other_details=p
		a.rooms=ed['Rooms']
		a.number_of_bedrooms=ed['Bed_Rooms']
		a.number_of_bathrooms=ed['Bath_Rooms']
		a.bathroom_type=ed['BathRoom_Type']
		a.in_time=ed['IN_Time_Value']
		a.out_time=ed['OUT_Time_Value']
		a.address=ed['Address']
		a.startdate=ed['Start_Date']
		a.enddate=ed['End_Date']
		a.location=ed['Location']
		a.save()
	elif(category=='Cabs'):
		
		
		c=cabs.objects.get(other_details=p)
		
		c.other_details=p
		c.startdate=ed['Start_Date']
		
		c.starttime=ed['Start_Time']
		
		c.car_type=ed['CarType']
		c.car_name=ed['CarName']
		c.car_service=ed['CarService']
		c.smoking=options[0]['Option_Value']
		c.kids=options[1]['Option_Value']
		c.luggage=options[2]['Option_Value']
		c.pets=options[3]['Option_Value']
		c.music=options[4]['Option_Value']
		
		c.destination=ed['Location']
			
	elif(category=='Books'):
		
		b=books.objects.get(other_details=p)
		
		b.other_details=p
		b.startdate=ed['Start_Date']
		b.enddate=ed['End_Date']
		b.author_first_name=ed['Author_First_Name']
		b.author_last_name=ed['Author_Last_Name']
		b.location=ed['Location']
		b.tag1=ed['Tag1']
		b.tag2=ed['Tag2']
		b.tag3=ed['Tag3']
		b.college=ed['College']
		b.save()
	else:
		
		
		l=laundary.objects.get(other_details=p)

		
		l.other_details=p
		l.startdate=ed['Start_Date']
		l.starttime=ed['Start_Time']
		
		l.weight=ed['Weights']
		l.white_clothes=options[0]['Option_Value']
		l.light_clothes=options[1]['Option_Value']
		
		l.dry_cleaning=options[2]['Option_Value']
		l.steam_press=options[3]['Option_Value']
		l.fabric_softner=options[4]['Option_Value']
		l.save()
	return JsonResponse({'status':0})

@csrf_exempt
def send_email(request):

	
	to = 'tanayagl@gmail.com'
	user = 'devarshsheth13@gmail.com'
	pwd = 'idontknowits13'
	smtpserver = smtplib.SMTP("smti.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo() # extra characters to permit edit
	smtpserver.login(user, pwd)
	header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:testing \n'
	print header
	msg = header + '\n this is test msg from splitnsave \n\n'
	smtpserver.sendmail(user, to, msg)
	print 'done!'
	smtpserver.quit()
	return JsonResponse({'status':0})

@csrf_exempt
def product_details(request):
	input1=json.loads(request.body)
	
	Product_Id=input1['Product_Id']
	p=products.objects.get(product_id=Product_Id)
	i=p
	u=i.user_id
	si=None
	d={'Category_Id':0,'product':{},'options':[],'user':{}}
	if(i.category_id.category_name=='Books'):
		si=books.objects.get(other_details=p)
		d["Category_Id"]='3'
	elif(i.category_id.category_name=='Apartments'):
		si=apartments.objects.get(other_details=p)
		d["Category_Id"]='1'
	elif(i.category_id.category_name=='Laundary'):
		si=laundary.objects.get(other_details=p)
		d["Category_Id"]='4'
	else:
		si=cabs.objects.get(other_details=p)
		d["Category_Id"]='2'
	d['product']['Price']=i.price
	d['product']['Description']=i.description
	d['product']['Title']=i.product_name
	d['product']['Image_Link']=i.image_url
	d['product']['Sharers']=i.number_of_sharers
	d['product']['Sharers_Left']=i.number_of_sharers_left
	d['product']['Gender']=i.gender
	d['product']['Post_Date']=i.post_date
	d['product']['Location']=i.location
	d['product']['Product_Id']=i.product_id
	if(d["Category_Id"]=='3'):
		d['product']['Start_Date']=si.startdate
		d['product']['End_Date']=si.enddate
		d['product']['Author_First_Name']=si.author_first_name
		d['product']['Author_Last_Name']=si.author_last_name
		d['product']['Tag1']=si.tag1
		d['product']['Tag2']=si.tag2
		d['product']['Tag3']=si.tag3
		d['product']['Location']=si.location
		d['product']['College']=si.college

	if(d['Category_Id']=='1'):
		d['options'].append({'Option_Name':'Kitchen','Option_Value':si.kitchen})
		d['options'].append({'Option_Name':'Internet','Option_Value':si.internet})
		d['options'].append({'Option_Name':'Television','Option_Value':si.television})
		d['options'].append({'Option_Name':'A.C','Option_Value':si.air_conditioner})
		d['options'].append({'Option_Name':'Heater','Option_Value':si.heater})
		d['options'].append({'Option_Name':'Washing Machine','Option_Value':si.washing_machine})
		d['options'].append({'Option_Name':'Parking Space','Option_Value':si.parking})
		d['options'].append({'Option_Name':'No Smoking','Option_Value':si.smoking})
		d['options'].append({'Option_Name':'Wheelchair Support','Option_Value':si.wheelchair})
		d['options'].append({'Option_Name':'Elevator','Option_Value':si.elevator})
		d['options'].append({'Option_Name':'Gym','Option_Value':si.gym})
		d['options'].append({'Option_Name':'Pool','Option_Value':si.pool})
		d['options'].append({'Option_Name':'Fire exit alarm','Option_Value':si.fire_alarm})
		d['options'].append({'Option_Name':'First-Aid-Kit','Option_Value':si.medical_aid})
		d['product']['Rooms']=si.rooms
		d['product']['Bed_Rooms']=si.number_of_bedrooms
		d['product']['Bath_Rooms']=si.number_of_bathrooms
		d['product']['IN_Time_Value']=si.in_time
		d['product']['OUT_Time_Value']=si.out_time
		d['product']['Location']=si.location
		d['product']['Address']=si.address
		d['product']['Start_Date']=si.startdate
		d['product']['End_Date']=si.enddate
		d['product']['BathRoom_Type']=si.bathroom_type
	if(d['Category_Id']=='2'):
		d['options'].append({'Option_Name':'No Smoking','Option_Value':si.smoking})
		d['options'].append({'Option_Name':'No Kids','Option_Value':si.kids})
		d['options'].append({'Option_Name':'No Luggage','Option_Value':si.luggage})
		d['options'].append({'Option_Name':'No Pets','Option_Value':si.pet})
		d['options'].append({'Option_Name':'No Music','Option_Value':si.music})
		d['options'].append({'Option_Name':'Non Stop Journey','Option_Value':si.non_stop_journey})
		d['product']['Location']=si.destination
		d['product']['Start_Date']=si.startdate
		
		d['product']['End_Date']=si.enddate
		
		d['product']['CarService']=si.car_service
		d['product']['CarName']=si.car_name
		d['product']['CarType']=si.car_type

	if(d['Category_Id']=='4'):
		d['options'].append({'Option_Name':'White Clothes','Option_Value':si.white_clothes})
		d['options'].append({'Option_Name':'Light Clothes','Option_Value':si.light_clothes})
		d['options'].append({'Option_Name':'Cotton Clothes','Option_Value':si.cotton_clothes})
		d['options'].append({'Option_Name':'Silk Clothes','Option_Value':si.silk_clothes})
		d['options'].append({'Option_Name':'Dry Cleaning','Option_Value':si.dry_cleaning})
		d['options'].append({'Option_Name':'Steam Press','Option_Value':si.steam_press})
		d['options'].append({'Option_Name':'Fabric Softner','Option_Value':si.fabric_softner})
		d['product']['Start_Date']=si.startdate
		d['product']['End_Date']=si.enddate
		
		d['product']['Weights']=si.weight

	d['user']['First_Name']=u.first_name
	d['user']['Last_Name']=u.last_name
	d['user']['Image_Link']=u.image_url
	d['user']['rating']=u.rating
	d['user']['User_Id']=u.user_id
	d['user']['Email']=u.email
	try:
		Email=input1['Email']
		u1=users.objects.get(email=Email)
		d['user']['Status_Confirm']=user_interested.objects.get(user_id=u1,product_id=p).status
		try:
			d['user']['Status_Report']=user_report_post.objects.get(user_id=u1,product_id=p).status
		except:
			d['user']['Status_Report']='0'
	except:
		d['user']['Status_Confirm']='0'
		try:
			d['user']['Status_Report']=user_report_post.objects.get(user_id=u1,product_id=p).status
		except:
			d['user']['Status_Report']='0'

	return JsonResponse(d)

@csrf_exempt
def login(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	Password=input1['Password']
	flag=1
	try:
		u=users.objects.get(email=Email,password=Password)
		flag=0
	except:
		pass
	if(flag==0):
		return JsonResponse({'status':0,'First_Name':u.first_name})
	else:
		return JsonResponse({'status':1,'First_Name':''})
@csrf_exempt
def send_request(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	Product_Id=input1['Product_Id']
	p=products.objects.get(product_id=Product_Id)
	u=users.objects.get(email=Email)
	
	user_interested.objects.create(product_id=p,user_id=u,status=1)


	return JsonResponse({'status':0})
@csrf_exempt
def report_product(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	Product_Id=input1['Product_Id']
	p=products.objects.get(product_id=Product_Id)
	u=users.objects.get(email=Email)
	
	user_report_post.objects.create(product_id=p,user_id=u,status=1)

	return JsonResponse({'status':0})

@csrf_exempt
def category_products(request):
	input1=json.loads(request.body)
	Category_Id=input1['Category_Id']
	name=''
	sp=None
	products1=[]
	if(Category_Id==1 or Category_Id=='1'):
		name='Apartments'
	if(Category_Id==2 or Category_Id=='2'):
		name='Cabs'
		
	if(Category_Id==3 or Category_Id=='3'):
		name='Books'
		
	if(Category_Id==4 or Category_Id=='4'):
		name='Laundary'
	c=categories.objects.get(category_name=name)
	#return JsonResponse({'a':c.category_name})
	try:
		p=products.objects.filter(category_id=c,status=0)
		
	except:
		return JsonResponse({'products':products1})
	d={'Category_Id':0,'product':{'options':[]},'user':{}}
	
	
	
	
	for i in p:

		d={'Category_Id':0,'product':{'options':[]},'user':{}}
		if(Category_Id==1 or Category_Id=='1'):
			sp=apartments.objects.get(other_details=i)
		
			d["Category_Id"]='1'
		if(Category_Id==2 or Category_Id=='2'):
			sp=cabs.objects.get(other_details=i)
			name='Cabs'
			d["Category_Id"]='2'
		if(Category_Id==3 or Category_Id=='3'):
			name='Books'
			d["Category_Id"]='3'
			sp=books.objects.get(other_details=i)
		if(Category_Id==4 or Category_Id=='4'):
			name='Laundary'
			d["Category_Id"]='4'
			sp=laundary.objects.get(other_details=i)
		d['product']['Price']=i.price
		d['product']['Description']=i.description
		d['product']['Title']=i.product_name
		d['product']['Image_Link']=i.image_url
		d['product']['Sharers']=i.number_of_sharers
		d['product']['Sharers_Left']=i.number_of_sharers_left
		d['product']['Gender']=i.gender
		d['product']['Post_Date']=i.post_date
		d['product']['Location']=i.location
		d['product']['Product_Id']=i.product_id
		d['product']['Hosted']=str(i.user_id.first_name)+" "+str(i.user_id.last_name)
		if(d["Category_Id"]=='3'):
			d['product']['Start_Date']=sp.startdate
			d['product']['End_Date']=sp.enddate
			d['product']['Author_First_Name']=sp.author_first_name
			d['product']['Author_Last_Name']=sp.author_last_name
			d['product']['Tag1']=sp.tag1
			d['product']['Tag2']=sp.tag2
			d['product']['Tag3']=sp.tag3
			d['product']['Location']=sp.location
			d['product']['College']=sp.college

		if(d['Category_Id']=='1'):
			d['product']['options'].append({'Option_Name':'Kitchen','Option_Value':sp.kitchen})
			d['product']['options'].append({'Option_Name':'Internet','Option_Value':sp.internet})
			d['product']['options'].append({'Option_Name':'Television','Option_Value':sp.television})
			d['product']['options'].append({'Option_Name':'A.C','Option_Value':sp.air_conditioner})
			d['product']['options'].append({'Option_Name':'Heater','Option_Value':sp.heater})
			d['product']['options'].append({'Option_Name':'Washing Machine','Option_Value':sp.washing_machine})
			d['product']['options'].append({'Option_Name':'Parking Space','Option_Value':sp.parking})
			d['product']['options'].append({'Option_Name':'No Smoking','Option_Value':sp.smoking})
			d['product']['options'].append({'Option_Name':'Wheelchair Support','Option_Value':sp.wheelchair})
			d['product']['options'].append({'Option_Name':'Elevator','Option_Value':sp.elevator})
			d['product']['options'].append({'Option_Name':'Gym','Option_Value':sp.gym})
			d['product']['options'].append({'Option_Name':'Pool','Option_Value':sp.pool})
			d['product']['options'].append({'Option_Name':'Fire exit alarm','Option_Value':sp.fire_alarm})
			d['product']['options'].append({'Option_Name':'First-Aid-Kit','Option_Value':sp.medical_aid})
			d['product']['Rooms']=sp.rooms
			d['product']['Bed_Rooms']=sp.number_of_bedrooms
			d['product']['Bath_Rooms']=sp.number_of_bathrooms
			d['product']['IN_Time_Value']=sp.in_time
			d['product']['OUT_Time_Value']=sp.out_time
			d['product']['Location']=sp.location

		if(d['Category_Id']=='2'):
			d['product']['options'].append({'Option_Name':'No Smoking','Option_Value':sp.smoking})
			d['product']['options'].append({'Option_Name':'Kids','Option_Value':sp.kids})
			d['product']['options'].append({'Option_Name':'Luggage','Option_Value':sp.luggage})
			d['product']['options'].append({'Option_Name':'Pets','Option_Value':sp.pet})
			d['product']['options'].append({'Option_Name':'Music','Option_Value':sp.music})
			d['product']['options'].append({'Option_Name':'Non Stop Journey','Option_Value':sp.non_stop_journey})
			d['product']['Location']=sp.destination
			d['product']['Start_Date']=sp.startdate
			
			d['product']['End_Date']=sp.enddate
			
			d['product']['CarService']=sp.car_service
			d['product']['CarName']=sp.car_name
			d['product']['CarType']=sp.car_type

		if(d['Category_Id']=='4'):
			d['product']['options'].append({'Option_Name':'White Clothes','Option_Value':sp.white_clothes})
			d['product']['options'].append({'Option_Name':'Light Clothes','Option_Value':sp.light_clothes})
			d['product']['options'].append({'Option_Name':'Cotton Clothes','Option_Value':sp.cotton_clothes})
			d['product']['options'].append({'Option_Name':'Silk Clothes','Option_Value':sp.silk_clothes})
			d['product']['options'].append({'Option_Name':'Dry Cleaning','Option_Value':sp.dry_cleaning})
			d['product']['options'].append({'Option_Name':'Steam Press','Option_Value':sp.steam_press})
			d['product']['options'].append({'Option_Name':'Fabric Softner','Option_Value':sp.fabric_softner})
			d['product']['Start_Date']=sp.startdate
			d['product']['End_Date']=sp.enddate
			
			
			d['product']['Weights']=sp.weight

		
		products1.append(d)
	return JsonResponse({'products':products1})

@csrf_exempt
def send_users(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	u=users.objects.get(email=Email)
	u1=user_interested.objects.filter(user_id=u)
	p=products.objects.filter(user_id=u)
	u2=user_interested.objects.filter(product_id=p)
	users2=[]
	users1=[]
	for i in u1:
		if(i.status==2 or i.status=='2'):
			users2.append(i.product_id.user_id)
	for i in u2:
		if(i.status==2 or i.status=='2'):
			users2.append(i.user_id)
	output = []
	seen = set()
	for value in users2:
		if value not in seen:
			output.append(value)
			seen.add(value)
	for i in output:
		temp={'First_Name':i.first_name,'Last_Name':i.last_name,'Image_Link':i.image_url,'User_Id':i.user_id}
		users1.append(temp)
	return JsonResponse({'Users':users1})
@csrf_exempt
def chat_history_data(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	User_Id=input1['User_Id']
	u1=users.objects.get(email=Email)
	u2=users.objects.get(user_id=User_Id)
	ch=chat_history.objects.filter(sender=u1,receiver=u2)
	ch1=chat_history.objects.filter(sender=u2,receiver=u1)
	users1=[]
	chats=[]
	
	for i in ch:
		chat={'username':i.sender.first_name,'User2':i.receiver.first_name,'content':i.message,'Timestamp':i.timestamp}
		chats.append(chat)
	for i in ch1:
		chat={'username':i.sender.first_name,'User2':i.receiver.first_name,'content':i.message,'Timestamp':i.timestamp}
		chats.append(chat)
	for i in xrange(0,len(chats)):
		for j in xrange(i,len(chats)-1):
			if(chats[j]['Timestamp']>chats[j+1]['Timestamp']):
				temp=chats[j]
				chats[j]=chats[j+1]
				chats[j+1]=temp
	return JsonResponse({'Users':users1,'Chats':chats})



@csrf_exempt
def add_chat(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	User_Id=input1['User_Id']
	u1=users.objects.get(email=Email)
	u2=users.objects.get(user_id=User_Id)
	Message=input1['Message']
	chat_history.objects.create(sender=u1,receiver=u2,message=Message,timestamp=datetime.now())


	return JsonResponse({'status':0})

@csrf_exempt
def verify_user(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	to = Email
	user = 'splitnsave25@gmail.com'
	pwd = 'splitnsave25@'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo() # extra characters to permit edit
	smtpserver.login(user, pwd)
	header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:Verification \n'
	print header
	import random
	import string

	digits = "".join( [random.choice(string.digits) for i in xrange(3)] )
	chars = "".join( [random.choice(string.letters) for i in xrange(3)] )
	code = digits + chars
	msg = header + '\n Your Verification Code is %s \n\n'%code
	smtpserver.sendmail(user, to, msg)
	print 'done!'
	smtpserver.quit()
	return JsonResponse({'code':code})

@csrf_exempt
def forgot_password(request):
	input1=json.loads(request.body)
	Email=input1['Email']
	to = Email
	user = 'splitnsave25@gmail.com'
	pwd = 'splitnsave25@'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo() # extra characters to permit edit
	smtpserver.login(user, pwd)
	header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:Password Change \n'
	print header
	import random
	import string

	digits = "".join( [random.choice(string.digits) for i in xrange(4)] )
	chars = "".join( [random.choice(string.letters) for i in xrange(4)] )
	code = digits + chars
	msg = header + '\n Your New Password is %s \n\n'%code
	smtpserver.sendmail(user, to, msg)
	print 'done!'
	smtpserver.quit()
	

	u=users.objects.get(email=Email)
	u.password=code
	u.save()
	return JsonResponse({'status':0})