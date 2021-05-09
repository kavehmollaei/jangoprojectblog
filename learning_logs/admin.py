from django.contrib import admin

# Register your models here.

from .models import Topic,Person,Entry




admin.site.register(Topic)
admin.site.register(Person)
admin.site.register(Entry)