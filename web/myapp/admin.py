from django.contrib import admin

# Register your models here.

from .models import CPMS, Examinees, OJTInput

admin.site.register(CPMS)
admin.site.register(Examinees)
admin.site.register(OJTInput)