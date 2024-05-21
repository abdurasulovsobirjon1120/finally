from django.contrib import admin
from .models import Maqola

# Register your models here.
@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title' ,'author' , 'created_at' ]
    class Meta:
        model = Maqola