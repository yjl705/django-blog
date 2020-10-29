from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
class Post(models.Model):
    title = models.CharField(max_length=70) #标题
    
    body = models.TextField() #正文,可存储大端文本
    
    reated_time = models.DataTimeField() #分别表示文章的创建时间和最后一次修改时间
    odified_time = models.DateTimeField()

    xcerpt = models.CharField(max_length=200, blank=True) #文章摘要，可以没有
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE) #文章作者，User是django已经写好的用户模型
