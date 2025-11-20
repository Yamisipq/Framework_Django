from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "pokemon_fav", "gender", "doc")
  
admin.site.register(Member, MemberAdmin)