from django.db import models
from apps.devtools.models import *

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=255)
    image = models.ImageField(upload_to='idea_images/%Y%m%d', null=True, blank=True)
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', default=0)
    # devtool
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name='예상 개발툴', related_name="idea")

    def __str__(self):
        return self.title