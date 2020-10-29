from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Tag',max_length=70) #标题
    
    body = models.TextField('Text') #正文,可存储大端文本
    
    #created_time = models.DateTimeField('Created_time', default=timezone.now) #分别表示文章的创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField('Modified_time')

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt= strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)

    excerpt = models.CharField('Abstract',max_length=200, blank=True) #文章摘要，可以没有
    
    category = models.ForeignKey(Category,verbose_name='class', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='Tag', blank=True)
    
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE) #文章作者，User是django已经写好的用户模型

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
