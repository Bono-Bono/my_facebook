from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    # 이 아래부분은 부가적(해도 안해도 상관없음 !)
    def __str__(self):
        return self.title

# 코멘트 모델
class Comment(models.Model):
    article     = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author      = models.CharField(max_length=120)
    text        = models.TextField()
    password    = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
