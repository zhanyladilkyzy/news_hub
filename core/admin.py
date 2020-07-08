from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import MainUserChangeForm, MainUserCreationForm
from .models import MainUser, Category, News, Like, Comment

# Register your models here.
# admin.site.register(Car)

admin.site.register(News)
# admin.site.register(UserTest)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'text', 'publishing_date')
    list_filter = ('title', 'publishing_date')
    search_fields = ('title', 'publishing_date')

# if use User model from django
# admin.site.unregister(User)

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     list_display = ('id', 'username')

# if extends from AbstractBaseUser and PermissionsMixin
@admin.register(MainUser)
class UserAdmin(UserAdmin):
    form = MainUserChangeForm
    add_form = MainUserCreationForm
    list_display = ('id', 'username', 'fullname')
    list_filter = ('is_superuser',)
    fieldsets = (
        ('Main Fields', dict(fields=(
            'username',
            'full_name',
        ))
        ),
        ('Password', {'fields': ('password',)}),
        ('Permissions',
         {'fields': ('groups', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )