from django.contrib import admin
from home.models import contact_table
from home.models import order
from home.models import Add_product

admin.site.site_header = 'Restaurant Management System'
admin.site.site_title = 'My Restaurant'
admin.site.index_title = 'MAHI RESTAURANT'

# Register your models here.
admin.site.register(contact_table)
admin.site.register(Add_product)
admin.site.register(order)
