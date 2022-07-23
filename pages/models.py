from random import choices
from secrets import choice
from django.db import models
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

skills_choices = (
    ('Python', 'Python'),
    ('UI/UX', 'UI/UX'),
    ('HTML/CSS', 'HTML/CSS'),
    ('Postgres', 'Postgres'),
)

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=100)
    skills = MultiSelectField(choices=skills_choices)
    what_i_do = RichTextField()
    about = RichTextField()
    facebook_link = models.URLField(max_length=100)
    github_link = models.URLField(max_length=100)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    github_link = models.URLField(max_length=100)
    photo1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.name