from django.contrib import admin

from toys.models import Brend, Toy, Category

# Register your models here.
admin.site.register(Toy)
admin.site.register(Brend)
admin.site.register(Category)
