from django.db import models
from django.utils import timezone


class Card(models.Model):
    avatar1 = models.ImageField(default='avatar1.png')
    avatar2 = models.ImageField(default='avatar2.png')
    name_card = models.CharField(max_length=30)
    occupation = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now
        self.save()

    def __str__(self):
        return self.name_card


class Social(models.Model):
    social_network_name = models.CharField(max_length=30)
    social_network_link = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now
        self.save()

    def __str__(self):
        return self.social_network_name


class ShareOn(models.Model):
    social_network_name = models.CharField(max_length=30)
    social_network_link = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now
        self.save()

    def __str__(self):
        return self.social_network_name


class About(models.Model):
    title = models.CharField(max_length=30)
    introduction = models.CharField(max_length=30)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now
        self.save()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(default='project-image.png')
    project_link = models.CharField(max_length=200)

    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now
        self.save()

    def __str__(self):
        return self.title


class HeadTag(models.Model):
    og_url = models.CharField(max_length=200, default='https://flavialopes.dev')
    og_type = models.CharField(max_length=200, default='website')
    og_title = models.CharField(max_length=200)
    og_description = models.CharField(max_length=200)
    og_image = models.ImageField(default='logo.png')
    og_site_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    keywords = models.CharField(max_length=200)
    title = models.CharField(max_length=20)

    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now
        self.save()

    def __str__(self):
        return self.title
