from django.contrib import admin
from .models import IQACMember, GalleryItem

# Register your models here.


@admin.register(IQACMember)
class IQACMemberAdmin(admin.ModelAdmin):
	list_display = ("name", "department", "role", "is_active")
	list_filter = ("role", "is_active")
	search_fields = ("name", "department")


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
	list_display = ("title", "media_type", "is_active", "created_at")
	list_filter = ("media_type", "is_active")
	search_fields = ("title",)
