from django.db import models

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