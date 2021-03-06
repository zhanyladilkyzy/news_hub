from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.

class MainUserManager(BaseUserManager):
    """
        Main user manager
        Methods
        -------
        create_user(self, username, password=None, full_name=None, email=None)
            creates user with params
    """

    def create_user(self, username, password=None, full_name=None):
        """
        Creates user
        :param username: username of user
        :type username: str
        :return: instance of user
        Attributes
        ----------
        username: str
            username of user
        """
        if not username:
            raise ValueError('User must have a username')
        user = self.model(username=username, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MainUser(AbstractBaseUser, PermissionsMixin):
    """ Repersent a "user profile" inside our system """
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'


    objects = MainUserManager()

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.title, self.description)

class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return '{} {}'.format(self.news, self.user, self.feedback)

class Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.news, self.user, self.liked)

    # метод возвращаюший количество лайков

