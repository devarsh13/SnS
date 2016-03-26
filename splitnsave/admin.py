from django.contrib import admin
from .models import users,city_list
from django.db.models import get_models,get_app
# Register your models here.
for model in get_models(get_app('splitnsave')):
	admin.site.register(model)
