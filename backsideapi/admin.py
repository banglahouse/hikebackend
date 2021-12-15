from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  as BaseUser
# Register your models here.
from .models import MenuItem , NewOrderTable


# Register your models here.

# admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(NewOrderTable)
# admin.site.register(OrderBy)
# admin.site.register(OrderDetails)



#pass
