# from django.db import models
from django import forms
from blog.models import *
 
CATEGORY = Category.objects.all()
 
class ArticleForm(forms.Form):
    title = forms.CharField(required=True, max_length=50)
    content = forms.CharField(widget=forms.Textarea())
    category = forms.ModelChoiceField(queryset=CATEGORY, empty_label='请选择分类')

# class MyModel(models.Model):
#     categories = models.ManyToManyField(
#         'category.Category',
#         help_text='Categorize this item.'
#     )
#     tags = models.ManyToManyField(
#         'category.Tag',
#         help_text='Tag this item.'
#     )

# class Category(models.Model):
#     category = models.CharField(max_length = 30, unique=True)   


#     name = models.CharField(max_length=100)

# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     def __unicode__(self):
#         return self.category


# class Post(models.Model):
#     category = models.ForeignKey(Category)

#     def __unicode__(self):
#         return self.title