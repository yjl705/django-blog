from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    url = models.URLField('URL', blank=True)
    text = models.TextField('Text')
    created_time = models.DateTimeField('Created_time', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='Article', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = verbose_name


    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
