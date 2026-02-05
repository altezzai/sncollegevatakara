from django.contrib import admin
from .models import IQACMember, GalleryItem, CampusLifePage, CampusLifeMember, CampusLifeGalleryItem, ScholarshipItem, ClubCommitteeItem

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


@admin.register(CampusLifePage)
class CampusLifePageAdmin(admin.ModelAdmin):
	list_display = ("title", "slug", "is_published", "sort_order", "updated_at")
	list_filter = ("is_published",)
	search_fields = ("title", "slug")
	prepopulated_fields = {"slug": ("title",)}
	ordering = ("sort_order", "title", "id")


@admin.register(CampusLifeMember)
class CampusLifeMemberAdmin(admin.ModelAdmin):
	list_display = ("name", "position", "page", "is_active", "sort_order")
	list_filter = ("is_active", "page")
	search_fields = ("name", "position")
	ordering = ("page", "sort_order", "name", "id")


@admin.register(CampusLifeGalleryItem)
class CampusLifeGalleryItemAdmin(admin.ModelAdmin):
	list_display = ("page", "media_type", "caption", "is_active", "created_at")
	list_filter = ("media_type", "is_active", "page")
	search_fields = ("caption", "video_url")
	ordering = ("-created_at", "-id")


@admin.register(ScholarshipItem)
class ScholarshipItemAdmin(admin.ModelAdmin):
	list_display = ("page", "name", "is_active", "created_at")
	list_filter = ("is_active", "page")
	search_fields = ("name", "description", "link_url")
	ordering = ("-created_at", "-id")


@admin.register(ClubCommitteeItem)
class ClubCommitteeItemAdmin(admin.ModelAdmin):
	list_display = ("page", "name", "person_name", "person_position", "is_active", "created_at")
	list_filter = ("is_active", "page")
	search_fields = ("name", "description", "person_name", "person_position")
	ordering = ("-created_at", "-id")
