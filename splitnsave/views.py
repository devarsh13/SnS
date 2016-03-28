from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from models import *
# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	Email='devarshsheth13@gmal.com'
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

def editprofile(request):
	userid='1'
	u=users.objects.get(user_id=0)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)

def userprofile(request):
	userid='0'
	u=users.objects.get(user_id=0)
	d={'user_id':u.user_id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email,'password':u.password,'verified':u.verified,'contact_number':u.contact_number,'city':u.city.city_name,'institute':u.institute.institute_name,'birthday':u.birthday,'profession':u.profession.profession_name,'gender':u.gender,'status':u.status}
	return JsonResponse(d)
	