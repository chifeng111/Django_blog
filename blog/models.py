from django.db import models

# Create your models here.
def upload_location(object, filename):
    return "%s/%s" %(object.id, filename)


class Blog(models.Model):
    标题 = models.CharField(max_length=120)
    图片 = models.FileField(null=True, blank=True, upload_to=upload_location)
    内容 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True,auto_now_add=False)
    发布时间 = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.标题