from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Article

content_type = ContentType.objects.get_for_model(Article)

permissions = {
    "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
    "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
    "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
    "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
}

editors, _ = Group.objects.get_or_create(name="Editors")
editors.permissions.set([permissions["can_view"], permissions["can_create"], permissions["can_edit"]])

viewers, _ = Group.objects.get_or_create(name="Viewers")
viewers.permissions.set([permissions["can_view"]])

admins, _ = Group.objects.get_or_create(name="Admins")
admins.permissions.set(permissions.values())

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)




# Register your models here.
