from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Post(models.Model):

    genre_dict = {
        "Games": "G",
        "Movies": "M"
    }

    rating = {
        "Bad": "1",
        "Average": "2",
        "Good": "3",
        "Best": "4",
        "Masterpiece": "5"
    }

    GENRE_CHOICES = [(code, label) for label, code in genre_dict.items()]
    RATING_CHOICES = [(code, label) for label, code in rating.items()]

    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilma_tarihi = models.DateTimeField(default=timezone.now())
    yayinlanma_tarihi = models.DateTimeField(blank=True, null=True)
    tur = models.CharField(max_length=200, choices=GENRE_CHOICES, default='G')
    puan = models.CharField(max_length=200, choices=RATING_CHOICES, default=1)

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
    avatar = models.ImageField(blank=True, null=True, default ='indiedeveloper.jpg')
    followers = models.ManyToManyField(User, related_name='is_following', blank = True)
    #person.profile.followers.all() ->takipçilerim
    #person..is_following.all() ->kimi takip ediyorum

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
        profile = Profile.objects.create(user=instance)
        profile.followers.add(2) #id 2 kullanıcıyı direk yeni kullanıcının takipçisi yapıyoruz


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Like(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Post, related_name='likes')