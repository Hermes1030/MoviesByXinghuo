from django.db import models


# Create your models here.
class movies(models.Model):
    name = models.CharField(verbose_name="电影名称", max_length=20, null=False, blank=True)
    status = models.TextField(verbose_name="基本信息", null=False, blank=True)
    describe = models.TextField(verbose_name="剧情内容", null=True, blank=True)
    rate = models.FloatField(verbose_name="得分")
