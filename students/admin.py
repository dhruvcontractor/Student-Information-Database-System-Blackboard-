from django.contrib import admin
from .models import Student, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_gpa')
    list_select_related = ('profile', )

    def get_gpa(self, instance):
        return instance.profile.gpa
    get_gpa.short_description = 'GPA'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.site_header = 'Project App'
admin.site.register(Student)
