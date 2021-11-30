from django.contrib import admin
from.models import category,product
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    #The attribute prepopulated_fields tells the admin application to automatically fill
    # the field slug - in this case with the text entered into the name field.
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)


class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,productadmin)