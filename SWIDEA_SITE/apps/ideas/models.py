from django.db import models
from apps.devtools.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=255)
    image = models.ImageField(upload_to='idea_images/%Y%m%d', null=True, blank=True)
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', default=0)
    # devtool
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name='예상 개발툴', related_name="idea")
    #생성 시각
    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)
    

    def __str__(self):
        return self.title
    

@receiver(post_save, sender=Idea)
def create_idea_star(sender, instance, created, **kwargs):
    """
    Idea 모델이 저장될 때 IdeaStar 모델을 자동으로 생성하는 신호 핸들러
    """
    if created:
        # Idea 모델이 처음 생성된 경우에만 IdeaStar 모델을 생성
        IdeaStar.objects.create(idea=instance, star=False)

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    star = models.BooleanField(default=False)