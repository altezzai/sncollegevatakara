from django.db import models
import uuid

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')
    qualification = models.TextField()

class Event(models.Model):
    title = models.CharField(max_length=200)
    time = models.TimeField()
    date = models.DateField()
    description = models.TextField()
    venue = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    def __str__(self):
        return self.title
class NewsImage(models.Model):
    news_article = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news_images/')

class Notification(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.title
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)  # optional, to enable/disable a banner
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Banner {self.id}"        


class AnnualReport(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    file = models.FileField(upload_to='annual_reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-id']

    def __str__(self):
        return f"{self.year} - {self.title}"


class IQACMember(models.Model):
    ROLE_COORDINATOR = "coordinator"
    ROLE_JOINT_COORDINATOR = "joint_coordinator"
    ROLE_MEMBER = "member"

    ROLE_CHOICES = (
        (ROLE_COORDINATOR, "Coordinator"),
        (ROLE_JOINT_COORDINATOR, "Joint Coordinator"),
        (ROLE_MEMBER, "Member"),
    )

    name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='iqac/', null=True, blank=True)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default=ROLE_MEMBER)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["role", "name", "id"]

    def __str__(self):
        return f"{self.name} ({self.department}) - {self.role}"


class GalleryItem(models.Model):
    TYPE_IMAGE = "image"
    TYPE_VIDEO = "video"

    TYPE_CHOICES = (
        (TYPE_IMAGE, "Photo"),
        (TYPE_VIDEO, "Media (Video)"),
    )

    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default=TYPE_IMAGE)
    # For videos, use `file`. For photos, store multiple images via related GalleryImage.
    file = models.FileField(upload_to='gallery/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return f"{self.title} ({self.media_type})"


class GalleryImage(models.Model):
    gallery_item = models.ForeignKey(GalleryItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Image for {self.gallery_item_id}"


class CampusLifePage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    content = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='campus_life/', null=True, blank=True)
    attachment = models.FileField(upload_to='campus_life/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "title", "id"]

    def __str__(self):
        return self.title


class CampusLifeMember(models.Model):
    page = models.ForeignKey(CampusLifePage, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='campus_life/members/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "name", "id"]

    def __str__(self):
        return f"{self.name} - {self.position}"


class CampusLifeGalleryItem(models.Model):
    TYPE_IMAGE = "image"
    TYPE_VIDEO = "video"

    TYPE_CHOICES = (
        (TYPE_IMAGE, "Photo"),
        (TYPE_VIDEO, "Video"),
    )

    page = models.ForeignKey(CampusLifePage, on_delete=models.CASCADE, related_name='gallery_items')
    upload_batch = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    media_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default=TYPE_IMAGE)
    caption = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='campus_life/gallery/', null=True, blank=True)
    video_file = models.FileField(upload_to='campus_life/gallery/', null=True, blank=True)
    video_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return f"{self.page.slug} - {self.media_type}"


class ScholarshipItem(models.Model):
    page = models.ForeignKey(CampusLifePage, on_delete=models.CASCADE, related_name='scholarship_items')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='campus_life/scholarships/', null=True, blank=True)
    description = models.TextField(blank=True)
    link_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return self.name


class ClubCommitteeItem(models.Model):
    page = models.ForeignKey(CampusLifePage, on_delete=models.CASCADE, related_name='club_committee_items')
    name = models.CharField(max_length=220)
    description = models.TextField()
    person_name = models.CharField(max_length=180)
    person_position = models.CharField(max_length=180)
    person_photo = models.ImageField(upload_to='campus_life/clubs/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return self.name


class AddOnCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return self.title