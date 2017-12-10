from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilma_tarihi = models.DateTimeField(default=timezone.now())
    yayinlanma_tarihi = models.DateTimeField(blank=True, null=True)


    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik

    def onaylanan_yorumlar(self):
        return self.comments.filter(onaylanma_durumu=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    yazar = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilma_tarihi = models.DateTimeField(default=timezone.now())
    onaylanma_durumu = models.BooleanField(default=False)

    def approve(self):
        self.onaylanma_durumu = True
        self.save()

    def __str__(self):
        return self.yazi

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(max_length=240, blank=True, null=True)
    avatar = models.ImageField(upload_to="user_imgs", blank=True, null=True)

    genders = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = models.CharField(max_length=1, choices=genders, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


