from django.contrib import admin
from api.models import Api
# Register your models here.
class ApiAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    fields = ['query']

admin.site.register(Api, ApiAdmin)
