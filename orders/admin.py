from django.contrib import admin


from django.contrib import admin
from orders.models import Order


class LengowTestAdmin(admin.AdminSite):
    site_header = 'Lengow administration'


admin_site = LengowTestAdmin(name='admin')


admin.site.register(Order)