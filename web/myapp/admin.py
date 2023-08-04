from django.contrib import admin

# Register your models here.

from .models import CPMS, Examinees, OJTInput, tmd

admin.site.register(CPMS)
admin.site.register(Examinees)
admin.site.register(OJTInput)
admin.site.register(tmd)