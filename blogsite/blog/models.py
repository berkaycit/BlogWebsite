from django.db import models
from django.utils import timezone

class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilma_tarihi = models.DateTimeField(default=timezone.now)
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




