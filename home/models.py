from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Tag(models.Model):
    title_tag = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title_tag

    def __str__(self):              # __unicode__ on Python 2
        return self.title_tag
        





class Post(models.Model):

    title = models.CharField(max_length=200,blank=True,null =True)
    text = models.TextField(blank=True,null =True)
    author = models.CharField(max_length=400,blank=True,null =True)
    content = RichTextField(blank=True, null = True)
    tag_field = models.ManyToManyField('Tag')


    featured =  models.BooleanField(default = 'False')
    draft =  models.BooleanField(default = 'False')


    




    created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
    modified = models.DateTimeField(auto_now=True,blank=True, null = True)
