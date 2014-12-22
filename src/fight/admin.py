from django.contrib import admin

# Register your models here.
from .models import User
from .models import Fight

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)

class FightAdmin(admin.ModelAdmin):
    class Meta:
        model = Fight

admin.site.register(Fight, FightAdmin)
