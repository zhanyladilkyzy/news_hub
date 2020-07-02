from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class News(models.Model):
    title = models.CharField(max_length=200)
    author =  models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    #image
    #comments = models.CharField(max_length=500)
    #likes = models.CharField(max_length=500)
    publishing_data = models.DateTimeField()

    def __str__(self):
        return '{} {}'.format(self.created.strftime('%d.%m.%Y %H:%M'))


class Comments(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE,
                                related_name='news_comment')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE,
                                related_name='user_comment')
    feedback = models.CharField(max_length=500)

class Likes(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE,
                                related_name='news_like')
    user_id = models.ForeignKey(News, on_delete=models.CASCADE,
                                related_name='user_like')
    liked = models.CharField(max_length=10, blank=False, null=False)
